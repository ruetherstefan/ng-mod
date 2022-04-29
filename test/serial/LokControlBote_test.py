from src.serial.LokControlBote import LokControlBote


def test_get_low_byte_adresse_1():
    assert 1 == LokControlBote().get_low_byte_adresse(1)
