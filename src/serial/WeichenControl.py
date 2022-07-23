"""
Module:  Weichen_Control
Steuerung von Weichen (englisch turnouts)
Communication with Intellibox (IB) via serial COM port

History:
06.03.2016 - 1.01: Command Lok_stop() with realtime measurement
16.03.2016 - 1.02: Command Lok_go(), Read & print of IB answers
17.03.2016 - 1.03: Implementation of Hex commands variants
13.03.2018 - 2.01: Aufteilung in Module lok_Control und weichen_control
23.09.2018 - 2.02: Erste Implementation von turnout_set_for_route() und turnout_free().
                   Achtung: Die Funktionen erwarten Stings fuer die Adressbytes. Das könnte genauso wie die
                   Reihenfolge der Adressbytes geändert werden.
                   Achtung: z.Zt. str_addr_high ohne Funktion. Deshalb nur Weichenadressen 1-255 unterstützt!
18.03.2022 - 2.03: Überarbeitung der Kommentare.
                   ser.bautrate in ser.baudrate  geändert aber noch nicht geprüft.
"""
import timeit
import time

from src.serial import SerialConnector
from src.serial.WeichenControlInterface import WeichenControlInterface


class WeichenControl(WeichenControlInterface):

    CONF_RUNTIME = True
    CONF_DEBUG = False
    CONF_HEX = True

    """
    Ansteuerung einer Weiche (eng. turnouts)
    für das Einstellen einer Fahrstrasse (route).
    Während die Fahrstrasse eingestellt ist, muss die Bedienung durch die IB verboten werden.
    Deshalb wird in dieser Funktion die Weiche (für den PC) reserviert.
    Die Reservierung muss später wieder aufgehoben werden mit turnout_free().
    """
    def turnout_set_for_route(self, str_addr_low, str_addr_high, bol_color):

        if self.CONF_RUNTIME:
            timestamp = time.perf_counter()

        #if addr_high>0x07:
            # raise Exception('Cmd turnout_set_for_route: Parameter addr_high must not > 0x07!')
        #    print('Cmd turnout_set_for_route: Parameter addr_high must not > 0x07!')

        if self.CONF_HEX:
            # with this command we're setting F1...F4 and
            # forcing the cmd that PC and IB can work in parallel
            # var_2nd_byte = 0x60 + addr_high
            if bol_color:
                string_2nd_byte = b'\xE0'
            else:
                string_2nd_byte = b'\x60'

            if self.CONF_DEBUG:
                print('2nd byte', string_2nd_byte)

            # string = addr_low + addr_high + var_2nd_byte
            # if CONF_DEBUG:
            #    print('sting', string)

            # XTrnt (090h) + 2 Byte
            string1 = b'\x90'
            SerialConnector.ser.write(string1)

            SerialConnector.ser.write(str_addr_low)

            # string3 = b'\xE0'
            SerialConnector.ser.write(string_2nd_byte)

            # ser.write(b'\xA7')
            # ser.write(var_2nd_byte)

            Answer = SerialConnector.ser.read()
            if self.CONF_DEBUG:
                print('Answer IB turnout_set_for_route(HEX)(0 = OK)', Answer)
        else:
            # raise Exception('Cmd turnout_set_for_route not supported for ASCCI mode:')
            print('Cmd turnout_set_for_route not supported for ASCCI mode:')

        if self.CONF_DEBUG:
            print('turnout_set_for_route() finished')

        if self.CONF_RUNTIME:
            print('Runtime of turnout_set_for_route():', time.perf_counter() - timestamp, 'sec\n')


    """
    Zurücknahme der Reservierung einer Weiche (engl. turnout)
    nach Einstellen einer Fahrstrasse (route).
    """
    def turnout_free(self, str_addr_low, str_addr_high):
        """


        :rtype: object
        """
        if self.CONF_RUNTIME:
            timestamp = time.perf_counter()

        # if addr_high>0x07:
            # raise Exception('Cmd turnout_set_for_route: Parameter addr_high must not > 0x07!')
        #    print('Cmd turnout_set_for_route: Parameter addr_high must not > 0x07!')

        if self.CONF_HEX:
            # NoCmd Bit setzten, um die Reservierung zurückzunehmen.
            string_2nd_byte = b'\x10'


            if self.CONF_DEBUG:
                print('2nd byte', string_2nd_byte)

            # string = addr_low + addr_high + var_2nd_byte
            # if CONF_DEBUG:
            #    print('sting', string)

            # XTrnt (090h) + 2 Byte
            string1 = b'\x90'
            SerialConnector.ser.write(string1)

            SerialConnector.ser.write(str_addr_low)

            SerialConnector.ser.write(string_2nd_byte)

            Answer = SerialConnector.ser.read()
            if self.CONF_DEBUG:
                print('Answer IB turnout_set_for_route(HEX)(0 = OK)', Answer)
        else:
            # raise Exception('Cmd turnout_set_for_route not supported for ASCII mode:')
            print('Cmd turnout_free not supported for ASCII mode:')

        if self.CONF_DEBUG:
            print('turnout_free() finished')

        if self.CONF_RUNTIME:
            print('Runtime of turnout_free():', time.perf_counter() - timestamp, 'sec\n')
