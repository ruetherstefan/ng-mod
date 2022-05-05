from src.model.Lok import Lok
from src.serial.LokControl import LokControl


def test_get_low_byte_adresse_1():
    assert LokControl().get_adresse_low_byte(1) == 1


def test_get_low_byte_adresse_2():
    assert LokControl().get_adresse_low_byte(2) == 2


def test_get_low_byte_adresse_256():
    assert LokControl().get_adresse_low_byte(256) == 0


def test_get_high_byte_adresse_1():
    assert LokControl().get_adresse_high_byte(1) == 0


def test_get_high_byte_adresse_256():
    assert LokControl().get_adresse_high_byte(256) == 1


def test_get_byte_funktionen_default_nur6und7gesetzt():
    assert LokControl().get_byte_funktionen(Lok(1)) & 0xC0 == 0xC0


def test_get_byte_funktionen_forwaerts_5gesetzt():
    lok = Lok(1)
    lok.forwaerts = True
    assert LokControl().get_byte_funktionen(lok) & 0x20 == 0x20

def test_get_byte_funktionen_rueckwaerts_5nichtgesetzt():
    lok = Lok(1)
    lok.forwaerts = False
    assert LokControl().get_byte_funktionen(lok) & 0x20 == 0



def test_get_byte_funktionen_frontlicht_4gesetzt():
    lok = Lok(1)
    lok.frontlicht = True
    assert LokControl().get_byte_funktionen(lok) & 0x10 == 0x10

def test_get_byte_funktionen_frontlicht_4nichtgesetzt():
    lok = Lok(1)
    lok.frontlicht = False
    assert LokControl().get_byte_funktionen(lok) & 0x10 == 0



def test_get_byte_funktionen_F4_3gesetzt():
    lok = Lok(1)
    lok.f4 = True
    assert LokControl().get_byte_funktionen(lok) & 0x08 == 0x08

def test_get_byte_funktionen_F4_3nichtgesetzt():
    lok = Lok(1)
    lok.f4 = False
    assert LokControl().get_byte_funktionen(lok) & 0x08 == 0



def test_get_byte_funktionen_F3_2gesetzt():
    lok = Lok(1)
    lok.f3 = True
    assert LokControl().get_byte_funktionen(lok) & 0x04 == 0x04

def test_get_byte_funktionen_F3_2nichtgesetzt():
    lok = Lok(1)
    lok.f3 = False
    assert LokControl().get_byte_funktionen(lok) & 0x04 == 0


def test_get_byte_funktionen_F2_1gesetzt():
    lok = Lok(1)
    lok.f2 = True
    assert LokControl().get_byte_funktionen(lok) & 0x02 == 0x02

def test_get_byte_funktionen_F2_1nichtgesetzt():
    lok = Lok(1)
    lok.f2 = False
    assert LokControl().get_byte_funktionen(lok) & 0x02 == 0


def test_get_byte_funktionen_F1_0gesetzt():
    lok = Lok(1)
    lok.f1 = True
    assert LokControl().get_byte_funktionen(lok) & 0x01 == 0x01

def test_get_byte_funktionen_F1_0nichtgesetzt():
    lok = Lok(1)
    lok.f1 = False
    assert LokControl().get_byte_funktionen(lok) & 0x01 == 0
