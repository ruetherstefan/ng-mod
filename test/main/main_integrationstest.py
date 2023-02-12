import sys
from unittest.mock import patch, Mock

import pygame
from pygame.event import Event


def test_integrationstest_mocking_pygame():
    pygame_mock = Mock()

    sys.modules['pygame'] = pygame_mock
    pygame_mock.QUIT = pygame.QUIT

    event = Event(pygame.QUIT)
    pygame_mock.event.get = Mock(return_value=[event])

    import src.main.stellpult
