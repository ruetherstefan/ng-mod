from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.model.Gleisbelegung import Gleisbelegung
from src.model.BesetztModul import BesetztModul
from src.model.weiche.Weiche import Weiche
from src.model.weiche.Weichenadresse import Weichenadresse
from src.model.weiche.Weichenstellung import Weichenstellung
from src.controller.FahrstrasseController import FahrstrasseController
from src.model.zug.Fahrstrecke import Fahrstrecke


def test_fahrstrasse_stellen():
    fahrstrecke, besetztmodul1, besetztmodul2 = gegeben_fahrstrecke_mit_2_modulen()
    assert True is FahrstrasseController().stelle_fahrstrasse(fahrstrecke)
    assert Gleisbelegung.FAHRSTRASSE == besetztmodul1.gleisbelegung()
    assert Gleisbelegung.FAHRSTRASSE == besetztmodul2.gleisbelegung()


def test_fahrstrasse_stellen_nicht_wenn_fahrstrasse_geschnitten_wird():
    fahrstrecke, besetztmodul1, besetztmodul2 = gegeben_fahrstrecke_mit_2_modulen()
    besetztmodul2.fahrstrasse = True
    assert False is FahrstrasseController().stelle_fahrstrasse(fahrstrecke)
    assert Gleisbelegung.FREI == besetztmodul1.gleisbelegung()
    assert Gleisbelegung.FAHRSTRASSE == besetztmodul2.gleisbelegung()


def test_fahrstrasse_stellen_mit_weiche():
    besetzt_modul: BesetztModul = BesetztModul(BesetztModulAdresse.H1)
    weiche: Weiche = Weiche(Weichenadresse.W1, besetzt_modul)
    fahrstrecke: Fahrstrecke = Fahrstrecke()
    fahrstrecke.besetzt_module = [besetzt_modul]
    assert True is FahrstrasseController().stelle_fahrstrasse(fahrstrecke)
    assert Gleisbelegung.FAHRSTRASSE == weiche.gleisbelegung()


def gegeben_fahrstrecke_mit_2_modulen():
    besetztmodul1: BesetztModul = BesetztModul(BesetztModulAdresse.H1)
    besetztmodul2: BesetztModul = BesetztModul(BesetztModulAdresse.H2)
    fahrstrecke: Fahrstrecke = Fahrstrecke()
    fahrstrecke.besetzt_module = [besetztmodul1, besetztmodul2]
    return fahrstrecke, besetztmodul1, besetztmodul2


def test_fahrstrasse_weiche_stellen():
    fahrstrecke, besetztmodul1, besetztmodul2 = gegeben_fahrstrecke_mit_2_modulen()

    weiche: Weiche = Weiche(Weichenadresse.W1, besetztmodul1)
    weiche.weichenstellung = Weichenstellung.GERADE
    fahrstrecke.weichenstellungen = {weiche: Weichenstellung.ABZWEIGEND}

    FahrstrasseController().stelle_fahrstrasse(fahrstrecke)
    assert Weichenstellung.ABZWEIGEND == weiche.weichenstellung


def test_fahrstrasse_weiche_stellen_nicht_wenn_fahrstrasse():
    fahrstrecke, besetztmodul1, besetztmodul2 = gegeben_fahrstrecke_mit_2_modulen()
    besetztmodul1.fahrstrasse = True

    weiche: Weiche = Weiche(Weichenadresse.W1, besetztmodul1)
    weiche.weichenstellung = Weichenstellung.GERADE
    fahrstrecke.weichenstellungen = {weiche: Weichenstellung.ABZWEIGEND}

    FahrstrasseController().stelle_fahrstrasse(fahrstrecke)
    assert weiche.weichenstellung == Weichenstellung.GERADE


def test_fahrstrasse_mehrere_weichen_in_einem_besetztmodul():
    fahrstrecke, weiche1, weiche2 = gegeben_fahrstreck_2_weichen()

    FahrstrasseController().stelle_fahrstrasse(fahrstrecke)
    assert Gleisbelegung.FAHRSTRASSE == weiche1.gleisbelegung()
    assert Gleisbelegung.FAHRSTRASSE == weiche2.gleisbelegung()


def test_fahrstrasse_keine_fahrstrasse_wenn_weiche_gesperrt():
    fahrstrecke, weiche1, weiche2 = gegeben_fahrstreck_2_weichen()
    weiche1.gesperrt = True

    FahrstrasseController().stelle_fahrstrasse(fahrstrecke)
    assert Gleisbelegung.GESPRERRT == weiche1.gleisbelegung()
    assert Gleisbelegung.FREI == weiche2.gleisbelegung()


def gegeben_fahrstreck_2_weichen():
    fahrstrecke: Fahrstrecke = Fahrstrecke()
    besetztmodul: BesetztModul = BesetztModul(BesetztModulAdresse.H1)
    fahrstrecke.besetzt_module.append(besetztmodul)

    weiche1: Weiche = Weiche(Weichenadresse.W1, besetztmodul)
    weiche2: Weiche = Weiche(Weichenadresse.W2, besetztmodul)

    fahrstrecke.weichenstellungen = {weiche1: Weichenstellung.GERADE,
                                     weiche2: Weichenstellung.ABZWEIGEND}
    return fahrstrecke, weiche1, weiche2


def test_fahrstrasse_keine_fahrstrasse_wenn_besetzt():
    fahrstrecke, besetztmodul1, besetztmodul2 = gegeben_fahrstrecke_mit_2_modulen()
    besetztmodul1.besetzt = True

    assert False is FahrstrasseController().stelle_fahrstrasse(fahrstrecke)
    assert Gleisbelegung.FREI == besetztmodul1.gleisbelegung()
    assert Gleisbelegung.FREI == besetztmodul2.gleisbelegung()


# Test Toggle
def test_toggle_gleisbelegung_frei_zu_fahrstrasse():
    besetzt_modul = BesetztModul(BesetztModulAdresse.H1)
    besetzt_modul.fahrstrasse = False
    weiche = Weiche(Weichenadresse.W2, besetzt_modul)
    FahrstrasseController().toggle_fahrstrasse(weiche)
    assert Gleisbelegung.FAHRSTRASSE == weiche.gleisbelegung()


def test_toggle_gleisbelegung_fahrstrasse_zu_frei():
    besetzt_modul = BesetztModul(BesetztModulAdresse.H1)
    besetzt_modul.fahrstrasse = True
    weiche = Weiche(Weichenadresse.W2, besetzt_modul)
    FahrstrasseController().toggle_fahrstrasse(weiche)
    assert Gleisbelegung.FREI == weiche.gleisbelegung()

