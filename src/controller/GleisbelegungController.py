from src.model.Gleisbelegung import Gleisbelegung


class GleisbelegungController:
    def toggle_fahrstrasse(self, weiche):
        if Gleisbelegung.FAHRSTRASSE == weiche.gleisbelegung:
            weiche.gleisbelegung = Gleisbelegung.FREI
        else:
            weiche.gleisbelegung = Gleisbelegung.FAHRSTRASSE

