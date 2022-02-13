from src.model.Gleisbelegung import Gleisbelegung
from src.model.Weichenstellung import Weichenstellung
from src.serial.WeichenControlBote import WeichenControlBote


class Weiche:

    def __init__(self, weichenadresse):
        self.adresse = weichenadresse
        self.weichenstellung = Weichenstellung.GERADE
        self.gleisbelegung = Gleisbelegung.FREI

    def toggleFahrstrasse(self):
        if Gleisbelegung.FREI == self.gleisbelegung:
            self.gleisbelegung = Gleisbelegung.FAHRSTRASSE
        elif Gleisbelegung.FAHRSTRASSE == self.gleisbelegung:
            self.gleisbelegung = Gleisbelegung.FREI
