from unittest.mock import Mock

from src.model.BesetztModul import BesetztModul
from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.serial.Signal88ControlBote import Signal88ControlBote


def test_mock_wenn_offline():
    assert isinstance(Signal88ControlBote().signal_88_control, Mock)


def gegeben_bote_mit_control_returning(control_return):
    bote: Signal88ControlBote = Signal88ControlBote()
    bote.signal_88_control.lese_signale = Mock(return_value=control_return)
    bote.besetzt_modul_adress_mappings__module1 = {BesetztModulAdresse.H1: 0,
                                                   BesetztModulAdresse.H2: 1}
    return bote


def gegeben2modul_mit_besetzt_status(besetzt1, besetzt2):
    modul1: BesetztModul = BesetztModul(BesetztModulAdresse.H1)
    modul1.besetzt = besetzt1

    modul2: BesetztModul = BesetztModul(BesetztModulAdresse.H2)
    modul2.besetzt = besetzt2
    return modul1, modul2


def test_update_module__keine_aenderung_false():
    bote = gegeben_bote_mit_control_returning([False, False, False, False, False, False, False, False])
    modul1, modul2 = gegeben2modul_mit_besetzt_status(False, False)

    bote.update_module([modul1, modul2])
    assert not modul1.besetzt
    assert not modul2.besetzt


def test_update_module__keine_aenderung_true():
    bote = gegeben_bote_mit_control_returning([True, False, False, False, False, False, False, False])
    modul1, modul2 = gegeben2modul_mit_besetzt_status(True, False)

    bote.update_module([modul1, modul2])
    assert modul1.besetzt
    assert not modul2.besetzt


def test_update_module__aenderung_true_mapping1():
    bote = gegeben_bote_mit_control_returning([True, False, False, False, False, False, False, False])
    modul1, modul2 = gegeben2modul_mit_besetzt_status(False, False)

    bote.update_module([modul1, modul2])
    assert modul1.besetzt
    assert not modul2.besetzt


def test_update_module__aenderung_true_mapping2():
    bote = gegeben_bote_mit_control_returning([False, True, False, False, False, False, False, False])
    modul1, modul2 = gegeben2modul_mit_besetzt_status(False, False)

    bote.update_module([modul1, modul2])
    assert not modul1.besetzt
    assert modul2.besetzt


def test_update_module__aenderung_wird_angezeigt_false():
    bote = gegeben_bote_mit_control_returning([True, False, False, False, False, False, False, False])
    modul1, modul2 = gegeben2modul_mit_besetzt_status(True, False)

    assert not bote.update_module([modul1, modul2])


def test_update_module__aenderung_wird_angezeigt_true():
    bote = gegeben_bote_mit_control_returning([True, False, False, False, False, False, False, False])
    modul1, modul2 = gegeben2modul_mit_besetzt_status(False, False)

    assert bote.update_module([modul1, modul2])
