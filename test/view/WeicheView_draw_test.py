from unittest.mock import *

import pytest

from src.model.BesetztModul import BesetztModul
from src.model.weiche.Weiche import Weiche
from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.view.WeicheView import *
from src.model.weiche.Weichenadresse import Weichenadresse
from src.model.Gleisbelegung import Gleisbelegung


@pytest.fixture
def screen(monkeypatch):
    import pygame

    def fake_blit(bildadresse, position):
        return

    screen = Mock(spec=pygame.display)
    screen.blit = fake_blit
    return screen


@patch('src.view.WeicheView.Bilder')
@patch('src.view.WeicheView.WeichenstellungBildLookup')
def test_draw_WeichenStellungGerade(weichenstellung_bild_lookup_mock, bilder, screen):
    weiche: Weiche = WeicheViewRechtsNachUnten(Weiche(Weichenadresse.W1, BesetztModul(BesetztModulAdresse.H1)))
    weiche.set_position_index([42, 42])
    weiche.draw(screen)
    weichenstellung_bild_lookup_mock.lookup.assert_called_with(ANY, Gleisbelegung.FREI)
