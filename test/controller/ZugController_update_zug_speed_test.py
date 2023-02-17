from src.controller.ZugController import ZugController
from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.model.zug.Fahrstrecke import Fahrstrecke
from src.model.zug.Lok import Lok
from src.model.zug.SpeedModifier import SpeedModifier
from src.model.zug.Zug import Zug


def gegeben_zug_mit_anfang_und_ende(anfang, ende) -> Zug:
    zug: Zug = Zug()
    zug.anfang = anfang
    zug.ende = ende
    zug.lok = Lok(42)
    return zug


def gegeben_fahrstrecke_mit_einem_modul() -> Fahrstrecke:
    fahrstrecke: Fahrstrecke = Fahrstrecke()
    fahrstrecke.besetzt_module = [BesetztModulAdresse.H1]
    return fahrstrecke


def gegeben_fahrstrecke_mit_zwei_modulen() -> Fahrstrecke:
    fahrstrecke: Fahrstrecke = gegeben_fahrstrecke_mit_einem_modul()
    fahrstrecke.besetzt_module.append(BesetztModulAdresse.H2)
    return fahrstrecke


def test_update_zug_speed_strecke_gerade():
    fahrstrecke = gegeben_fahrstrecke_mit_einem_modul()
    zug = gegeben_zug_mit_anfang_und_ende(BesetztModulAdresse.H1, BesetztModulAdresse.H1)

    fahrstrecke.speed_modifier = {}
    zug.speeds = {SpeedModifier.STRECKE_GERADE: 10}

    ZugController().update_zug_speed(zug, fahrstrecke)
    assert zug.lok.speed == zug.speeds[SpeedModifier.STRECKE_GERADE]


def test_update_zug_speed_strecke_abwaerts():
    fahrstrecke = gegeben_fahrstrecke_mit_einem_modul()
    zug = gegeben_zug_mit_anfang_und_ende(BesetztModulAdresse.H1, BesetztModulAdresse.H1)

    fahrstrecke.speed_modifier = {BesetztModulAdresse.H1: SpeedModifier.STRECKE_ABWAERTS}
    zug.speeds = {SpeedModifier.STRECKE_ABWAERTS: 7,
                  SpeedModifier.STRECKE_AUFWAERTS: 15}

    ZugController().update_zug_speed(zug, fahrstrecke)
    assert zug.lok.speed == zug.speeds[SpeedModifier.STRECKE_ABWAERTS]


def test_update_zug_speed_strecke_aufwaerts():
    fahrstrecke = gegeben_fahrstrecke_mit_einem_modul()
    zug = gegeben_zug_mit_anfang_und_ende(BesetztModulAdresse.H1, BesetztModulAdresse.H1)

    fahrstrecke.speed_modifier = {BesetztModulAdresse.H1: SpeedModifier.STRECKE_AUFWAERTS}
    zug.speeds = {SpeedModifier.STRECKE_ABWAERTS: 7,
                  SpeedModifier.STRECKE_AUFWAERTS: 15}

    ZugController().update_zug_speed(zug, fahrstrecke)
    assert zug.lok.speed == zug.speeds[SpeedModifier.STRECKE_AUFWAERTS]


def test_update_zug_speed_bahnhof_stop():
    fahrstrecke = gegeben_fahrstrecke_mit_einem_modul()
    zug = gegeben_zug_mit_anfang_und_ende(BesetztModulAdresse.H1, BesetztModulAdresse.H1)

    fahrstrecke.speed_modifier = {BesetztModulAdresse.H1: SpeedModifier.BAHNHOF_STOP}
    zug.speeds = {}

    ZugController().update_zug_speed(zug, fahrstrecke)
    assert zug.lok.speed == 0


def test_update_zug_speed_min_von_anfang_und_ende__anfang_kleiner():
    fahrstrecke = gegeben_fahrstrecke_mit_zwei_modulen()
    zug = gegeben_zug_mit_anfang_und_ende(BesetztModulAdresse.H1, BesetztModulAdresse.H2)

    fahrstrecke.speed_modifier = {BesetztModulAdresse.H1: SpeedModifier.STRECKE_ABWAERTS,
                                  BesetztModulAdresse.H2: SpeedModifier.STRECKE_AUFWAERTS}
    zug.speeds = {SpeedModifier.STRECKE_ABWAERTS: 7,
                  SpeedModifier.STRECKE_AUFWAERTS: 15}

    ZugController().update_zug_speed(zug, fahrstrecke)
    assert zug.lok.speed == zug.speeds[SpeedModifier.STRECKE_ABWAERTS]


def test_update_zug_speed_min_von_anfang_und_ende__ende_kleiner():
    fahrstrecke = gegeben_fahrstrecke_mit_zwei_modulen()
    zug = gegeben_zug_mit_anfang_und_ende(BesetztModulAdresse.H1, BesetztModulAdresse.H2)

    fahrstrecke.speed_modifier = {BesetztModulAdresse.H1: SpeedModifier.STRECKE_ABWAERTS,
                                  BesetztModulAdresse.H2: SpeedModifier.STRECKE_AUFWAERTS}
    zug.speeds = {SpeedModifier.STRECKE_ABWAERTS: 15,
                  SpeedModifier.STRECKE_AUFWAERTS: 7}

    ZugController().update_zug_speed(zug, fahrstrecke)
    assert zug.lok.speed == zug.speeds[SpeedModifier.STRECKE_AUFWAERTS]
