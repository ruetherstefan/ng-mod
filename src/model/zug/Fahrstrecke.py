from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.model.weiche.Weiche import Weiche
from src.model.weiche.Weichenstellung import Weichenstellung
from src.model.zug.SpeedModifier import SpeedModifier


class Fahrstrecke:
    def __init__(self):
        self.besetzt_module: [BesetztModulAdresse] = []
        self.weichenstellungen: {Weiche: Weichenstellung} = {}
        self.speed_modifier: {BesetztModulAdresse: SpeedModifier} = {}
