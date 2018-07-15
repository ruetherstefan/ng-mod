# Module:

# Weichen_Control
# Steuerung von Weichen
# Communication with Intellibox (IB) via serial COM port
#
#
# History:
# 06.03.2016 - 1.01: Command Lok_stop() with realtime measurement
# 16.03.2016 - 1.02: Command Lok_go(), Read & print of IB answers
# 17.03.2016 - 1.03: Implementation of Hex commands variants
# 13.03.2018 - 2.01: Aufteilung in Module lok_Control und weichen_control

import serial
# import timeit
import time

# Global definition of the COM port
ser = serial.Serial('COM4')  # open serial port
CONF_RUNTIME = True
CONF_DEBUG = True
CONF_HEX = True


def initialisation():
    if CONF_RUNTIME:
        timestamp = time.perf_counter()

    ser.bautrate = 9600
    ser.stopbits = 2
    ser.rtscts = False

    if CONF_DEBUG:
        print('Initialisation() -> Used COM Port', ser.name)  # check which port was really used

    if CONF_RUNTIME:
        print('Runtime of Initialisation:', time.perf_counter() - timestamp, 'sec\n')


def de_initialisation():
    if CONF_RUNTIME:
        timestamp = time.perf_counter()

    ser.close()  # close serial port

    if CONF_RUNTIME:
        print('Runtime of De_Initialisation:', time.perf_counter() - timestamp, 'sec\n')


# Alle Loks werden nach Nothalt wieder mit Fahrspannung versorgt.
# Identisch mit der Funktionstaste 'go" an der IB
def lok_go():
    if CONF_RUNTIME:
        timestamp = time.perf_counter()

    if not CONF_HEX:
        ser.write(b'go\r')
        Answer = ser.read()
        Answer = Answer + ser.read()
        Answer = Answer + ser.read()
        Answer = Answer + ser.read()
        Answer = Answer + ser.read()
        Answer = Answer + ser.read()
        Answer = Answer + ser.read()
        Answer = Answer + ser.read()
        if CONF_DEBUG:
            print('Answer IB Lok_go(ASCCI): ', Answer, '\n')

    if CONF_HEX:
        ser.write(b'\xA7')
        Answer = ser.read()
        if CONF_DEBUG:
            print('Answer IB Lok_go(HEX)(0 = OK)', Answer)

    if CONF_DEBUG:
        print('Lok_go() finished')

    if CONF_RUNTIME:
        print('Runtime of Lok_go():', time.perf_counter() - timestamp, 'sec\n')


def lok_stop_pwr_off():
    """
    # Stop aller Loks, Nothalt durch abschalten der Fahrspannung.
    # Identisch mit der Funktionstaste 'stop" an der IB
    """
    if CONF_RUNTIME:
        timestamp = time.perf_counter()

    if not CONF_HEX:
        print('if conf_hex==false')
        ser.write(b'stop\r')
        # Problemstellung:
        # Buffer auslesen bei bekannter Länge oder bekanntem letzten Zeichen: Kein Problem!
        # Aber wie kann eine Ausnahmebehandlung entwickeln, damit sich das Programm nicht aufhängt,
        # wenn die Intellibox nicht reagiert?
        # Bisher keine Lösung gefunden.

        # Der Versuch, den Input Buffer auszulesen, bis dieser geleert ist, scheint nicht möglich.
        # Answer = ser.iread_until(ser, '\r', 10)
        # print('Answer_S: ', bytes())
        Answer = ser.read()
        Answer = Answer + ser.read()
        Answer = Answer + ser.read()
        Answer = Answer + ser.read()
        Answer = Answer + ser.read()
        Answer = Answer + ser.read()
        Answer = Answer + ser.read()
        Answer = Answer + ser.read()
        Answer = Answer + ser.read()
        if CONF_DEBUG:
            print('Answer IB Lok_stop(ASCCI): ', Answer)

    if CONF_HEX:
        ser.write(b'\xA6')
        Answer = ser.read()
        if CONF_DEBUG:
            print('Answer IB Lok_stop(HEX)(0 = OK)', Answer)

    if CONF_DEBUG:
        print('Lok_stop() finished')

    if CONF_RUNTIME:
        print('Runtime of Lok_stop():', time.perf_counter() - timestamp, 'sec\n')


