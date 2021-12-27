from src.serial.WeichenControl import WeichenControl


#################
# Hauptprogramm:
#################

weichenControl = WeichenControl()

weichenControl.initialisation()

# --------------------------------------
# Weiche 1 der IB auf gruen = geradeaus
weichenControl.turnout_set_for_route(b'\01', b'\00', True)

# Weiche 1 der IB auf rot = abbiegen
weichenControl.turnout_set_for_route(b'\01', b'\00', False)

# Reservierung der Weiche für die Fahrstrasse zurueck nehmen.
weichenControl.turnout_free(b'\01', b'\00')

weichenControl.de_initialisation()
