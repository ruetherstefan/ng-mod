import time

import serial
import serial.tools.list_ports

CONF_RUNTIME = True
CONF_DEBUG = False
CONF_HEX = True


def is_offline():
    comports = serial.tools.list_ports.comports()
    if not comports:
        return True
    elif len(comports) == 1 and comports[0].description == 'Intel(R) Active Management Technology - SOL (COM3)':
        return True
    else:
        return False


def initialisation():
    if not is_offline():
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
    if not is_offline():
        """
    
        :rtype: object
        """
        if CONF_RUNTIME:
            timestamp = time.perf_counter()

        ser.close()  # close serial port

        if CONF_RUNTIME:
            print('Runtime of De_Initialisation:', time.perf_counter() - timestamp, 'sec\n')


if not is_offline():
    comports = serial.tools.list_ports.comports()

    if len(comports) == 1:
        ser = serial.Serial('COM5')
    else:
        ser = serial.Serial('COM4')
