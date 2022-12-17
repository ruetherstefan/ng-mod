from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.model.Gleisbelegung import Gleisbelegung


class BesetztModul:
    def __init__(self, adresse):
        self.adresse: BesetztModulAdresse = adresse
        self.fahrstrasse: bool = False
        self.besetzt: bool = False

    def gleisbelegung(self):
        if self.fahrstrasse:
            return Gleisbelegung.FAHRSTRASSE
        else:
            return Gleisbelegung.FREI

