from copy import copy

import pygame

from src.controller.ZugController import ZugController
from src.model.BesetztModul import BesetztModulVerwalter
from src.model.BesetztModulAdresse import BesetztModulAdresse
from src.model.weiche.Weiche import Weiche
from src.model.zug.Fahrstrecke import Fahrstrecke
from src.model.zug.SpeedModifier import SpeedModifier
from src.model.zug.Zug import Zug
from src.serial import SerialConnector
from src.serial.Signal88ControlBote import Signal88ControlBote
from src.view.BausteinView import BausteinView


class Stellpult:
    WHITE = (255, 255, 255)

    # Test Fahrstrecke definition
    DEMO_FAHRSTRECKE_HIN = Fahrstrecke()
    DEMO_FAHRSTRECKE_ZURUECK = Fahrstrecke()

    def __init__(self, model, view, besetzt_modul_verwalter, zug) -> None:
        super().__init__()

        self.model: [Weiche] = model
        self.view: [BausteinView] = view

        # Test Besetztmodule init
        self.besetzt_modul_verwalter: BesetztModulVerwalter = besetzt_modul_verwalter

        # Test Züge init
        self.zug: Zug = zug

        Stellpult.DEMO_FAHRSTRECKE_HIN.besetzt_module = [BesetztModulAdresse.H1, BesetztModulAdresse.H2,
                                                         BesetztModulAdresse.H3]
        Stellpult.DEMO_FAHRSTRECKE_HIN.speed_modifier = {
            Stellpult.DEMO_FAHRSTRECKE_HIN.besetzt_module[0]: SpeedModifier.BAHNHOF_FAHRT,
            Stellpult.DEMO_FAHRSTRECKE_HIN.besetzt_module[2]: SpeedModifier.BAHNHOF_STOP}

        Stellpult.DEMO_FAHRSTRECKE_ZURUECK.besetzt_module = list(
            reversed(Stellpult.DEMO_FAHRSTRECKE_HIN.besetzt_module))
        Stellpult.DEMO_FAHRSTRECKE_ZURUECK.speed_modifier = {
            Stellpult.DEMO_FAHRSTRECKE_ZURUECK.besetzt_module[0]: SpeedModifier.BAHNHOF_FAHRT,
            Stellpult.DEMO_FAHRSTRECKE_ZURUECK.besetzt_module[2]: SpeedModifier.BAHNHOF_STOP}

        self.fahrstrecken: [Fahrstrecke] = [copy(Stellpult.DEMO_FAHRSTRECKE_HIN)]

    def run(self):

        pygame.init()

        # setup serial port
        SerialConnector.initialisation()

        size = (1000, 800)
        screen = pygame.display.set_mode(size)

        pygame.display.set_caption("Stellpult")

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
                    for baustein_view in self.view:
                        if baustein_view.bild.get_rect().move(baustein_view.get_position()).collidepoint(event.pos):
                            baustein_view.click(event)

            # --- Game logic should go here

            # Besetztabfrage
            Signal88ControlBote().update_module(self.besetzt_modul_verwalter)

            for fahrstrecke in self.fahrstrecken:
                ZugController.update_zug_position(self.zug, fahrstrecke, self.besetzt_modul_verwalter)
                ZugController.update_zug_speed(self.zug, fahrstrecke)

                zug_hat_ende_der_strecke_erreicht = self.zug.anfang is fahrstrecke.besetzt_module[-1]
                if zug_hat_ende_der_strecke_erreicht:
                    self.fahrstrecken.remove(fahrstrecke)

            # lok Geschwindigkeit Signal geben

            # Demo: neue Strecke setzen
            if 0 == len(self.fahrstrecken):
                if self.zug.anfang is BesetztModulAdresse.H1:
                    self.fahrstrecken.append(copy(Stellpult.DEMO_FAHRSTRECKE_HIN))
                elif self.zug.anfang is BesetztModulAdresse.H3:
                    self.fahrstrecken.append(copy(Stellpult.DEMO_FAHRSTRECKE_ZURUECK))

            # --- Screen-clearing code goes here
            screen.fill(Stellpult.WHITE)

            # --- Drawing code should go here
            for baustein_view in self.view:
                baustein_view.draw(screen)

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            clock.tick(60)

        # Close the window and quit.
        pygame.quit()

        # tear down serial port
        SerialConnector.de_initialisation()
