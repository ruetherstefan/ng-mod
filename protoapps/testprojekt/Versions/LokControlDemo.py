import time
import serial

from src.model.Lok import Lok
from src.serial.LokControl import LokControl


def initialisation():
    if CONF_RUNTIME:
        timestamp = time.perf_counter()

    # ser.bautrate = 9600
    ser.baudrate = 4800
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



CONF_RUNTIME = True
CONF_DEBUG = False
CONF_HEX = True

# Global definition of the COM port
ser = serial.Serial('COM3')
initialisation()

lok: Lok = Lok(200)
lok.speed = 20
LokControl().lok_fahre(lok, ser)



de_initialisation()
