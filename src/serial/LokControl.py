from src.model.Lok import Lok


class LokControl:
    def lok_fahre(self, lok: Lok):
        ser.write(self.get_adresse_low_byte(lok.adresse))
        answer = ser.read()

        ser.write(self.get_adresse_high_byte(lok.adresse))
        answer = ser.read()

        ser.write(lok.speed)
        answer = ser.read()

        ser.write(self.get_byte_funktionen(lok))
        answer = ser.read()

    def get_adresse_low_byte(self, adresse: int):
        my_byte = adresse & 0xFF
        return my_byte

    def get_adresse_high_byte(self, adresse: int):
        my_byte = adresse >> 8
        return my_byte

    def get_byte_funktionen(self, lok: Lok):
        byte_funktion = 0xc0       # default bit 6 und 7
        if lok.forwaerts:
            byte_funktion += 0x20      # forwaerts bit 5 setzen
        if lok.frontlicht:
            byte_funktion += 0x10      # frontlicht bit 4 setzen
        if lok.f4:
            byte_funktion += 0x08      # funktion F4 bit 3 setzen
        if lok.f3:
            byte_funktion += 0x04      # funktion F3 bit 2 setzen
        if lok.f2:
            byte_funktion += 0x02      # funktion F2 bit 1 setzen
        if lok.f1:
            byte_funktion += 0x01      # funktion F1 bit 0 setzen
        return byte_funktion
