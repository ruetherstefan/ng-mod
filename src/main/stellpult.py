from copy import copy

import pygame

from src.controller.Streckenplaner import Streckenplaner
from src.controller.ZugController import ZugController
from src.model.BesetztModul import BesetztModul
from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.model.zug.Fahrstrecke import Fahrstrecke
from src.model.zug.Lok import Lok
from src.model.zug.SpeedModifier import SpeedModifier
from src.model.zug.Zug import Zug
from src.serial import SerialConnector
from src.serial.Signal88ControlBote import Signal88ControlBote
from src.view.Streckenmaler import Streckenmaler

WHITE = (255, 255, 255)

pygame.init()

# setup serial port
SerialConnector.initialisation()

size = (1000, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Stellpult Prototyp")

ennepetal_model = Streckenplaner().plane_ennepetal_model()
ennepetal_view = Streckenmaler(ennepetal_model).plane_ennepetal_view(screen)

# Test Besetztmodule init
besetzt_module: [BesetztModul] = [BesetztModul(BesetztModulAdresse.H1),
                                  BesetztModul(BesetztModulAdresse.H2),
                                  BesetztModul(BesetztModulAdresse.H3)]

# Test Züge init
zug: Zug = Zug()
zug.ende = besetzt_module[0]
zug.anfang = besetzt_module[0]
zug.speeds = {SpeedModifier.STRECKE_GERADE: 15,
              SpeedModifier.BAHNHOF_FAHRT: 8}
zug.lok = Lok(215)


# Test Fahrstrecke definition
DEMO_FAHRSTRECKE_HIN = Fahrstrecke()
DEMO_FAHRSTRECKE_HIN.besetzt_module = besetzt_module
DEMO_FAHRSTRECKE_HIN.speed_modifier = {DEMO_FAHRSTRECKE_HIN.besetzt_module[0]: SpeedModifier.BAHNHOF_FAHRT,
                                       DEMO_FAHRSTRECKE_HIN.besetzt_module[2]: SpeedModifier.BAHNHOF_STOP}

DEMO_FAHRSTRECKE_ZURUECK = Fahrstrecke()
DEMO_FAHRSTRECKE_ZURUECK.besetzt_module = list(reversed(besetzt_module))
DEMO_FAHRSTRECKE_ZURUECK.speed_modifier = {DEMO_FAHRSTRECKE_ZURUECK.besetzt_module[0]: SpeedModifier.BAHNHOF_FAHRT,
                                           DEMO_FAHRSTRECKE_ZURUECK.besetzt_module[2]: SpeedModifier.BAHNHOF_STOP}

fahrstrecken: [Fahrstrecke] = [copy(DEMO_FAHRSTRECKE_HIN)]

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
done = False

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for baustein_view in ennepetal_view:
                if baustein_view.bild.get_rect().move(baustein_view.get_position()).collidepoint(event.pos):
                    baustein_view.click(event)

    # --- Game logic should go here

    # Besetztabfrage
    # TODO Signal88ControlBote besetzt_modul_adress_mappings__module1 schreiben
    Signal88ControlBote().update_module(besetzt_module)

    for fahrstrecke in fahrstrecken:
        ZugController.update_zug_position(zug, fahrstrecke)
        ZugController.update_zug_speed(zug, fahrstrecke)

        zug_hat_ende_der_strecke_erreicht = zug.anfang is fahrstrecke.besetzt_module[-1]
        if zug_hat_ende_der_strecke_erreicht:
            fahrstrecken.remove(fahrstrecke)

    #lok Geschwindigkeit Signal geben

    # Demo: neue Strecke setzen
    if 0 == len(fahrstrecken):
        if zug.anfang is besetzt_module[0]:
            fahrstrecken.append(copy(DEMO_FAHRSTRECKE_HIN))
        elif zug.anfang is besetzt_module[-1]:
            fahrstrecken.append(copy(DEMO_FAHRSTRECKE_ZURUECK))


    # --- Screen-clearing code goes here
    screen.fill(WHITE)

    # --- Drawing code should go here
    for baustein_view in ennepetal_view:
        baustein_view.draw()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

# tear down serial port
SerialConnector.de_initialisation()
