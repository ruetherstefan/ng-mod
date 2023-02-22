import sys
from unittest.mock import Mock


def mock_pygame() -> Mock:
    pygame_mock = Mock()
    sys.modules['pygame'] = pygame_mock
    return pygame_mock


class PyTimer:
    def __init__(self, timeout, method_to_call):
        self.timeout = timeout
        self.method_to_call = method_to_call


def test_timer():
    mock_to_call = Mock()
    timer = PyTimer(2000, mock_to_call.a)

    pygame_mock = mock_pygame()
    pygame_mock.timer.get_ticks = Mock(return_value=42)

    assert not mock_to_call.a.called
