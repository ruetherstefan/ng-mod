import pygame

from src.baustein.Gleis import *
from src.baustein.Baustein import Gleisschrauber


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()


size = (1000, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Stellpult Prototyp")


# load images
gleis1 = GleisVertikal(screen)
gleis1.set_position_index([25, 10])

gleise = Gleisschrauber().neu(gleis1)\
    .unterer_nachbar(GleisObenNachLinks(screen))\
    .links_unten_nachbar(GleisLinksNachOben(screen))\
    .linker_nachbar(WeicheLinksNachUnten(screen)) \
    .linker_nachbar(WeicheRechtsNachOben(screen)) \
    .links_oben_nachbar(GleisLinksNachUnten(screen)) \
    .linker_nachbar(GleisHorizontal(screen)) \
    .linker_nachbar(GleisHorizontal(screen)) \
    .linker_nachbar(GleisRechtsNachUnten(screen)) \
    .links_unten_nachbar(WeicheLinksUntenNachOben(screen)) \
    .rechter_nachbar(GleisHorizontal(screen)) \
    .rechter_nachbar(GleisHorizontal(screen)) \
    .rechter_nachbar(GleisHorizontal(screen)) \
    .rechter_nachbar(GleisHorizontal(screen)) \
    .ende()



gleis2 = GleisVertikal(screen)
gleis2.set_position_index([gleis1.get_position_index()[0] + 1, gleis1.get_position_index()[1] + 1])

abschnitt2 = Gleisschrauber().neu(gleis2)\
    .unterer_nachbar(GleisObenNachLinks(screen))\
    .links_unten_nachbar(GleisLinksNachOben(screen))\
    .linker_nachbar(WeicheRechtsNachOben(screen))\
    .linker_nachbar(GleisHorizontal(screen))\
    .linker_nachbar(GleisHorizontal(screen))\
    .linker_nachbar(GleisHorizontal(screen))\
    .linker_nachbar(GleisHorizontal(screen))\
    .linker_nachbar(GleisHorizontal(screen))\
    .linker_nachbar(GleisHorizontal(screen))\
    .linker_nachbar(GleisHorizontal(screen))\
    .linker_nachbar(WeicheLinksUntenNachOben(screen))\
    .links_unten_nachbar(GleisUntenNachRechts(screen))\
    .ende()
gleise.extend(abschnitt2)



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
            print("User pressed a mouse button")

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

