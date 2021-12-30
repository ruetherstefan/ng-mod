import pytest

from src.model.Weiche import Weiche
from src.model.Weichenadresse import Weichenadresse
from src.view.Streckenmaler import Streckenmaler


def test_model_funktion():
    model = Weiche(Weichenadresse.W1)
    maler = Streckenmaler([model, Weiche(Weichenadresse.W2)])
    assert model == maler.get_model(Weichenadresse.W1)


def test_model_funktion_nicht_vorhanden():
    maler = Streckenmaler([])
    with pytest.raises(NotImplementedError):
        maler.get_model(Weichenadresse.W1)

