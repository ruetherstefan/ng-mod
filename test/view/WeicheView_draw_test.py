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

    #monkeypatch.setattr('src.baustein.Weiche.get_image', MagicMock(return_value="EinBild"))

    def fake_blit(bildadresse, position):
        return

    srceen = Mock(spec=pygame.display)
    srceen.blit = fake_blit
    return srceen


@patch('src.view.WeicheView.Bilder')
@patch('src.view.WeicheView.WeichenstellungBildLookup')
def test_draw_WeichenStellungGerade(weichenstellung_bild_lookup_mock, bilder, screen):
    weiche: Weiche = WeicheViewRechtsNachUnten(screen, Weiche(Weichenadresse.W1, BesetztModul(BesetztModulAdresse.H1)))
    weiche.set_position_index([42, 42])
    weiche.draw()
    weichenstellung_bild_lookup_mock.lookup.assert_called_with(ANY, Gleisbelegung.FREI)
