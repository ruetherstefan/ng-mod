from unittest.mock import Mock

from src.model.BesetztModul import BesetztModulVerwalter
from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.serial import SerialConnector
from src.serial.Signal88Control import Signal88Control


class Signal88ControlBote:
    def __init__(self):
        self.besetzt_modul_adress_mappings__module1: {BesetztModulAdresse: int} = {BesetztModulAdresse.H1: 0,
                                                                                   BesetztModulAdresse.H2: 1,
                                                                                   BesetztModulAdresse.H3: 3}

        self.signal_88_control: Signal88Control = Signal88Control()
        if SerialConnector.is_offline():
            self.signal_88_control = Mock(spec=Signal88Control)
            self.signal_88_control.lese_signale = Mock(
                return_value=[True, False, False, False, False, False, False, False])

    def update_module(self, verwalter: BesetztModulVerwalter):
        aenderungs_flag = False

        modul1 = self.signal_88_control.lese_signale(1)
        for adresse in self.besetzt_modul_adress_mappings__module1:

            ausgelesener_wert = modul1[self.besetzt_modul_adress_mappings__module1[adresse]]
            if verwalter.get(adresse).besetzt != ausgelesener_wert:
                verwalter.get(adresse).besetzt = ausgelesener_wert
                aenderungs_flag = True

        return aenderungs_flag
