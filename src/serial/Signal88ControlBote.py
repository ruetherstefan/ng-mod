from unittest.mock import Mock

from src.model.BesetztModul import BesetztModul
from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.serial import SerialConnector
from src.serial.Signal88Control import Signal88Control


class Signal88ControlBote:
    def __init__(self):
        self.besetzt_modul_adress_mappings__module1: {BesetztModulAdresse: int} = {}

        self.signal_88_control = Signal88Control()
        if SerialConnector.is_offline():
            self.signal_88_control = Mock(spec=Signal88Control)

    def update_module(self, besetzt_module: [BesetztModul]):
        besetzt_module_map: {BesetztModulAdresse: BesetztModul} = self.erstelle_besetzt_modul_map_zur_adresse(besetzt_module)
        aenderungs_flag = False

        modul1 = self.signal_88_control.lese_signale(1)
        for adresse in self.besetzt_modul_adress_mappings__module1:

            ausgelesener_wert = modul1[self.besetzt_modul_adress_mappings__module1[adresse]]
            if besetzt_module_map[adresse].besetzt != ausgelesener_wert:
                besetzt_module_map[adresse].besetzt = ausgelesener_wert
                aenderungs_flag = True

        return aenderungs_flag

    @staticmethod
    def erstelle_besetzt_modul_map_zur_adresse(besetzt_module: [BesetztModul]):
        besetzt_module_map: {BesetztModulAdresse: BesetztModul} = {}
        for modul in besetzt_module:
            besetzt_module_map.update({modul.adresse: modul})
        return besetzt_module_map

