from src.model.Lok import Lok


class LokControlBote:
    def lok_fahre(self, lok: Lok):
        pass
        #ser.write(self.get_low_byte_adresse(lok.adresse))
        #answer = ser.read()

    def get_low_byte_adresse(self, adresse: int):
        my_byte = adresse & 0xFF
        return my_byte
