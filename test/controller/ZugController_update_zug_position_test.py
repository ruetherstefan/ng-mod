from src.controller.ZugController import ZugController
from src.model.BesetztModul import BesetztModul, BesetztModulVerwalter
from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.model.zug.Fahrstrecke import Fahrstrecke
from src.model.zug.Zug import Zug


def gegeben_fahrstrecke():
    fahrstrecke: Fahrstrecke = Fahrstrecke()
    fahrstrecke.besetzt_module = [BesetztModulAdresse.H1,
                                  BesetztModulAdresse.H2,
                                  BesetztModulAdresse.H3]
    return fahrstrecke


def gegeben_besetzmodul(adresse, besetzt):
    modul = BesetztModul(adresse)
    modul.besetzt = besetzt
    return modul


def gegeben_verwalter_mit_3_besetztmodulen(besetzt1, besetzt2, besetzt3):
    besetzmodul1 = gegeben_besetzmodul(BesetztModulAdresse.H1, besetzt1)
    besetzmodul2 = gegeben_besetzmodul(BesetztModulAdresse.H2, besetzt2)
    besetzmodul3 = gegeben_besetzmodul(BesetztModulAdresse.H3, besetzt3)
    return BesetztModulVerwalter({besetzmodul1, besetzmodul2, besetzmodul3})


def gegeben_zug_mit_vorposition(ende, anfang):
    zug: Zug = Zug()
    zug.ende = ende
    zug.anfang = anfang

    return zug


def test_update_zug_position_keine_veraenderung_zug2_lang():
    verwalter = gegeben_verwalter_mit_3_besetztmodulen(True, True, False)
    zug = gegeben_zug_mit_vorposition(BesetztModulAdresse.H1, BesetztModulAdresse.H2)

    ZugController().update_zug_position(zug, gegeben_fahrstrecke(), verwalter)
    assert BesetztModulAdresse.H1 == zug.ende
    assert BesetztModulAdresse.H2 == zug.anfang


def test_update_zug_position_keine_veraenderung_zug1_lang():
    verwalter = gegeben_verwalter_mit_3_besetztmodulen(True, False, False)
    zug = gegeben_zug_mit_vorposition(BesetztModulAdresse.H1, BesetztModulAdresse.H1)

    ZugController().update_zug_position(zug, gegeben_fahrstrecke(), verwalter)

    assert BesetztModulAdresse.H1 == zug.ende
    assert BesetztModulAdresse.H1 == zug.anfang


def test_update_zug_position_keine_veraenderung_zug1_lang_weiter_hinten():
    verwalter = gegeben_verwalter_mit_3_besetztmodulen(False, True, False)
    zug = gegeben_zug_mit_vorposition(BesetztModulAdresse.H2, BesetztModulAdresse.H2)

    ZugController().update_zug_position(zug, gegeben_fahrstrecke(), verwalter)
    assert BesetztModulAdresse.H2 == zug.ende
    assert BesetztModulAdresse.H2 == zug.anfang


def test_update_zug_position_weiter_gefahren_zug1_zu_2_lang():
    verwalter = gegeben_verwalter_mit_3_besetztmodulen(True, True, False)
    zug = gegeben_zug_mit_vorposition(BesetztModulAdresse.H1, BesetztModulAdresse.H1)

    ZugController().update_zug_position(zug, gegeben_fahrstrecke(), verwalter)
    assert BesetztModulAdresse.H1 == zug.ende
    assert BesetztModulAdresse.H2 == zug.anfang


def test_update_zug_position_weiter_gefahren_zug2_zu_3_lang():
    verwalter = gegeben_verwalter_mit_3_besetztmodulen(True, True, True)
    zug = gegeben_zug_mit_vorposition(BesetztModulAdresse.H1, BesetztModulAdresse.H2)

    ZugController().update_zug_position(zug, gegeben_fahrstrecke(), verwalter)
    assert BesetztModulAdresse.H1 == zug.ende
    assert BesetztModulAdresse.H3 == zug.anfang


