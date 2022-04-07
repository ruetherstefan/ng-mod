from unittest.mock import *

from src.controller.GleisbelegungController import GleisbelegungController
from src.model.Gleisbelegung import Gleisbelegung
from src.model.Weiche import Weiche
from src.model.Weichenadresse import Weichenadresse
from src.model.Weichenstellung import Weichenstellung


def test_toggle_gleisbelegung_frei_zu_fahrstrasse():
    weiche = Weiche(Weichenadresse.W2)
    weiche.gleisbelegung = Gleisbelegung.FREI
    GleisbelegungController().toggle_fahrstrasse(weiche)
    assert Gleisbelegung.FAHRSTRASSE == weiche.gleisbelegung


def test_toggle_gleisbelegung_fahrstrasse_zu_frei():
    weiche = Weiche(Weichenadresse.W2)
    weiche.gleisbelegung = Gleisbelegung.FAHRSTRASSE
    GleisbelegungController().toggle_fahrstrasse(weiche)
    assert Gleisbelegung.FREI == weiche.gleisbelegung