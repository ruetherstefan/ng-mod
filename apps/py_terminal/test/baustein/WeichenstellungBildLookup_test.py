from unittest.mock import *

from src.baustein.WeichenstellungBildLookup import *
from src.baustein.Weichenbelegung import Weichenbelegung
from src.baustein.Baustein import Baustein


@patch('src.baustein.WeichenstellungBildLookup.Bilder')
def test_lookupFrei(bilder_mock):
    WeichenstellungBildLookup.lookup(Markierungsart.RECHTS_MITTE, Weichenbelegung.FREI)
    bilder_mock().get_image.assert_called_with(Baustein.bilder_ordner + "Markierungen/WeicheRechtsMitte.png")

@patch('src.baustein.WeichenstellungBildLookup.Bilder')
def test_lookupFrei_andereMarkierungsant(bilder_mock):
    WeichenstellungBildLookup.lookup(Markierungsart.RECHTS_UNTEN, Weichenbelegung.FREI)
    bilder_mock().get_image.assert_called_with(Baustein.bilder_ordner + "Markierungen/WeicheRechtsUnten.png")

@patch('src.baustein.WeichenstellungBildLookup.Bilder')
def test_lookupFrei_weichenbelegung(bilder_mock):
    WeichenstellungBildLookup.lookup(Markierungsart.RECHTS_UNTEN, Weichenbelegung.FAHRSTRASSE)
    bilder_mock().get_image.assert_called_with(Baustein.bilder_ordner + "Markierungen/FahrstrasseWeicheRechtsUnten.png")
