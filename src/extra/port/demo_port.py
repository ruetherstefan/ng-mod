import serial

__author__ = 'jan'

# port = '/dev/ttyUSB0'
port = 'COM3'

ser = serial.Serial(port, 19200, timeout=1)
ser.write('1')
ser.close()
