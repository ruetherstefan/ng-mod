import pygame

from src.baustein.Gleis import *
from src.main.Streckenplaner import Streckenplaner


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()


size = (1000, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Stellpult Prototyp")


gleise = Streckenplaner().plane_ennepetal(screen)



# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Loop until the user clicks the close button.
done = False


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for gleis in gleise:
                if gleis.bild.get_rect().move(gleis.get_position()).collidepoint(event.pos):
                    if isinstance(gleis, Weiche):
                        gleis.aendereWeichenstellung()

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

