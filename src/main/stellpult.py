import pygame

from src.baustein.Weiche import Weiche
from src.main.Streckenplaner import Streckenplaner
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

gleise = Streckenplaner().plane_ennepetal(screen)

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
            for gleis in gleise:
                if gleis.bild.get_rect().move(gleis.get_position()).collidepoint(event.pos):
                    if MOUSE_CLICK_LEFT == event.button:
                        if isinstance(gleis, Weiche):
                            gleis.aendere_weichenstellung()
                    elif MOUSE_CLICK_RIGHT == event.button:
                        if isinstance(gleis, Weiche):
                            gleis.toggleFahrstrasse()

    # --- Game logic should go here

    # --- Screen-clearing code goes here
    screen.fill(WHITE)

    # --- Drawing code should go here
    for gleis in gleise:
        gleis.draw()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

# tear down serial port
weichen_control.de_initialisation()
