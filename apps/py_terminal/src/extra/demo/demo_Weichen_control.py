from src.serial.WeichenControl import *


#################
# Hauptprogramm:
#################


initialisation()

# --------------------------------------
# Weiche 1 der IB auf gruen = geradeaus
turnout_set_for_route(b'\01', b'\00', True)

# Weiche 1 der IB auf rot = abbiegen
turnout_set_for_route(b'\01', b'\00', False)

# Reservierung der Weiche für die Fahrstrasse zurueck nehmen.
turnout_free(b'\01', b'\00')

de_initialisation()
