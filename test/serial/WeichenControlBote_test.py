from unittest.mock import *

from src.model.weiche.Weichenadresse import Weichenadresse
from src.model.weiche.Weichenstellung import Weichenstellung
from src.serial.WeichenControlBote import WeichenControlBote


def test_mock_wenn_offline():
    assert isinstance(WeichenControlBote().weichen_control, Mock)


def test_aendere_weichenstellung__ruft_serial_gerade():
    bote = WeichenControlBote()
    bote.aendere_weichenstellung(Weichenadresse.W1, Weichenstellung.GERADE)
    bote.weichen_control.turnout_set_for_route.assert_called_with(ANY, ANY, True)


def test_aendere_weichenstellung__ruft_serial_abzweigend():
    bote = WeichenControlBote()
    bote.aendere_weichenstellung(Weichenadresse.W1, Weichenstellung.ABZWEIGEND)
    bote.weichen_control.turnout_set_for_route.assert_called_with(ANY, ANY, False)


def test_aendere_weichenstellung__w1_ruft_adresse1():
    bote = WeichenControlBote()
    bote.aendere_weichenstellung(Weichenadresse.W1, Weichenstellung.GERADE)
    bote.weichen_control.turnout_set_for_route.assert_called_with(b'\12', b'\00', ANY)


def test_aendere_weichenstellung__w2_ruft_adresse2():
    bote = WeichenControlBote()
    bote.aendere_weichenstellung(Weichenadresse.W2, Weichenstellung.GERADE)
    bote.weichen_control.turnout_set_for_route.assert_called_with(b'\14', b'\00', ANY)
