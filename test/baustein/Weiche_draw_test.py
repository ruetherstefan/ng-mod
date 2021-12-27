from unittest.mock import *

import pytest

from src.baustein.Weiche import *
from src.baustein.Weichenadresse import Weichenadresse
from src.baustein.Gleisbelegung import Gleisbelegung


@pytest.fixture
def screen(monkeypatch):
    import pygame

    #monkeypatch.setattr('src.baustein.Weiche.get_image', MagicMock(return_value="EinBild"))

    def fake_blit(bildadresse, position):
        return

    srceen = Mock(spec=pygame.display)
    srceen.blit = fake_blit
    return srceen


@patch('src.baustein.Weiche.Bilder')
@patch('src.baustein.Weiche.WeichenstellungBildLookup')
def test_draw_WeichenStellungGerade(weichenstellung_bild_lookup_mock, bilder, screen):
    weiche = WeicheRechtsNachUnten(screen, Weichenadresse.W1)
    weiche.set_position_index([42,42])
    weiche.draw()
    weichenstellung_bild_lookup_mock.lookup.assert_called_with(ANY, Gleisbelegung.FREI)
