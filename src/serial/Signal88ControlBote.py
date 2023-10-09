from unittest.mock import Mock

from src.model.BesetztModul import BesetztModulVerwalter
from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.serial import SerialConnector
from src.serial.Signal88Control import Signal88Control


class Signal88ControlBote:
    besetzt_modul_adress_mappings__module1: {BesetztModulAdresse: int} = {
        BesetztModulAdresse.B001_HAUPT_AUSFAHRT_LINKS: 0,
        BesetztModulAdresse.B002_HAUPT_AUSFAHRT_RECHTS_G1_SCHATTEN: 1,
        BesetztModulAdresse.B003_HAUPT_AUSFAHRT_RECHTS_G2_UND_G3_GUETER: 2,
        BesetztModulAdresse.B011_HAUPT_G1_HALTE_LINKS: 3,
        BesetztModulAdresse.B012_HAUPT_G1_MITTE: 4,
        BesetztModulAdresse.B013_HAUPT_G1_HALTE_RECHTS: 5,
        BesetztModulAdresse.B021_HAUPT_G2_HALTE_LINKS: 6,
        BesetztModulAdresse.B022_HAUPT_G2_MITTE: 7,
        BesetztModulAdresse.B023_HAUPT_G2_HALTE_RECHTS: 8,
        BesetztModulAdresse.B031_HAUPT_G3_HALTE_LINKS: 9,
        BesetztModulAdresse.B032_HAUPT_G3_MITTE: 10,
        BesetztModulAdresse.B033_HAUPT_G3_HALTE_RECHTS: 11
    }

    fake_results = {BesetztModulAdresse.B001_HAUPT_AUSFAHRT_LINKS: True,
                    BesetztModulAdresse.B011_HAUPT_G1_HALTE_LINKS: False,
                    BesetztModulAdresse.B012_HAUPT_G1_MITTE: False,
                    BesetztModulAdresse.B013_HAUPT_G1_HALTE_RECHTS: False}

    def __init__(self):
        self.signal_88_control: Signal88Control = Signal88Control()
        if SerialConnector.is_offline():
            self.fake_results = {BesetztModulAdresse.B001_HAUPT_AUSFAHRT_LINKS: True,
                                 BesetztModulAdresse.B011_HAUPT_G1_HALTE_LINKS: False,
                                 BesetztModulAdresse.B012_HAUPT_G1_MITTE: False,
                                 BesetztModulAdresse.B013_HAUPT_G1_HALTE_RECHTS: False}

            self.signal_88_control = Mock(spec=Signal88Control)
            self.signal_88_control.lese_signale = Mock(
                return_value=[Signal88ControlBote.fake_results[BesetztModulAdresse.B001_HAUPT_AUSFAHRT_LINKS],
                              Signal88ControlBote.fake_results[BesetztModulAdresse.B011_HAUPT_G1_HALTE_LINKS],
                              Signal88ControlBote.fake_results[BesetztModulAdresse.B012_HAUPT_G1_MITTE],
                              Signal88ControlBote.fake_results[BesetztModulAdresse.B013_HAUPT_G1_HALTE_RECHTS],
                              False, False,
                              False, False])

    def update_module(self, verwalter: BesetztModulVerwalter):
        aenderungs_flag = False

        modul1 = self.signal_88_control.lese_signale(1)
        for adresse in self.besetzt_modul_adress_mappings__module1:

            ausgelesener_wert = modul1[self.besetzt_modul_adress_mappings__module1[adresse]]
            if verwalter.get(adresse).besetzt != ausgelesener_wert:
                verwalter.get(adresse).besetzt = ausgelesener_wert
                aenderungs_flag = True

        return aenderungs_flag
