# Module:
# Communication with Intellibox (IB) via serial COM port
#
#
# History:
# 06.03.2016 - 1.01: Command Lok_stop() with realtime measurement
# 16.03.2016 - 1.02: Command Lok_go(), Read & print of IB answers
# 17.03.2016 - 1.03: Implementation of Hex commands variants

import serial
# import timeit
import time

# Global definition of the COM port
ser = serial.Serial('COM7')  # open serial port
CONF_RUNTIME = True
CONF_DEBUG = False
CONF_HEX = True


# def Runtime_measure_start():
#     if CONF_RUNTIME == True:
#        timestamp = time.perf_counter()


def initialisation():
    if CONF_RUNTIME:
        timestamp = time.perf_counter()

    ser.bautrate = 9600
    ser.stopbits = 2
    ser.rtscts = False

    if CONF_DEBUG:
        print("Initialisation() -> Used COM Port", ser.name)  # check which port was really used

    if CONF_RUNTIME:
        print("Runtime of Initialisation:", time.perf_counter() - timestamp, '\n')


def de_initialisation():
    if CONF_RUNTIME:
        timestamp = time.perf_counter()

    ser.close()  # close serial port

    if CONF_RUNTIME:
        print("Runtime of De_Initialisation:", time.perf_counter() - timestamp)


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
            print("Antwort IB Lok_go(ASCCI): ", Answer, "\n")

    if CONF_HEX:
        ser.write(b'\xA7')
        Answer = ser.read()
        if CONF_DEBUG:
            print("Antwort IB Lok_go(HEX)(0 = OK)", Answer)

    if CONF_DEBUG:
        print('Lok_go() finished\n')

    if CONF_RUNTIME:
        print("Runtime of Lok_go():", time.perf_counter() - timestamp)


def lok_stop():
    if CONF_RUNTIME:
        timestamp = time.perf_counter()

    if not CONF_HEX:
        print("if conf_hex==false")
        ser.write(b'stop\r')
        # Problemstellung:
        # Buffer auslesen bei bekannter Länge oder bekanntem letzten Zeichen: Kein Problem!
        # Aber wie kann eine Ausnahmebehandlung entwickeln, damit sich das Programm nicht aufhängt,
        # wenn die Intellibox nicht reagiert?
        # Bisher keine Lösung gefunden.

        # Der Versuch, den Input Buffer auszulesen, bis dieser geleert ist, scheint nicht möglich.
        # Answer = ser.iread_until(ser, '\r', 10)
        # print("Antwort_S: ", bytes())
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
            print("Antwort IB Lok_stop(ASCCI): ", Answer)

    if CONF_HEX:
        ser.write(b'\xA6')
        Answer = ser.read()
        if CONF_DEBUG:
            print("Antwort IB Lok_stop(HEX)(0 = OK)", Answer)

    if CONF_DEBUG:
        print('Lok_stop() finished\n')

    if CONF_RUNTIME:
        print("Runtime of Lok_stop():", time.perf_counter() - timestamp)



#################
# Hauptprogramm:
#################

initialisation()


lok_stop()

# nachfolgender Reset hat nicht die Auswirkung, dass restliche Bytes im Buffer gelöscht werden.
# ser.reset_input_buffer()

lok_go()


de_initialisation()
