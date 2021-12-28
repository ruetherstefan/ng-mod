# Module:
# Communication with Intellibox (IB) via serial COM port
#
#
# History:
# 06.03.2016 - 1.01: Command Lok_stop() with realtime measurement
# 16.03.2016 - 1.02: Command Lok_go(), Read & print of IB answers



import serial
# import timeit
import time

# Global definition of the COM port
ser = serial.Serial('COM7')  # open serial port
CONF_RUNTIME = True
CONF_DEBUG = True


# def Runtime_measure_start():
#     if CONF_RUNTIME == True:
#        timestamp = time.perf_counter()


def Initialisation():
    if CONF_RUNTIME:
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


def Lok_go():
    if CONF_RUNTIME == True:
        timestamp = time.perf_counter()

    ser.write(b'go\r')

    if CONF_RUNTIME == True:
        print("Runtime of Lok_go():", time.perf_counter() - timestamp)

    print('Lok_go() finished\n')


#################
# Hauptprogramm:
#################

Initialisation()

# Ist hier nicht sinnvoll, da gerade geöffnete Schnittstelle geleerte Buffer hat.
# ser.reset_input_buffer()

Lok_stop()


# Der Versuch, den Input Buffer auszulesen, bis dieser geleert ist, scheint nicht möglich.
# Answer = ser.iread_until(ser, '\r', 10)
# print("Antwort_S: ", bytes())

# Problemstellung:
# Buffer auslesen bei bekannter Länge oder bekanntem letzten Zeichen: Kein Problem!
# Aber wie kann eine Ausnahmebehandlung entwickeln, damit sich das Programm nicht aufhängt, wenn die Intellibox nicht reagiert?
# Bisher keine Lösung gefunden.

Answer = ser.read()
print("Antwort: ", Answer)
Answer = Answer + ser.read()
print("Antwort: ", Answer)
Answer = Answer + ser.read()
print("Antwort: ", Answer)
Answer = Answer + ser.read()
print("Antwort: ", Answer)
Answer = Answer + ser.read()
print("Antwort: ", Answer)
Answer = Answer + ser.read()
print("Antwort: ", Answer)
Answer = Answer + ser.read()
print("Antwort: ", Answer)
Answer = Answer + ser.read()
print("Antwort: ", Answer)
Answer = Answer + ser.read()
print("Antwort: ", Answer, "\n")

# nachfolgender Reset hat nicht die Auswirkung, dass restliche Bytes im Buffer gelöscht werden.
# ser.reset_input_buffer()

Lok_go()

Answer = ser.read()
print("Antwort: ", Answer)
# Answer = Answer + ser.read()
# print("Antwort: ", Answer)
Answer = Answer + ser.read()
print("Antwort: ", Answer)
Answer = Answer + ser.read()
print("Antwort: ", Answer)
Answer = Answer + ser.read()
print("Antwort: ", Answer)
Answer = Answer + ser.read()
print("Antwort: ", Answer)
Answer = Answer + ser.read()
print("Antwort: ", Answer)
Answer = Answer + ser.read()
print("Antwort: ", Answer)
Answer = Answer + ser.read()
print("Antwort: ", Answer, "\n")

De_Initialisation()