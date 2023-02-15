from src.model.BesetztModul import BesetztModul, BesetztModulVerwalter
from src.model.BesetztModulAdresse import BesetztModulAdresse


def test_besetz_modul_verwalter():
    modul1 = BesetztModul(BesetztModulAdresse.H1)
    modul2 = BesetztModul(BesetztModulAdresse.H2)
    verwalter = BesetztModulVerwalter({modul1, modul2})
    assert modul1 is verwalter.get(BesetztModulAdresse.H1)
    assert modul2 is verwalter.get(BesetztModulAdresse.H2)
