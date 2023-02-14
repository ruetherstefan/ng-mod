import sys
from unittest.mock import Mock

import pygame
from pygame.event import Event

from src.controller.Streckenplaner import Streckenplaner
from src.model.BesetztModul import BesetztModul
from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.model.zug.Lok import Lok
from src.model.zug.SpeedModifier import SpeedModifier
from src.model.zug.Zug import Zug
from src.view.Streckenmaler import Streckenmaler


def test_integrationstest_mocking_pygame():
    mock_pygame_quit()
    from src.main.stellpult import Stellpult

    ennepetal_model = Streckenplaner().plane_ennepetal_model()
    ennepetal_view = Streckenmaler(ennepetal_model).plane_ennepetal_view()
    besetzt_module: [BesetztModul] = get_besetzt_module()
    zug = get_zug(besetzt_module)

    stellpult = Stellpult(ennepetal_model, ennepetal_view, besetzt_module, zug)
    stellpult.run()


def mock_pygame_quit():
    pygame_mock = Mock()
    sys.modules['pygame'] = pygame_mock
    pygame_mock.QUIT = pygame.QUIT
    event = Event(pygame.QUIT)
    pygame_mock.event.get = Mock(return_value=[event])


def get_besetzt_module():
    return [BesetztModul(BesetztModulAdresse.H1),
            BesetztModul(BesetztModulAdresse.H2),
            BesetztModul(BesetztModulAdresse.H3)]


def get_zug(besetzt_module):
    zug: Zug = Zug()
    zug.ende = besetzt_module[0]
    zug.anfang = besetzt_module[0]
    zug.speeds = {SpeedModifier.STRECKE_GERADE: 15,
                  SpeedModifier.BAHNHOF_FAHRT: 8}
    zug.lok = Lok(215)
    return zug
