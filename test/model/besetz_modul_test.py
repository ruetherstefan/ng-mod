from src.model.BesetztModul import BesetztModul, BesetztModulVerwalter
from src.model.BesetztModulAdresse import BesetztModulAdresse


def test_besetz_modul_verwalter():
    modul1 = BesetztModul(BesetztModulAdresse.B001_HAUPT_AUSFAHRT_LINKS)
    modul2 = BesetztModul(BesetztModulAdresse.B011_HAUPT_G1_HALTE_LINKS)
    verwalter = BesetztModulVerwalter({modul1, modul2})
    assert modul1 is verwalter.get(BesetztModulAdresse.B001_HAUPT_AUSFAHRT_LINKS)
    assert modul2 is verwalter.get(BesetztModulAdresse.B011_HAUPT_G1_HALTE_LINKS)