# Stop aller Loks, Nothalt OHNE abschalten der Fahrspannung.
def lok_halt():
    if CONF_RUNTIME:
        timestamp = time.perf_counter()

    if CONF_HEX:
        ser.write(b'\xA5')
        Answer = ser.read()
        if CONF_DEBUG:
            print('Answer IB Lok_halt(HEX)(0 = OK)', Answer)
    else:
        raise Exception("Cmd lok_halt not supported for ASCCI mode:")

    if CONF_DEBUG:
        print('Lok_halt() finished')

    if CONF_RUNTIME:
        print('Runtime of Lok_halt():', time.perf_counter() - timestamp, 'sec\n')


# function lok_cmd()
# Control of one Lok, with all relevant parameters
#
# Parameters (byte)
# 1st	low byte of Lok address
# 2nd	high byte of Lok address
# 3rd	speed (0..127: 0 = Stop, 1 = Stop/Em.Stop)
# 	N.B. bit #7 is reserved for future use!
# 4th	this byte has the following format:
#
# 	bit#   7     6     5     4     3     2     1     0
#	    +-----+-----+-----+-----+-----+-----+-----+-----+
#	    |ChgF |Force| Dir | FL  | F4  | F3  | F2  | F1  |
#	    +-----+-----+-----+-----+-----+-----+-----+-----+
#
# 	where:
# 		ChgF	set if F1..F4 to be used for setting F1..F4 of
#			Lok (otherwise F1..F4 are ignored)
# 		Force	if set (1), then the XLok command is 'forced'
# 			even in case of a Lok already controlled by a
# 			non-PC device
# 		Dir	Lok direction: 1 = forward, 0 = reverse
# 		FL	Lok light status: 1 = on, 0 = off
# 		F4..F1	Lok F4..F1 status (if ChgF is set)
#
# N.B.	Address must be in range 0..9999
# 	(depending on protocol, not every address is legal!)
#
# Remark:  F2..F4 are not supported here, because no lok with this functions avaliable
def lok_cmd(addr_low, addr_high, speed, direction, frontlight, f1):
    if CONF_RUNTIME:
        timestamp = time.perf_counter()

    if CONF_HEX:
        # with this command we setting F1..F4 and
        # forcing the cmd that PC and IB can work in parallel
        var_4th_byte = 0xc0
        if direction:
            var_4th_byte = var_4th_byte + 0x20
        if frontlight:
            var_4th_byte = var_4th_byte + 0x10
        if f1:
            var_4th_byte = var_4th_byte + 0x01
        # Remark:  F2..F4 are not supported here, because no lok with this functions available
        if CONF_DEBUG:
            print('4th byte', var_4th_byte)

        string = addr_low + addr_high + speed + var_4th_byte
        if CONF_DEBUG:
            print('sting', string)

        # XLok (080h) + 4 Byte
        # ser.write(b'\x80')
        Answer = ser.read()
        # if CONF_DEBUG:
        # print('Answer IB Lok_cmd(HEX)(0 = OK)', Answer)
    else:
        raise Exception("Cnd lok_cmd not supported for ASCCI mode:")

    if CONF_DEBUG:
        print('Lok_cmd() finished')

    if CONF_RUNTIME:
        print('Runtime of Lok_cmd():', time.perf_counter() - timestamp, '\n')


#################
# Hauptprogramm:
#################

initialisation()

# --------------------------------------
# Test 1:
# Aus- und einschalten der Lokversorgung
lok_halt()
# nachfolgender Reset hat nicht die Auswirkung, dass restliche Bytes im Buffer gelöscht werden.
# ser.reset_input_buffer()
lok_go()
# --------------------------------------

# --------------------------------------
# Test 2:
lok_cmd(10, 00, 15, True, False, False)

de_initialisation()
