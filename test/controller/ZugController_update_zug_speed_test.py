from src.model.BesetztModul import BesetztModul
from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.model.zug.Fahrstrecke import Fahrstrecke
from src.model.zug.Lok import Lok
from src.model.zug.Zug import Zug
from src.controller.ZugController import ZugController
from src.model.zug.SpeedModifier import SpeedModifier


def gegeben_zug_mit_anfang(besetzt_modul):
    zug: Zug = Zug()
    zug.anfang = besetzt_modul
    zug.lok = Lok(42)
    return zug


def gegeben_fahrstrecke_mit_einem_modul():
    besetzt_modul: BesetztModul = BesetztModul(BesetztModulAdresse.H1)
    fahrstrecke: Fahrstrecke = Fahrstrecke()
    fahrstrecke.besetzt_module = [besetzt_modul]
    return besetzt_modul, fahrstrecke


def test_update_zug_speed_strecke_gerade():
    besetzt_modul, fahrstrecke = gegeben_fahrstrecke_mit_einem_modul()
    zug = gegeben_zug_mit_anfang(besetzt_modul)

    fahrstrecke.speed_modifier = {}
    zug.speeds = {SpeedModifier.STRECKE_GERADE: 10}

    ZugController().update_zug_speed(zug, fahrstrecke)
    assert zug.lok.speed == zug.speeds[SpeedModifier.STRECKE_GERADE]


def test_update_zug_speed_strecke_abwaerts():
    besetzt_modul, fahrstrecke = gegeben_fahrstrecke_mit_einem_modul()
    zug = gegeben_zug_mit_anfang(besetzt_modul)

    fahrstrecke.speed_modifier = {besetzt_modul: SpeedModifier.STRECKE_ABWAERTS}
    zug.speeds = {SpeedModifier.STRECKE_ABWAERTS: 7,
                  SpeedModifier.STRECKE_AUFWAERTS: 15}

    ZugController().update_zug_speed(zug, fahrstrecke)
    assert zug.lok.speed == zug.speeds[SpeedModifier.STRECKE_ABWAERTS]


def test_update_zug_speed_strecke_aufwaerts():
    besetzt_modul, fahrstrecke = gegeben_fahrstrecke_mit_einem_modul()
    zug = gegeben_zug_mit_anfang(besetzt_modul)

    fahrstrecke.speed_modifier = {besetzt_modul: SpeedModifier.STRECKE_AUFWAERTS}
    zug.speeds = {SpeedModifier.STRECKE_ABWAERTS: 7,
                  SpeedModifier.STRECKE_AUFWAERTS: 15}

    ZugController().update_zug_speed(zug, fahrstrecke)
    assert zug.lok.speed == zug.speeds[SpeedModifier.STRECKE_AUFWAERTS]


def test_update_zug_speed_bahnhof_stop():
    besetzt_modul, fahrstrecke = gegeben_fahrstrecke_mit_einem_modul()
    zug = gegeben_zug_mit_anfang(besetzt_modul)

    fahrstrecke.speed_modifier = {besetzt_modul: SpeedModifier.BAHNHOF_STOP}
    zug.speeds = {}

    ZugController().update_zug_speed(zug, fahrstrecke)
    assert zug.lok.speed == 0

