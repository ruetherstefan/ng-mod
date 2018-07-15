import serial
# import timeit
import time

# Global definition of the COM port
ser = serial.Serial('COM3')  # open serial port
CONF_RUNTIME = True
CONF_DEBUG = True


# def Runtime_measure_start():
#     if CONF_RUNTIME == True:
#        timestamp = time.perf_counter()


def Initialisation():
    if CONF_RUNTIME == True:
        timestamp = time.perf_counter()

    ser.bautrate = 9600
    ser.stopbits = 2
    ser.rtscts = True

    if CONF_DEBUG == True:
        print("Initialisation() -> Used COM Port", ser.name)  # check which port was really used

    if CONF_RUNTIME == True:
        print("Runtime of Initialisation:", time.perf_counter() - timestamp)


def De_Initialisation():
    if CONF_RUNTIME == True:
        timestamp = time.perf_counter()

    ser.close()  # close serial port

    if CONF_RUNTIME == True:
        print("Runtime of De_Initialisation:", time.perf_counter() - timestamp)


def Lok_stop():
    if CONF_RUNTIME == True:
        timestamp = time.perf_counter()

    ser.write(b'stop\r')

    if CONF_RUNTIME == True:
        print("Runtime of Lok_stop():", time.perf_counter() - timestamp)

    print('Lok_stop() finished\n')


#################
# Hauptprogramm:
#################

Initialisation()
Lok_stop()
De_Initialisation()
