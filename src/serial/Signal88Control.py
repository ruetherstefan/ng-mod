from serial import Serial

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

"""
XSensOff (0x99)- Länge = 1 Byte

Befehlsbytes:
        0: 0x99 XSensOff (Löschen und Rücksetzen S88)

Antwort: 1. Byte: 0 = Ok, accepted

Löscht alle S88-Bits auf Null und löscht alle Change-Flags.
Sinnvoll bei Programmstart, wenn mit Events gearbeitet wird. 
Daraufhin lösen alle aktiven Eingänge das S88 Event aus. 
"""