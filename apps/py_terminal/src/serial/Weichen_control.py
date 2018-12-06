# Module:

# Weichen_Control
# Steuerung von Weichen (englisch turnouts)
# Communication with Intellibox (IB) via serial COM port
#
#
# History:
# 06.03.2016 - 1.01: Command Lok_stop() with realtime measurement
# 16.03.2016 - 1.02: Command Lok_go(), Read & print of IB answers
# 17.03.2016 - 1.03: Implementation of Hex commands variants
# 13.03.2018 - 2.01: Aufteilung in Module lok_Control und weichen_control
# 23.09.2018 - 2.02. Erste Implemetation von turnout_set_for_route() und turnout_free().
#                    Achtung: Die Funktionen erwarten Stings fuer die Adressbytes. Das koennte genauso wie die
#                    Reihenfolge der Adressbytes geaendert werden.
#                    Achtung: z.Zt. str_addr_high ohne Funktion. Deshalb nur Weichenadressen 1-255 unterstuetzt!

import serial
# import timeit
import time

# Global definition of the COM port
ser = serial.Serial('COM3')  # open serial port
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
    """

    :rtype: object
    """
    if CONF_RUNTIME:
        timestamp = time.perf_counter()

    ser.close()  # close serial port

    if CONF_RUNTIME:
        print('Runtime of De_Initialisation:', time.perf_counter() - timestamp, 'sec\n')


# -------------------------------------------------------------------------------------------
# Ansteuerung einer Weiche (engl. turnouts)
# fuer das Einstellen einer Fahrstrasse (route).
# Waehrend die Fahrstrasse eingestellt ist, muss die Bedienung durch die IB verboten werden.
# Deshalb wird in dieser Funktion die Weiche (fuer den PC) reserviert.
# Die Reservierung muss spaeter wieder aufgegoben werden mit turnout_free().
# -------------------------------------------------------------------------------------------
def turnout_set_for_route(str_addr_low, str_addr_high, bol_color):

    if CONF_RUNTIME:
        timestamp = time.perf_counter()

    #if addr_high>0x07:
        # raise Exception('Cmd turnout_set_for_route: Parameter addr_high must not > 0x07!')
    #    print('Cmd turnout_set_for_route: Parameter addr_high must not > 0x07!')

    if CONF_HEX:
        # with this command we setting F1..F4 and
        # forcing the cmd that PC and IB can work in parallel
        #var_2nd_byte = 0x60 + addr_high
        if bol_color:
            string_2nd_byte = b'\xE0'
        else:
            string_2nd_byte = b'\x60'

        if CONF_DEBUG:
            print('2nd byte', string_2nd_byte)

        #string = addr_low + addr_high + var_2nd_byte
        #if CONF_DEBUG:
        #    print('sting', string)

        # XTrnt (090h) + 2 Byte
        string1 = b'\x90'
        ser.write(string1)

        ser.write(str_addr_low)

        # string3 = b'\xE0'
        ser.write(string_2nd_byte)

        #ser.write(b'\xA7')
        # ser.write(var_2nd_byte)

        Answer = ser.read()
        if CONF_DEBUG:
            print('Answer IB turnout_set_for_route(HEX)(0 = OK)', Answer)
    else:
        # raise Exception('Cmd turnout_set_for_route not supported for ASCCI mode:')
        print('Cmd turnout_set_for_route not supported for ASCCI mode:')

    if CONF_DEBUG:
        print('turnout_set_for_route() finished')

    if CONF_RUNTIME:
        print('Runtime of turnout_set_for_route():', time.perf_counter() - timestamp, 'sec\n')






# -------------------------------------------------------------------------------------------
# Zuruecknahme der Reservierung einer Weiche (engl. turnout)
# nach Einstellen einer Fahrstrasse (route).
# -------------------------------------------------------------------------------------------
def turnout_free(str_addr_low, str_addr_high):

    """

    :rtype: object
    """
    if CONF_RUNTIME:
        timestamp = time.perf_counter()

    #if addr_high>0x07:
        # raise Exception('Cmd turnout_set_for_route: Parameter addr_high must not > 0x07!')
    #    print('Cmd turnout_set_for_route: Parameter addr_high must not > 0x07!')

    if CONF_HEX:
       # NoCmd Bit setzten um die reservierung zurueck zu nehmen.
        string_2nd_byte = b'\x10'


        if CONF_DEBUG:
            print('2nd byte', string_2nd_byte)

        #string = addr_low + addr_high + var_2nd_byte
        #if CONF_DEBUG:
        #    print('sting', string)

        # XTrnt (090h) + 2 Byte
        string1 = b'\x90'
        ser.write(string1)

        ser.write(str_addr_low)

        ser.write(string_2nd_byte)

        Answer = ser.read()
        if CONF_DEBUG:
            print('Answer IB turnout_set_for_route(HEX)(0 = OK)', Answer)
    else:
        # raise Exception('Cmd turnout_set_for_route not supported for ASCCI mode:')
        print('Cmd turnout_free not supported for ASCCI mode:')

    if CONF_DEBUG:
        print('turnout_free() finished')

    if CONF_RUNTIME:
        print('Runtime of turnout_free():', time.perf_counter() - timestamp, 'sec\n')






#################
# Hauptprogramm:
#################


initialisation()

# --------------------------------------
# Weiche 1 der IB auf gruen = geradeaus
turnout_set_for_route(b'\01', b'\00', True)

# Weiche 1 der IB auf rot = abbiegen
turnout_set_for_route(b'\01', b'\00', False)

# Reservierung der Weiche für die Fahrstrasse zurueck nehmen.
turnout_free(b'\01', b'\00')

de_initialisation()
