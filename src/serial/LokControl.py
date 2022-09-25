from serial import Serial

from src.model.Lok import Lok
from src.serial import SerialConnector

"""
function lok_cmd()
Control of one Lok, with all relevant parameters

XLok (080h) + 4 Byte
Parameters (byte)
1st	low byte of Lok address
2nd	high byte of Lok address
3rd	speed (0..127: 0 = Stop, 1 = Stop/Em.Stop)
N.B. bit #7 is reserved for future use!
4th	this byte has the following format:

bit    7     6     5     4     3     2     1     0
    +-----+-----+-----+-----+-----+-----+-----+-----+
    |ChgF |Force| Dir | FL  | F4  | F3  | F2  | F1  |
    +-----+-----+-----+-----+-----+-----+-----+-----+

where:
ChgF	set if F1..F4 to be used for setting F1..F4 of
        Lok (otherwise F1..F4 are ignored)
Force	if set (1), then the XLok command is 'forced'
        even in case of a Lok already controlled by a
        non-PC device
Dir	Lok direction: 1 = forward, 0 = reverse
FL	Lok light status: 1 = on, 0 = off
F4..F1	Lok F4..F1 status (if ChgF is set)

N.B.	Address must be in range 0..9999
(depending on protocol, not every address is legal!)

Reply:
1st	either 00h (cmd Ok) or error code.

Error/warning codes:
XBADPRM (02h)	illegal parameter value
XNOLSPC (08h)	there is no space in the Lok cmd buffer, please try later!
XNOSLOT (0Bh)	there is no slot available
XBADLNP (0Ch)	Lok# is illegal for this protocol
XLKBUSY (0Dh)	Lok already controlled by another device
XLKHALT (41h)	Command accepted (Lok status updated), but IB in 'Halt' mode!
XLkPOFF (42h)	Command accepted (Lok status updated), but IB in Power Off!

Remark:  F2...F4 are not supported here, because no lok with this functions available.
"""
class LokControl:
    def lok_fahre(self, lok: Lok):
        cmd = b'\x80'
        print(cmd)
        SerialConnector.ser.write(cmd)
        b1 = self.get_adresse_low_byte(lok.adresse).to_bytes(1, 'little')
        print(b1)
        SerialConnector.ser.write(b1)
        #answer = SerialConnector.ser.read()

        b2 = self.get_adresse_high_byte(lok.adresse).to_bytes(1, 'little')
        print(b2)
        SerialConnector.ser.write(b2)
        #answer = SerialConnector.ser.read()

        bspeed = lok.speed.to_bytes(1, 'little')
        print(bspeed)
        SerialConnector.ser.write(bspeed)
        #answer = SerialConnector.ser.read()

        bspezial = self.get_byte_funktionen(lok).to_bytes(1, 'little')
        print(bspezial)
        SerialConnector.ser.write(bspezial)
        answer = SerialConnector.ser.read()

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


"""
XStatus (0xA2)- Länge = 1 Byte

Befehlsbytes:
        0: 0xA2 XStatus (Statusabfrage für Spannung, Zustand usw.)

Antwort: Bitfeld, folgende Zuordnung:
         Bit 7:  Erweiterungsbit, wenn 1, kommt noch ein weiteres Byte als Antwort.
                 (momentan immer 0)
         Bit 6:  VREG: 1: Spannungsregelung (N Spur) ist aktiviert (ist bei bei uns der Fall)
                       0: keine Spannungsregelung
         Bit 5:  I2C   1: externes I2C Gerät vorhanden
                       0: nichts angeschlossen (unser Standard)
         Bit 4:  HALT  1: Loks angehalten, aber Gleisspannung vorhanden
         Bit 3:  PWR:  1: Zustand "EIN", grüne LED leuchtet.
                       0: Zustand "AUS", rot leuchtet.
         Bit 2:  HOT   1: zu heiss
                       0: (OpenDCC)
         Bit 1:  GO    1: falls gerade der grüne Taster an externer I2C Zentrale betätigt. (keine Entprellung)
         Bit 0:  STOP  1: falls gerade der rote Taster an externer I2C Zentrale betätigt. (keine Entprellung)
"""
