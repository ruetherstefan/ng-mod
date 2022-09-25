"""
Module:  Signal(S)88Control
Import der extern an S88-Hardware-Module angeschlossenen Signale.
Ein Modul besteht aus 2x8 (88) digitalen Eingängen.
Communication with Intellibox (IB) via serial COM port

History:
"""


from src.serial import SerialConnector


class Signal88Control:

    """
    -> Diese Funktion sollte aufgerufen werden, um die erwartete Konfiguration der IB zu prüfen.
       Diese sollte manuell in der IB konfiguriert werden.
    XP88Get (0x9C)- Länge = 1+1 Bytes
    Befehlsbytes:
            0: 0x9C XP88Get (Einlesen der S88 Konfiguration)
            1: Parameternummer:
               0: Zahl der automatisch gelesenen 16Bit-Module
               1, 2: nicht sinnvoll zu nutzten

    Antwort: 1. Byte: 0 = Ok, accepted oder Fehlercode
             2. Byte: Wert des abgefragten Parameters
    """
    def get_anzahl_16bit_module(self):
        cmd = b'\x9C'
        print(cmd)
        SerialConnector.ser.write(cmd)
        parameter = b'\0'
        print (parameter)
        SerialConnector.ser.write(parameter)
        errorcode = SerialConnector.ser.read()
        if errorcode != 0:
            print('Signal88Configuration Error Code: ' + errorcode)
        answer = SerialConnector.ser.read()
        print(answer)
        # Anzahl der in der IB konfigurierten 2-Byte Module
        return answer


    """
    X88PSet (0x9D)- Länge = 1+2 Bytes
    
    Befehlsbytes:
            0: 0x9D XP88Set (Einstellen der S88 Konfiguration)
            1: Parameternummer:
               0: Zahl der automatisch gelesenen 16Bit-Module
               1, 2: nicht sinnvoll zu nutzten
    
    Antwort: 1. Byte: 0 = Ok, accepted oder Fehlercode
    
    N.B. S88 parameter shall only be modified up to the next IB reset.
         In fact, upon an IB reset all s88 parameters are reset to the
         values specified by the user (per IB menus) and stored in the
         corresponding Special Option.
    """


    """
    -> Wichtigste Funktion um die an der IB angeschlossenen S88-Module von der IB einzulesen.
    XSensor (0x98)- Länge = 1+1 Bytes
    
    Befehlsbytes:
            0: 0x98 XSensor (Abfrage S88 Rückmelder)
            1: s88 Modulnummer (1..128) (Modul = 16 Bits)
               s88 module numbers 1..31 may correspond to real s88 modules connected to the IB. 
               Module numbers starting from 32 only correspond to LocoNet sensors.
    
    Antwort: 1. Byte: 0 = Ok, accepted (zwei Bytes folgen)
                      oder Fehlercode (02 = XMsg_BADPRM = angefragter Melder > konfigurierte Melder)
             2. Byte  Kontakte 1..8 dieses Moduls (Bits 7..0)
             3. Byte  Kontakte 9..16 dieses Moduls
    
    N.B. The data read by the XSensor cmd shows the *current* status,
    not the accumulated OR status (as would be the case for P50
    s88 commands), for the s88 module or LocoNet sensor being read.
    
    Reading an s88 module with the XSensor cmd removes any
    eventually pending sensor event for that module.
    """
    def lese_signale(self, modulenumber: int):
        cmd = b'\x98'
        print(cmd)
        SerialConnector.ser.write(cmd)

        print("modulnummer: " + str(modulenumber))
        SerialConnector.ser.write(modulenumber.to_bytes(1, 'little'))
        errorcode = SerialConnector.ser.read()
        if errorcode != b'\x00':
            print('GetS88Module Error Code: ' + str(errorcode))
            return  # Abbruch anders programmieren
        byte1 = SerialConnector.ser.read()      # Eingänge 1..8 dieses Moduls (Bits 7..0)
        byte2 = SerialConnector.ser.read()      # Eingänge 9..16 dieses Moduls

        print("Byte1: " + self.decode_bytes_to_boolarray(byte1))
        print("Byte2: " + self.decode_bytes_to_boolarray(byte2))
        return self.decode_bytes_to_boolarray(byte1) + self.decode_bytes_to_boolarray(byte2)

    def decode_bytes_to_boolarray(self, b: bytes):
        scale = 16  ## equals to hexadecimal
        num_of_bits = 8

        binary_string = bin(int(b.hex(), scale))[2:].zfill(num_of_bits)
        return list(map(lambda x: bool(int(x)), binary_string))

    """
    XSensOff (0x99)- Länge = 1 Byte
    
    Befehlsbytes:
            0: 0x99 XSensOff (Löschen und Rücksetzen S88)
    
    Antwort: 1. Byte: 0 = Ok, accepted
    
    Löscht alle S88-Bits auf Null und löscht alle Change-Flags.
    Sinnvoll bei Programmstart, wenn mit Events gearbeitet wird. 
    Daraufhin lösen alle aktiven Eingänge das S88 Event aus. 
    """

    def encode_booleans(bool_lst):
        res = 0
        for i, bval in enumerate(bool_lst):
            res += int(bval) << i
        return res

    def decode_booleans(intval, bits):
        res = []
        for bit in xrange(bits):
            mask = 1 << bit
            res.append((intval & mask) == mask)
        return res