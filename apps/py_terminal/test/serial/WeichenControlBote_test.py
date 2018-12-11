from unittest.mock import *

from src.serial.WeichenControlBote import WeichenControlBote
from src.baustein.Weichenstellung import Weichenstellung


@patch('src.serial.WeichenControlBote.weichen_control')
def test_aendere_weichenstellung__ruft_serial_gerade(weichen_control):
    WeichenControlBote().aendere_weichenstellung("weichenname", Weichenstellung.GERADE)
    weichen_control.turnout_set_for_route.assert_called_with(b'\01', b'\00', True)


@patch('src.serial.WeichenControlBote.weichen_control')
def test_aendere_weichenstellung__ruft_serial_abzweigend(weichen_control):
    WeichenControlBote().aendere_weichenstellung("weichenname", Weichenstellung.ABZWEIGEND)
    weichen_control.turnout_set_for_route.assert_called_with(b'\01', b'\00', False)

