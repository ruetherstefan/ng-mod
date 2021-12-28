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
# 29.04.2019 - 2.03: Auslagerung der main Funktion in Modul weichen_test.

from _ctypes import *

import serial
# import timeit
import time
import ctypes




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



def turnout_set_for_route(char_address, bol_color):
    """
    Ansteuerung einer Weiche (engl. turnouts)
    fuer das Einstellen einer Fahrstrasse (route).
    Waehrend die Fahrstrasse eingestellt ist, muss die Bedienung durch die IB verboten werden.
    Deshalb wird in dieser Funktion die Weiche (fuer den PC) reserviert.
    Die Reservierung muss spaeter wieder aufgehoben werden mit turnout_free().

    Das folgende Format erwartet die IB:
    ====================================
    Byte1: Command XTrnt (090h) - length =
    Bytes 1+2 als Parameter:
    1st	low byte of Turnout address (A7..A0). Please note: turnout
	address, NOT turnout *decoder* address!
    2nd	high byte of Turnout address plus 'color' and status bits:

	bit#   7     6     5     4     3     2     1     0
	    +-----+-----+-----+-----+-----+-----+-----+-----+
	    |Color| Sts | Res |NoCmd| n.u.| A10 |  A9 |  A8 |
	    +-----+-----+-----+-----+-----+-----+-----+-----+

	where:
		Color	1 = closed (green), 0 = thrown (red)
		Sts	turnout status (1 = on, 0 = off)
		Res	set if this turnout is to be reserved
			for exclusive PC control: this would imply
			that non-PC commands to this turnout would
			be discarded by the IB. An event would also
			be generated (please check the XEvent cmd)
		NoCmd	if set then no turnout cmd is actually sent
			to the tracks. Setting this bit allows, e.g.,
			to only set/reset the 'Res' bit of a turnout.
			Besides, if NoCmd is set, not even the internal
			IB status of this turnout is modified.
		n.u.	not currently used (0)
		A10..A8	top address bits of turnout address

    :param char_address:     Address of turnout (Magnetartikel: Weiche) 0..255
    :param bol_color:       1 = closed (green), 0 = thrown (red)
    :return:
    """
    if CONF_RUNTIME:
        timestamp = time.perf_counter()

    # if addr_high>0x07:
        # raise Exception('Cmd turnout_set_for_route: Parameter addr_high must not > 0x07!')
    #    print('Cmd turnout_set_for_route: Parameter addr_high must not > 0x07!')

    if CONF_HEX:
        # with this command we setting F1..F4 and
        # forcing the cmd that PC and IB can work in parallel
        #var_2nd_byte = 0x60 + addr_high

        int_addr_low = char_address & 0xFF                   # low byte von address
        int_addr_high = (char_address & 0xFF00) % 0x100      # High byte von address per modulo

        if CONF_DEBUG:
            print('2nd byte', int_addr_low)
            print('3rt byte', int_addr_high)

#        if bol_color:
#            int_addr_high = int_addr_high + 0x80            # MSB setzen
        if bol_color:
            string_2nd_byte = b'\xE0'
        else:
            string_2nd_byte = b'\x60'

        #string_2nd_byte = ctypes.c_char(0x7f)          # unsigned char, 1 byte in python
        #string_2nd_byte = int_addr_high

        if CONF_DEBUG:
            print('3rt byte with color', string_2nd_byte)
            print(repr(string_2nd_byte)),    # dieser Typ soll keine Größe haben?

        # Wandlung in Hex  =>  0x2
        #str_addr_low = hex(int_addr_low)
        #string_2nd_byte = hex(int_addr_high)

        # Erwartetes Format: b'\02'
        #str_addr_low = "b'" + "\\" + str_addr_low[1:] + "'"
        #string_2nd_byte = "b'" + "\\" + string_2nd_byte[1:] + "'"


        if CONF_DEBUG:
            #print('String 2nd byte', str_addr_low)
            print('String 3rt byte', string_2nd_byte)

        # XTrnt (090h) + 2 Byte
        # send Command byte
        str_cmd = b'\x90'
        ser.write(str_cmd)

        if CONF_DEBUG:
            print('Command', str_cmd)

        str_addr_low = b'\x02'
        ser.write(str_addr_low)
#        ser.write(char_address)

        # int_addr_high = int_addr_high & 0xff
        ser.write(string_2nd_byte)

        #ser.write(b'\xA7')
        # ser.write(var_2nd_byte)

        Answer = ser.read()
        #Answer = "ohne IB"
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
        # send Command byte
        str_cmd = b'\x90'
        ser.write(str_cmd)

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

# verlagert nach Weichen_test.py