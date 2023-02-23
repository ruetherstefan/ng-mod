import sys
from unittest.mock import Mock, MagicMock

from src.util.PyTimer import PyTimer


def mock_pygame() -> Mock:
    pygame_mock = MagicMock()
    sys.modules['pygame'] = pygame_mock
    return pygame_mock


def test_timer__zeit_nicht_abgelaufen():
    pygame_mock = mock_pygame()
    pygame_mock.time.get_ticks.return_value = 42

    mock_to_call = Mock()
    timer = PyTimer(2000, mock_to_call.a)

    assert not timer.run()
    assert not mock_to_call.a.called


def test_timer__zeit_abgelaufen():
    pygame_mock = mock_pygame()
    pygame_mock.time.get_ticks.side_effect = [42, 3000]

    mock_to_call = Mock()
    timer = PyTimer(2000, mock_to_call.a)

    assert timer.run()
    assert mock_to_call.a.called
