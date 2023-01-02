from src.model.weiche.Weiche import Weiche
from src.model.weiche.Weichenadresse import Weichenadresse
from src.view.WeicheView import WeicheView


def test_nicht_digitale_weiche_kein_model():
    weiche_view = WeicheView(None, None)
    assert weiche_view.model is None


def test_digitale_weiche_model_verbunden():
    model = Weiche(Weichenadresse.W1)
    weiche_view = WeicheView(None, model)
    assert weiche_view.model is model
