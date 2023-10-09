from src.controller.FahrstrasseController import FahrstrasseController
from src.model.BesetztModul import BesetztModul, BesetztModulVerwalter
from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.model.Gleisbelegung import Gleisbelegung
from src.model.weiche.Weiche import Weiche
from src.model.weiche.Weichenadresse import Weichenadresse
from src.model.weiche.Weichenstellung import Weichenstellung
from src.model.zug.Fahrstrecke import Fahrstrecke


def test_fahrstrasse_stellen():
    fahrstrecke, verwalter = gegeben_fahrstrecke_mit_2_modulen()
    assert True is FahrstrasseController.stelle_fahrstrasse(fahrstrecke, verwalter)
    assert Gleisbelegung.FAHRSTRASSE == verwalter.get(BesetztModulAdresse.B001_HAUPT_AUSFAHRT_LINKS).gleisbelegung()
    assert Gleisbelegung.FAHRSTRASSE == verwalter.get(BesetztModulAdresse.B011_HAUPT_G1_HALTE_LINKS).gleisbelegung()


def test_fahrstrasse_stellen_nicht_wenn_fahrstrasse_geschnitten_wird():
    fahrstrecke, verwalter = gegeben_fahrstrecke_mit_2_modulen()
    verwalter.get(BesetztModulAdresse.B011_HAUPT_G1_HALTE_LINKS).fahrstrasse = True
    assert False is FahrstrasseController.stelle_fahrstrasse(fahrstrecke, verwalter)
    assert Gleisbelegung.FREI == verwalter.get(BesetztModulAdresse.B001_HAUPT_AUSFAHRT_LINKS).gleisbelegung()
    assert Gleisbelegung.FAHRSTRASSE == verwalter.get(BesetztModulAdresse.B011_HAUPT_G1_HALTE_LINKS).gleisbelegung()


def test_fahrstrasse_stellen_mit_weiche():
    besetzt_modul: BesetztModul = BesetztModul(BesetztModulAdresse.B001_HAUPT_AUSFAHRT_LINKS)
    weiche: Weiche = Weiche(Weichenadresse.W1, besetzt_modul)
    fahrstrecke: Fahrstrecke = Fahrstrecke()
    fahrstrecke.besetzt_module = [BesetztModulAdresse.B001_HAUPT_AUSFAHRT_LINKS]
    assert True is FahrstrasseController.stelle_fahrstrasse(fahrstrecke, BesetztModulVerwalter({besetzt_modul}))
    assert Gleisbelegung.FAHRSTRASSE == weiche.gleisbelegung()


def gegeben_fahrstrecke_mit_2_modulen():
    fahrstrecke: Fahrstrecke = Fahrstrecke()
    fahrstrecke.besetzt_module = [BesetztModulAdresse.B001_HAUPT_AUSFAHRT_LINKS,
                                  BesetztModulAdresse.B011_HAUPT_G1_HALTE_LINKS]

    return fahrstrecke, BesetztModulVerwalter({(BesetztModul(BesetztModulAdresse.B001_HAUPT_AUSFAHRT_LINKS)),
                                               (BesetztModul(BesetztModulAdresse.B011_HAUPT_G1_HALTE_LINKS))})


def test_fahrstrasse_weiche_stellen():
    fahrstrecke, verwalter = gegeben_fahrstrecke_mit_2_modulen()

    weiche: Weiche = Weiche(Weichenadresse.W1, verwalter.get(BesetztModulAdresse.B001_HAUPT_AUSFAHRT_LINKS))
    weiche.weichenstellung = Weichenstellung.GERADE
    fahrstrecke.weichenstellungen = {weiche: Weichenstellung.ABZWEIGEND}

    FahrstrasseController.stelle_fahrstrasse(fahrstrecke, verwalter)
    assert Weichenstellung.ABZWEIGEND == weiche.weichenstellung


