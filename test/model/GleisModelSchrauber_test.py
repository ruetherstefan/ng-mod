from enum import Enum

import pytest

from src.model.Gleisbelegung import Gleisbelegung


class Gleis:
    def __init__(self, gleisadresse):
        self.adresse = gleisadresse
        self.gleisbelegung = Gleisbelegung.FREI

        self.seiteA = None
        self.seiteB = None


class Gleisadresse(Enum):
    H1 = 1
    H2 = 2
    H3 = 3
    H4 = 4
    H5 = 5
    H6 = 6


class GleisModelSchrauber:
    def verbindeGleise(self, gleis1, gleis2):
        if gleis1.seiteB is None:
            gleis1.seiteB = gleis2
            gleis2.seiteA = gleis1
        elif gleis1.seiteA is None:
            gleis1.seiteA = gleis2
            gleis2.seiteB = gleis1
        else:
            raise Exception("KonfigurationException: Gleis kann nur 2 mal verbunden werden")


def test_Gleisschrauber_gleiseVerbindenZuerstWirdBmitAVerbunden():
    gleis1 = Gleis(Gleisadresse.H1)
    gleis2 = Gleis(Gleisadresse.H2)
    GleisModelSchrauber().verbindeGleise(gleis1, gleis2)
    assert gleis1.seiteB == gleis2
    assert gleis2.seiteA == gleis1


def test_Gleisschrauber_gleiseVerbinden_AlsZweitesAmitB():
    gleis1 = Gleis(Gleisadresse.H1)
    gleis2 = Gleis(Gleisadresse.H2)
    gleis3 = Gleis(Gleisadresse.H3)
    GleisModelSchrauber().verbindeGleise(gleis2, gleis3)
    GleisModelSchrauber().verbindeGleise(gleis2, gleis1)
    assert gleis2.seiteA == gleis1
    assert gleis2.seiteB == gleis3



def test_Gleisschrauber_gleiseVerbinden_DrittesVerbindenException():
    gleis1 = Gleis(Gleisadresse.H1)
    gleis2 = Gleis(Gleisadresse.H2)
    gleis3 = Gleis(Gleisadresse.H3)
    gleis4 = Gleis(Gleisadresse.H4)
    GleisModelSchrauber().verbindeGleise(gleis2, gleis3)
    GleisModelSchrauber().verbindeGleise(gleis2, gleis1)
    with pytest.raises(Exception):
        GleisModelSchrauber().verbindeGleise(gleis2, gleis4)
