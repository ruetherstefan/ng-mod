from src.model.Gleisbelegung import Gleisbelegung
from src.model.Weichenstellung import Weichenstellung


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
