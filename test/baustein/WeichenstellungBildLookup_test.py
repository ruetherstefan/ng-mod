from unittest.mock import *

from src.view.WeichenstellungBildLookup import *
from src.model.Gleisbelegung import Gleisbelegung
from src.view.Baustein import Baustein


@patch('src.baustein.WeichenstellungBildLookup.Bilder')
def test_lookupFrei(bilder_mock):
    WeichenstellungBildLookup.lookup(Markierungsart.RECHTS_MITTE, Gleisbelegung.FREI)
    bilder_mock().get_image.assert_called_with(Baustein.bilder_ordner + "Markierungen/WeicheRechtsMitte.png")

@patch('src.baustein.WeichenstellungBildLookup.Bilder')
def test_lookupFrei_andereMarkierungsant(bilder_mock):
    WeichenstellungBildLookup.lookup(Markierungsart.RECHTS_UNTEN, Gleisbelegung.FREI)
    bilder_mock().get_image.assert_called_with(Baustein.bilder_ordner + "Markierungen/WeicheRechtsUnten.png")

@patch('src.baustein.WeichenstellungBildLookup.Bilder')
def test_lookupFrei_weichenbelegung(bilder_mock):
    WeichenstellungBildLookup.lookup(Markierungsart.RECHTS_UNTEN, Gleisbelegung.FAHRSTRASSE)
    bilder_mock().get_image.assert_called_with(Baustein.bilder_ordner + "Markierungen/FahrstrasseWeicheRechtsUnten.png")