def test_update_zug_position_weiter_gefahren_zug1_zu_1_lang():
    verwalter = gegeben_verwalter_mit_3_besetztmodulen(False, True, False)
    zug = gegeben_zug_mit_vorposition(BesetztModulAdresse.H1, BesetztModulAdresse.H1)

    ZugController().update_zug_position(zug, gegeben_fahrstrecke(), verwalter)
    assert BesetztModulAdresse.H2 == zug.ende
    assert BesetztModulAdresse.H2 == zug.anfang


def test_update_zug_position_weiter_gefahren_zug2_zu_1_lang():
    verwalter = gegeben_verwalter_mit_3_besetztmodulen(False, True, False)
    zug = gegeben_zug_mit_vorposition(BesetztModulAdresse.H1, BesetztModulAdresse.H2)

    ZugController().update_zug_position(zug, gegeben_fahrstrecke(), verwalter)
    assert BesetztModulAdresse.H2 == zug.ende
    assert BesetztModulAdresse.H2 == zug.anfang


def test_update_zug_position_weiter_gefahren_zug3_zu_2_lang():
    verwalter = gegeben_verwalter_mit_3_besetztmodulen(False, True, True)
    zug = gegeben_zug_mit_vorposition(BesetztModulAdresse.H1, BesetztModulAdresse.H3)

    ZugController().update_zug_position(zug, gegeben_fahrstrecke(), verwalter)
    assert BesetztModulAdresse.H2 == zug.ende
    assert BesetztModulAdresse.H3 == zug.anfang


def test_update_zug_position_fehlerfall_zug_weg():
    verwalter = gegeben_verwalter_mit_3_besetztmodulen(False, False, False)
    zug = gegeben_zug_mit_vorposition(BesetztModulAdresse.H1, BesetztModulAdresse.H3)

    ZugController().update_zug_position(zug, gegeben_fahrstrecke(), verwalter)
    assert None is zug.ende
    assert None is zug.anfang


def test_update_zug_position_fehlerfall_zug_wieder_da():
    verwalter = gegeben_verwalter_mit_3_besetztmodulen(False, True, False)
    zug = gegeben_zug_mit_vorposition(None, None)

    ZugController().update_zug_position(zug, gegeben_fahrstrecke(), verwalter)
    assert BesetztModulAdresse.H2 is zug.ende
    assert BesetztModulAdresse.H2 is zug.anfang


def test_update_zug_position_weiter_gefahren_vorherige_strecke_freigeben():
    verwalter = gegeben_verwalter_mit_3_besetztmodulen(False, True, False)
    zug = gegeben_zug_mit_vorposition(BesetztModulAdresse.H1, BesetztModulAdresse.H2)
    verwalter.get(BesetztModulAdresse.H1).fahrstrasse = True
    verwalter.get(BesetztModulAdresse.H2).fahrstrasse = True
    verwalter.get(BesetztModulAdresse.H3).fahrstrasse = True

    ZugController().update_zug_position(zug, gegeben_fahrstrecke(), verwalter)
    assert verwalter.get(BesetztModulAdresse.H1).fahrstrasse is False
    assert verwalter.get(BesetztModulAdresse.H2).fahrstrasse is True
    assert verwalter.get(BesetztModulAdresse.H3).fahrstrasse is True


def test_update_zug_position_nicht_weiter_gefahren_kreuzende_fahrstrasse_nicht_freigeben():
    verwalter = gegeben_verwalter_mit_3_besetztmodulen(False, True, False)
    zug = gegeben_zug_mit_vorposition(BesetztModulAdresse.H2, BesetztModulAdresse.H2)
    verwalter.get(BesetztModulAdresse.H1).fahrstrasse = True
    verwalter.get(BesetztModulAdresse.H2).fahrstrasse = True
    verwalter.get(BesetztModulAdresse.H3).fahrstrasse = True

    ZugController().update_zug_position(zug, gegeben_fahrstrecke(), verwalter)
    assert verwalter.get(BesetztModulAdresse.H1).fahrstrasse is True
    assert verwalter.get(BesetztModulAdresse.H2).fahrstrasse is True
    assert verwalter.get(BesetztModulAdresse.H3).fahrstrasse is True
