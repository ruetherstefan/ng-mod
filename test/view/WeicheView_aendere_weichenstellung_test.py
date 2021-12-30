from unittest.mock import *

import pytest

from src.model.Weiche import Weiche
from src.view.WeicheView import *
from src.model.Weichenadresse import Weichenadresse
from src.model.Weichenstellung import Weichenstellung


@pytest.fixture
def screen(monkeypatch):
    import pygame
    pygame_screen = Mock(spec=pygame.display)


@patch('src.view.WeichenstellungBildLookup.Bilder')
@patch('src.view.WeicheView.Bilder')
@patch('src.view.WeicheView.WeichenControlBote')
def test_aendere_weichenstellung_weicheadresse_weitergabe(weichen_control_bote_mock, bilder, bilder2, screen):
    weiche = WeicheViewRechtsNachUnten(screen, Weiche(Weichenadresse.W1))
    weiche.aendere_weichenstellung()
    weichen_control_bote_mock().aendere_weichenstellung.assert_called_with(Weichenadresse.W1, ANY)


@patch('src.view.WeichenstellungBildLookup.Bilder')
@patch('src.view.WeicheView.Bilder')
@patch('src.view.WeicheView.WeichenControlBote')
def test_aendere_weichenstellung_gerade_zu_abzweigend(weichen_control_bote_mock, bilder, bilder2, screen):
    weiche = WeicheViewRechtsNachUnten(screen, Weiche(Weichenadresse.W1))
    weiche.model.weichenstellung = Weichenstellung.GERADE
    weiche.aendere_weichenstellung()
    weichen_control_bote_mock().aendere_weichenstellung.assert_called_with(ANY, Weichenstellung.ABZWEIGEND)


@patch('src.view.WeichenstellungBildLookup.Bilder')
@patch('src.view.WeicheView.Bilder')
@patch('src.view.WeicheView.WeichenControlBote')
def test_aendere_weichenstellung_abzweigend_zu_gerade(weichen_control_bote_mock, bilder, bilder2, screen):
    weiche = WeicheViewRechtsNachUnten(screen, Weiche(Weichenadresse.W1))
    weiche.model.weichenstellung = Weichenstellung.ABZWEIGEND
    weiche.aendere_weichenstellung()
    weichen_control_bote_mock().aendere_weichenstellung.assert_called_with(ANY, Weichenstellung.GERADE)
