from src.model.BesetztModul import BesetztModul
from src.model.zug.Lok import Lok
from src.model.zug.SpeedModifier import SpeedModifier


class Zug:
    def __init__(self):
        self.ende: BesetztModul = None
        self.anfang: BesetztModul = None
        self.lok: Lok = None
        self.speeds: {SpeedModifier: int} = {}
