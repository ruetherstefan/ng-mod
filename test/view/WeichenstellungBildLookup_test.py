from unittest.mock import *

from src.view.WeichenstellungBildLookup import *
from src.model.Gleisbelegung import Gleisbelegung
from src.view.BausteinView import BausteinView


@patch('src.view.WeichenstellungBildLookup.Bilder')
def test_lookupFrei(bilder_mock):
    WeichenstellungBildLookup.lookup(Markierungsart.RECHTS_MITTE, Gleisbelegung.FREI)
    bilder_mock().get_image.assert_called_with("Markierungen/WeicheRechtsMitte.png")


@patch('src.view.WeichenstellungBildLookup.Bilder')
def test_lookupFrei_andereMarkierungsant(bilder_mock):
    WeichenstellungBildLookup.lookup(Markierungsart.RECHTS_UNTEN, Gleisbelegung.FREI)
    bilder_mock().get_image.assert_called_with("Markierungen/WeicheRechtsUnten.png")


@patch('src.view.WeichenstellungBildLookup.Bilder')
def test_lookupFrei_weichenbelegung(bilder_mock):
    WeichenstellungBildLookup.lookup(Markierungsart.RECHTS_UNTEN, Gleisbelegung.FAHRSTRASSE)
    bilder_mock().get_image.assert_called_with("Markierungen/FahrstrasseWeicheRechtsUnten.png")
