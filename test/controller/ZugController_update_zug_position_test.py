from src.model.BesetztModul import BesetztModul
from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.model.zug.Fahrstrecke import Fahrstrecke
from src.model.zug.Zug import Zug
from src.controller.ZugController import ZugController


def gegeben_fahrstrecke_mit_3_bereichen():
    fahrstrecke: Fahrstrecke = Fahrstrecke()
    fahrstrecke.besetzt_module = [BesetztModul(BesetztModulAdresse.H1),
                                  BesetztModul(BesetztModulAdresse.H2),
                                  BesetztModul(BesetztModulAdresse.H3)]

    return fahrstrecke, fahrstrecke.besetzt_module[0], fahrstrecke.besetzt_module[1], fahrstrecke.besetzt_module[2]


def gegeben_zug_mit_vorposition(ende, anfang):
    zug: Zug = Zug()
    zug.ende = ende
    zug.anfang = anfang

    return zug


def test_update_zug_position_keine_veraenderung_zug2_lang():
    fahrstrecke, bereich1, bereich2, bereich3 = gegeben_fahrstrecke_mit_3_bereichen()
    zug = gegeben_zug_mit_vorposition(bereich1, bereich2)
    bereich1.besetzt = True
    bereich2.besetzt = True

    ZugController().update_zug_position(zug, fahrstrecke)
    assert bereich1 == zug.ende
    assert bereich2 == zug.anfang


def test_update_zug_position_keine_veraenderung_zug1_lang():
    fahrstrecke, bereich1, bereich2, bereich3 = gegeben_fahrstrecke_mit_3_bereichen()
    zug = gegeben_zug_mit_vorposition(bereich1, bereich1)
    bereich1.besetzt = True

    ZugController().update_zug_position(zug, fahrstrecke)
    assert bereich1 == zug.ende
    assert bereich1 == zug.anfang


def test_update_zug_position_keine_veraenderung_zug1_lang_weiter_hinten():
    fahrstrecke, bereich1, bereich2, bereich3 = gegeben_fahrstrecke_mit_3_bereichen()
    zug = gegeben_zug_mit_vorposition(bereich2, bereich2)
    bereich2.besetzt = True

    ZugController().update_zug_position(zug, fahrstrecke)
    assert bereich2 == zug.ende
    assert bereich2 == zug.anfang


def test_update_zug_position_weiter_gefahren_zug1_zu_2_lang():
    fahrstrecke, bereich1, bereich2, bereich3 = gegeben_fahrstrecke_mit_3_bereichen()
    zug = gegeben_zug_mit_vorposition(bereich1, bereich1)
    bereich1.besetzt = True
    bereich2.besetzt = True

    ZugController().update_zug_position(zug, fahrstrecke)
    assert bereich1 == zug.ende
    assert bereich2 == zug.anfang


def test_update_zug_position_weiter_gefahren_zug2_zu_3_lang():
    fahrstrecke, bereich1, bereich2, bereich3 = gegeben_fahrstrecke_mit_3_bereichen()
    zug = gegeben_zug_mit_vorposition(bereich1, bereich2)
    bereich1.besetzt = True
    bereich2.besetzt = True
    bereich3.besetzt = True

    ZugController().update_zug_position(zug, fahrstrecke)
    assert bereich1 == zug.ende
    assert bereich3 == zug.anfang


def test_update_zug_position_weiter_gefahren_zug1_zu_1_lang():
    fahrstrecke, bereich1, bereich2, bereich3 = gegeben_fahrstrecke_mit_3_bereichen()
    zug = gegeben_zug_mit_vorposition(bereich1, bereich1)
    bereich2.besetzt = True

    ZugController().update_zug_position(zug, fahrstrecke)
    assert bereich2 == zug.ende
    assert bereich2 == zug.anfang


def test_update_zug_position_weiter_gefahren_zug2_zu_1_lang():
    fahrstrecke, bereich1, bereich2, bereich3 = gegeben_fahrstrecke_mit_3_bereichen()
    zug = gegeben_zug_mit_vorposition(bereich1, bereich2)
    bereich2.besetzt = True

    ZugController().update_zug_position(zug, fahrstrecke)
    assert bereich2 == zug.ende
    assert bereich2 == zug.anfang


def test_update_zug_position_weiter_gefahren_zug3_zu_2_lang():
    fahrstrecke, bereich1, bereich2, bereich3 = gegeben_fahrstrecke_mit_3_bereichen()
    zug = gegeben_zug_mit_vorposition(bereich1, bereich3)
    bereich2.besetzt = True
    bereich3.besetzt = True

    ZugController().update_zug_position(zug, fahrstrecke)
    assert bereich2 == zug.ende
    assert bereich3 == zug.anfang


def test_update_zug_position_fehlerfall_zug_weg():
    fahrstrecke, bereich1, bereich2, bereich3 = gegeben_fahrstrecke_mit_3_bereichen()
    zug = gegeben_zug_mit_vorposition(bereich1, bereich3)

    ZugController().update_zug_position(zug, fahrstrecke)
    assert None is zug.ende
    assert None is zug.anfang