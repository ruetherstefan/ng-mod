from unittest.mock import *

from src.controller.WeichenstellungController import WeichenstellungController
from src.model.BesetztModul import BesetztModul
from src.model.Weiche import Weiche
from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.model.Weichenadresse import Weichenadresse
from src.model.Weichenstellung import Weichenstellung


@patch('src.controller.WeichenstellungController.WeichenControlBote')
def test_aendere_weichenstellung_weicheadresse_weitergabe(weichen_control_bote_mock):
    weiche = Weiche(Weichenadresse.W1, BesetztModul(BesetztModulAdresse.H1))
    WeichenstellungController().aendere_weichenstellung(weiche)
    weichen_control_bote_mock().aendere_weichenstellung.assert_called_with(Weichenadresse.W1, ANY)


@patch('src.controller.WeichenstellungController.WeichenControlBote')
def test_aendere_weichenstellung_gerade_zu_abzweigend(weichen_control_bote_mock):
    weiche = Weiche(Weichenadresse.W1, BesetztModul(BesetztModulAdresse.H1))
    weiche.weichenstellung = Weichenstellung.GERADE
    WeichenstellungController().aendere_weichenstellung(weiche)
    assert Weichenstellung.ABZWEIGEND == weiche.weichenstellung
    weichen_control_bote_mock().aendere_weichenstellung.assert_called_with(ANY, Weichenstellung.ABZWEIGEND)


@patch('src.controller.WeichenstellungController.WeichenControlBote')
def test_aendere_weichenstellung_abzweigend_zu_gerade(weichen_control_bote_mock):
    weiche = Weiche(Weichenadresse.W1, BesetztModul(BesetztModulAdresse.H1))
    weiche.weichenstellung = Weichenstellung.ABZWEIGEND
    WeichenstellungController().aendere_weichenstellung(weiche)
    assert Weichenstellung.GERADE == weiche.weichenstellung
    weichen_control_bote_mock().aendere_weichenstellung.assert_called_with(ANY, Weichenstellung.GERADE)