def test_fahrstrasse_weiche_stellen_nicht_wenn_fahrstrasse():
    fahrstrecke, verwalter = gegeben_fahrstrecke_mit_2_modulen()
    verwalter.get(BesetztModulAdresse.B001_HAUPT_AUSFAHRT_LINKS).fahrstrasse = True

    weiche: Weiche = Weiche(Weichenadresse.W1, verwalter.get(BesetztModulAdresse.B001_HAUPT_AUSFAHRT_LINKS))
    weiche.weichenstellung = Weichenstellung.GERADE
    fahrstrecke.weichenstellungen = {weiche: Weichenstellung.ABZWEIGEND}

    FahrstrasseController.stelle_fahrstrasse(fahrstrecke, verwalter)
    assert weiche.weichenstellung == Weichenstellung.GERADE


def test_fahrstrasse_mehrere_weichen_in_einem_besetztmodul():
    fahrstrecke, weiche1, weiche2, verwalter = gegeben_fahrstreck_2_weichen()

    FahrstrasseController.stelle_fahrstrasse(fahrstrecke, verwalter)
    assert Gleisbelegung.FAHRSTRASSE == weiche1.gleisbelegung()
    assert Gleisbelegung.FAHRSTRASSE == weiche2.gleisbelegung()


def test_fahrstrasse_keine_fahrstrasse_wenn_weiche_gesperrt():
    fahrstrecke, weiche1, weiche2, verwalter = gegeben_fahrstreck_2_weichen()
    weiche1.gesperrt = True

    FahrstrasseController.stelle_fahrstrasse(fahrstrecke, verwalter)
    assert Gleisbelegung.GESPRERRT == weiche1.gleisbelegung()
    assert Gleisbelegung.FREI == weiche2.gleisbelegung()


def gegeben_fahrstreck_2_weichen():
    fahrstrecke: Fahrstrecke = Fahrstrecke()
    besetztmodul: BesetztModul = BesetztModul(BesetztModulAdresse.B001_HAUPT_AUSFAHRT_LINKS)
    fahrstrecke.besetzt_module.append(BesetztModulAdresse.B001_HAUPT_AUSFAHRT_LINKS)

    weiche1: Weiche = Weiche(Weichenadresse.W1, besetztmodul)
    weiche2: Weiche = Weiche(Weichenadresse.W2, besetztmodul)

    fahrstrecke.weichenstellungen = {weiche1: Weichenstellung.GERADE,
                                     weiche2: Weichenstellung.ABZWEIGEND}
    return fahrstrecke, weiche1, weiche2, BesetztModulVerwalter({besetztmodul})


def test_fahrstrasse_keine_fahrstrasse_wenn_besetzt():
    fahrstrecke, verwalter = gegeben_fahrstrecke_mit_2_modulen()
    verwalter.get(BesetztModulAdresse.B001_HAUPT_AUSFAHRT_LINKS).besetzt = True

    assert False is FahrstrasseController.stelle_fahrstrasse(fahrstrecke, verwalter)
    assert Gleisbelegung.BESETZT == verwalter.get(BesetztModulAdresse.B001_HAUPT_AUSFAHRT_LINKS).gleisbelegung()
    assert Gleisbelegung.FREI == verwalter.get(BesetztModulAdresse.B011_HAUPT_G1_HALTE_LINKS).gleisbelegung()
    assert not verwalter.get(BesetztModulAdresse.B001_HAUPT_AUSFAHRT_LINKS).fahrstrasse
    assert not verwalter.get(BesetztModulAdresse.B011_HAUPT_G1_HALTE_LINKS).fahrstrasse


# Test Toggle
def test_toggle_gleisbelegung_frei_zu_fahrstrasse():
    besetzt_modul = BesetztModul(BesetztModulAdresse.B001_HAUPT_AUSFAHRT_LINKS)
    besetzt_modul.fahrstrasse = False
    weiche = Weiche(Weichenadresse.W2, besetzt_modul)
    FahrstrasseController().toggle_fahrstrasse(weiche)
    assert Gleisbelegung.FAHRSTRASSE == weiche.gleisbelegung()


def test_toggle_gleisbelegung_fahrstrasse_zu_frei():
    besetzt_modul = BesetztModul(BesetztModulAdresse.B001_HAUPT_AUSFAHRT_LINKS)
    besetzt_modul.fahrstrasse = True
    weiche = Weiche(Weichenadresse.W2, besetzt_modul)
    FahrstrasseController().toggle_fahrstrasse(weiche)
    assert Gleisbelegung.FREI == weiche.gleisbelegung()
