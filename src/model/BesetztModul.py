from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.model.Gleisbelegung import Gleisbelegung


class BesetztModul:
    def __init__(self, adresse):
        self.adresse: BesetztModulAdresse = adresse
        self.fahrstrasse: bool = False
        self.besetzt: bool = False

    def gleisbelegung(self):
        if self.besetzt:
            return Gleisbelegung.BESETZT
        elif self.fahrstrasse:
            return Gleisbelegung.FAHRSTRASSE
        else:
            return Gleisbelegung.FREI


class BesetztModulVerwalter:
    def __init__(self, module):
        self.module: {BesetztModul} = module

    def get(self, adresse) -> BesetztModul:
        return list(filter(lambda a: a.adresse is adresse, self.module))[0]
