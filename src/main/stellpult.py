import pygame

from src.controller.Streckenplaner import Streckenplaner
from src.controller.Weichenstellungcontroller import Weichenstellungscontroller
from src.view.WeicheView import WeicheView
from src.view.Streckenmaler import Streckenmaler
from src.serial.WeichenControlBote import weichen_control

MOUSE_CLICK_LEFT = 1
MOUSE_CLICK_RIGHT = 3

WHITE = (255, 255, 255)


pygame.init()

# setup serial port
weichen_control.initialisation()

size = (1000, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Stellpult Prototyp")

ennepetal_model = Streckenplaner().plane_ennepetal_model()
ennepetal_view = Streckenmaler(ennepetal_model).plane_ennepetal_view(screen)

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
            for gleis_view in ennepetal_view:
                if gleis_view.bild.get_rect().move(gleis_view.get_position()).collidepoint(event.pos):
                    model = gleis_view.model
                    if MOUSE_CLICK_LEFT == event.button:
                        if isinstance(gleis_view, WeicheView): #weg
                            Weichenstellungscontroller().aendere_weichenstellung(model)
                    elif MOUSE_CLICK_RIGHT == event.button:
                        if isinstance(gleis_view, WeicheView): #weg
                            gleis_view.toggle_fahrstrasse()

    # --- Game logic should go here

    # --- Screen-clearing code goes here
    screen.fill(WHITE)

    # --- Drawing code should go here
    for gleis_view in ennepetal_view:
        gleis_view.draw()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

# tear down serial port
weichen_control.de_initialisation()
