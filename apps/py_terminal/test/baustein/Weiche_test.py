from unittest.mock import *

import pytest

from src.baustein.Weiche import *
from src.baustein.Weichenadresse import Weichenadresse
from src.baustein.Weichenstellung import Weichenstellung


@pytest.fixture
def screen():
    import pygame
    pygame_screen = Mock(spec=pygame.display)


@patch('src.baustein.Weiche.get_image')
@patch('src.baustein.Weiche.WeichenControlBote')
def test_aendere_weichenstellung_weicheadresse_weitergabe(weichen_control_bote_mock, get_image, screen):
    weiche = WeicheRechtsNachUnten(screen, Weichenadresse.W1)
    weiche.aendere_weichenstellung()
    weichen_control_bote_mock().aendere_weichenstellung.assert_called_with(Weichenadresse.W1, ANY)


@patch('src.baustein.Weiche.get_image')
@patch('src.baustein.Weiche.WeichenControlBote')
def test_aendere_weichenstellung_gerade_zu_abzweigend(weichen_control_bote_mock, get_image, screen):
    weiche = WeicheRechtsNachUnten(screen, Weichenadresse.W1)
    weiche.weichenstellung = Weichenstellung.GERADE
    weiche.aendere_weichenstellung()
    weichen_control_bote_mock().aendere_weichenstellung.assert_called_with(Weichenadresse.W1, Weichenstellung.ABZWEIGEND)

@patch('src.baustein.Weiche.get_image')
@patch('src.baustein.Weiche.WeichenControlBote')
def test_aendere_weichenstellung_abzweigend_zu_gerade(weichen_control_bote_mock, get_image, screen):
    weiche = WeicheRechtsNachUnten(screen, Weichenadresse.W1)
    weiche.weichenstellung = Weichenstellung.ABZWEIGEND
    weiche.aendere_weichenstellung()
    weichen_control_bote_mock().aendere_weichenstellung.assert_called_with(Weichenadresse.W1, Weichenstellung.GERADE)
