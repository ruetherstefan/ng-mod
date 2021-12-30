from unittest.mock import *

import pytest

from src.model.Weichenadresse import Weichenadresse


from src.controller.Streckenplaner import Streckenplaner


def test_w1_enthalten():
    models = Streckenplaner().plane_ennepetal_model()
    assert gib_weiche_zu_adresse(models, Weichenadresse.W1) is not None


def test_w20_enthalten():
    models = Streckenplaner().plane_ennepetal_model()
    assert gib_weiche_zu_adresse(models, Weichenadresse.W20) is not None


#def test_undefiniert_nicht_enthalten():
#    models = Streckenplaner().plane_ennepetal_model()
#    assert gib_weiche_zu_adresse(models, Weichenadresse.Undefiniert) is None


def gib_weiche_zu_adresse(weichen, adresse):
    for weiche in weichen:
        if weiche.adresse == adresse:
            return weiche



