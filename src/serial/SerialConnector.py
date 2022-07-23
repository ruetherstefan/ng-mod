import serial.tools.list_ports


def is_offline():
    comports = serial.tools.list_ports.comports()
    if not comports:
        return True
    elif len(comports) == 1 and comports[0].description == 'Intel(R) Active Management Technology - SOL (COM3)':
        return True
    else:
        return False

