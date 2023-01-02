from src.model.BesetztModul import BesetztModul
from src.model.Gleisbelegung import Gleisbelegung
from src.model.weiche.Weichenadresse import Weichenadresse
from src.model.weiche.Weichenstellung import Weichenstellung


class Weiche:

    def __init__(self, weichenadresse, besetztmodul):
        self.adresse: Weichenadresse = weichenadresse
        self.weichenstellung: Weichenstellung = Weichenstellung.GERADE
        self.besetztmodul: BesetztModul = besetztmodul
        self.gesperrt: bool = False

    def gleisbelegung(self):
        if self.gesperrt:
            return Gleisbelegung.GESPRERRT
        else:
            return self.besetztmodul.gleisbelegung()
