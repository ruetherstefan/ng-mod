from unittest.mock import *

import pytest

from src.view.Baustein import Baustein


@pytest.fixture
def baustein():
    import pygame
    pygame_screen = Mock(spec=pygame.display)
    return Baustein(pygame_screen)


def test_get_position__0_0(baustein):
    baustein.set_position_index([0, 0])
    assert baustein.get_position() == [0, 0]


def test_get_position__5_3(baustein):
    baustein.set_position_index([5, 3])
    assert baustein.get_position() == [5 * 32, 3 * 32]


def test_get_position__not_initialized(baustein):
    with pytest.raises(TypeError):
        assert baustein.get_position() == [0, 0]
