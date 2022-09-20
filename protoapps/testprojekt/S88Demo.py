
from src.serial import SerialConnector
from src.serial.Signal88Control import Signal88Control





SerialConnector.initialisation()

Signal88Control().lese_signale(1)

SerialConnector.de_initialisation()
