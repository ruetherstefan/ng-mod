from copy import copy

import pygame

from src.controller.ZugController import ZugController
from src.model.BesetztModul import BesetztModulVerwalter
from src.model.weiche.Weiche import Weiche
from src.model.zug.Fahrstrecke import Fahrstrecke, DEMO_FAHRSTRECKE_HIN, DEMO_FAHRSTRECKE_ZURUECK
from src.model.zug.Zug import Zug
from src.serial import SerialConnector
from src.serial.LokControlBote import LokControlBote
from src.serial.Signal88ControlBote import Signal88ControlBote
from src.view.BausteinView import BausteinView


class Stellpult:
    WHITE = (255, 255, 255)

    def __init__(self, model, view, besetzt_modul_verwalter, zug) -> None:
        super().__init__()

        self.model: [Weiche] = model
        self.view: [BausteinView] = view
        self.besetzt_modul_verwalter: BesetztModulVerwalter = besetzt_modul_verwalter
        self.zug: Zug = zug

        self.fahrstrecken: [Fahrstrecke] = [copy(DEMO_FAHRSTRECKE_HIN)]

    def run(self):

        SerialConnector.initialisation()

        pygame.init()

        size = (1000, 800)
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Stellpult")

        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()

        # -------- Main Program Loop -----------
        done = False
        waiting_time = 0
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
            geaenderte_modul_signale = Signal88ControlBote().update_module(self.besetzt_modul_verwalter)

            for fahrstrecke in self.fahrstrecken:
                ZugController.update_zug_position(self.zug, fahrstrecke, self.besetzt_modul_verwalter)
                if None is not self.zug.anfang:
                    ZugController.update_zug_speed(self.zug, fahrstrecke)
                    LokControlBote().lok_fahre(self.zug.lok)

                    zug_hat_ende_der_strecke_erreicht = self.zug.anfang is fahrstrecke.besetzt_module[-1]
                    if zug_hat_ende_der_strecke_erreicht:
                        self.fahrstrecken.remove(fahrstrecke)

            # lok Geschwindigkeit Signal geben

            # Demo: neue Strecke setzen
            if 0 == len(self.fahrstrecken):
                if self.zug.anfang is DEMO_FAHRSTRECKE_ZURUECK.besetzt_module[-1]:
                    self.fahrstrecken.append(copy(DEMO_FAHRSTRECKE_HIN))
                    self.zug.lok.forwaerts = not self.zug.lok.forwaerts
                elif self.zug.anfang is DEMO_FAHRSTRECKE_HIN.besetzt_module[-1]:
                    print(waiting_time)
                    if waiting_time == 0:
                        waiting_time = pygame.time.get_ticks()
                    elif waiting_time + 2000 < pygame.time.get_ticks():
                        self.fahrstrecken.append(copy(DEMO_FAHRSTRECKE_ZURUECK))
                        self.zug.lok.forwaerts = not self.zug.lok.forwaerts
                        waiting_time = 0

            # --- Screen-clearing code goes here
            screen.fill(Stellpult.WHITE)

            # --- Drawing code should go here
            for baustein_view in self.view:
                baustein_view.draw(screen)

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 5 frames per second
            clock.tick(30)

        # Close the window and quit.
        pygame.quit()

        # tear down serial port
        SerialConnector.de_initialisation()
