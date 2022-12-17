from src.model.BesetztModul import BesetztModul
from src.model.Weiche import Weiche
from src.model.Weichenstellung import Weichenstellung


class Fahrstrecke:
    def __init__(self):
        self.besetzt_module: [BesetztModul] = []
        self.weichenstellungen: {Weiche: Weichenstellung} = {}