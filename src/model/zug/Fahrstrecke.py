from src.model.BesetztModul import BesetztModul
from src.model.weiche.Weiche import Weiche
from src.model.weiche.Weichenstellung import Weichenstellung
from src.model.zug.SpeedModifier import SpeedModifier


class Fahrstrecke:
    def __init__(self):
        self.besetzt_module: [BesetztModul] = []
        self.weichenstellungen: {Weiche: Weichenstellung} = {}
        self.speed_modifier: {BesetztModul: SpeedModifier} = {}
