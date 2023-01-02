from unittest.mock import *

from src.serial.WeichenControlBote import WeichenControlBote
from src.model.weiche.Weichenstellung import Weichenstellung
from src.model.weiche.Weichenadresse import Weichenadresse

@patch('src.serial.WeichenControlBote.weichen_control')
def test_aendere_weichenstellung__ruft_serial_gerade(weichen_control):
    WeichenControlBote().aendere_weichenstellung(Weichenadresse.W1, Weichenstellung.GERADE)
    weichen_control.turnout_set_for_route.assert_called_with(ANY, ANY, True)


@patch('src.serial.WeichenControlBote.weichen_control')
def test_aendere_weichenstellung__ruft_serial_abzweigend(weichen_control):
    WeichenControlBote().aendere_weichenstellung(Weichenadresse.W1, Weichenstellung.ABZWEIGEND)
    weichen_control.turnout_set_for_route.assert_called_with(ANY, ANY, False)



@patch('src.serial.WeichenControlBote.weichen_control')
def test_aendere_weichenstellung__W1_ruft_Adresse1(weichen_control):
    WeichenControlBote().aendere_weichenstellung(Weichenadresse.W1, Weichenstellung.GERADE)
    weichen_control.turnout_set_for_route.assert_called_with(b'\12', b'\00', ANY)

@patch('src.serial.WeichenControlBote.weichen_control')
def test_aendere_weichenstellung__W2_ruft_Adresse2(weichen_control):
    WeichenControlBote().aendere_weichenstellung(Weichenadresse.W2, Weichenstellung.GERADE)
    weichen_control.turnout_set_for_route.assert_called_with(b'\14', b'\00', ANY)