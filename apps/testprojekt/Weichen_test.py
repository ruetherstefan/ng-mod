# Module:

# Weichen_Test
# Steuerung von Weichen (englisch turnouts)
# Communication with Intellibox (IB) via serial COM port
# Von diesem Modul werden die Routinen aus dem Modul Weichen_control aufgerufen um sie zu testen.
#
# History:
# 29.03.2019 - 1.01:
#

from Weichen_control import initialisation
from Weichen_control import de_initialisation
from Weichen_control import turnout_set_for_route
from Weichen_control import turnout_free





#################
# Hauptprogramm:
#################
#def test():

initialisation()

# --------------------------------------
# Weiche 1 der IB auf gruen = geradeaus
# turnout_set_for_route(b'\02', b'\00', True)
turnout_set_for_route(2, True)

# Weiche 1 der IB auf rot = abbiegen
# turnout_set_for_route(b'\02', b'\00', False)
turnout_set_for_route(2, False)

# Reservierung der Weiche für die Fahrstrasse zurueck nehmen.
turnout_free(b'\02', b'\00')

de_initialisation()

#string = b'\x90'
#str2 = hex(55)
#str3 = "b'" + "\\" + str2[1:] + "'"
#print(string)
#print(str2)
#print(str3)
