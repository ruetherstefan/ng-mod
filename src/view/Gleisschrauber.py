class Gleisschrauber:

    def __init__(self):
        self.bausteine = []

        self.letzter_baustein = None

    def neu(self, baustein):
        self.bausteine.append(baustein)

        self.letzter_baustein = baustein
        return self

    def rechter_nachbar(self, baustein):
        self.bausteine.append(baustein)
        letzter_index = self.letzter_baustein.get_position_index()
        baustein.set_position_index([letzter_index[0] + 1, letzter_index[1]])

        self.letzter_baustein = baustein
        return self

    def linker_nachbar(self, baustein):
        self.bausteine.append(baustein)
        letzter_index = self.letzter_baustein.get_position_index()
        baustein.set_position_index([letzter_index[0] - 1, letzter_index[1]])

        self.letzter_baustein = baustein
        return self

    def unterer_nachbar(self, baustein):
        self.bausteine.append(baustein)
        letzter_index = self.letzter_baustein.get_position_index()
        baustein.set_position_index([letzter_index[0], letzter_index[1] + 1])

        self.letzter_baustein = baustein
        return self

    def oberer_nachbar(self, baustein):
        self.bausteine.append(baustein)
        letzter_index = self.letzter_baustein.get_position_index()
        baustein.set_position_index([letzter_index[0], letzter_index[1] - 1])

        self.letzter_baustein = baustein
        return self



    def links_unten_nachbar(self, baustein):
        self.bausteine.append(baustein)
        letzter_index = self.letzter_baustein.get_position_index()
        baustein.set_position_index([letzter_index[0] - 1, letzter_index[1] + 1])

        self.letzter_baustein = baustein
        return self

    def links_oben_nachbar(self, baustein):
        self.bausteine.append(baustein)
        letzter_index = self.letzter_baustein.get_position_index()
        baustein.set_position_index([letzter_index[0] - 1, letzter_index[1] - 1])

        self.letzter_baustein = baustein
        return self

    def rechts_unten_nachbar(self, baustein):
        self.bausteine.append(baustein)
        letzter_index = self.letzter_baustein.get_position_index()
        baustein.set_position_index([letzter_index[0] + 1, letzter_index[1] + 1])

        self.letzter_baustein = baustein
        return self

    def rechts_oben_nachbar(self, baustein):
        self.bausteine.append(baustein)
        letzter_index = self.letzter_baustein.get_position_index()
        baustein.set_position_index([letzter_index[0] + 1, letzter_index[1] - 1])

        self.letzter_baustein = baustein
        return self

    def ende(self):
        return self.bausteine