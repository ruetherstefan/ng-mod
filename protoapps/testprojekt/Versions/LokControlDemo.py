from src.model.Lok import Lok
from src.serial import SerialConnector
from src.serial.LokControl import LokControl

SerialConnector.initialisation()

lok: Lok = Lok(1000)
lok.speed = 60
lok.f1 = True
lok.f2 = False
lok.f3 = True
lok.f4 = True
lok.forwaerts = False
lok.frontlicht = False
LokControl().lok_fahre(lok)

SerialConnector.de_initialisation()
