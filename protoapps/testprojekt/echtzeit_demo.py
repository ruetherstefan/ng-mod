import pygame

from src.model.Lok import Lok
from src.serial import SerialConnector
from src.serial.LokControl import LokControl
from src.serial.Signal88Control import Signal88Control


pygame.init()

# setup serial port
SerialConnector.initialisation()

size = (1000, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Echzeitdemo Prototyp")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# -------- Main Program Loop -----------
done = False

meldebereich1_besetzt = False
meldebereich1_changed = False
meldebereich2_besetzt = False
meldebereich2_changed = False
meldebereich3_besetzt = False
meldebereich3_changed = False
meldebereich4_besetzt = False
meldebereich4_changed = False

lok = Lok(212)
lok.forwaerts = True

while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #--> umbauen auf nur alle x ticks ausführen
    signale = Signal88Control().lese_signale(1)
    if signale[0] != meldebereich1_besetzt:
        meldebereich1_changed = True
        meldebereich1_besetzt = signale[0]
    if signale[1] != meldebereich2_besetzt:
        meldebereich2_changed = True
        meldebereich2_besetzt = signale[1]
    if signale[2] != meldebereich3_besetzt:
        meldebereich3_changed = True
        meldebereich3_besetzt = signale[2]
    if signale[3] != meldebereich4_besetzt:
        meldebereich4_changed = True
        meldebereich4_besetzt = signale[3]

    # --- Game logic should go here
    # halt und start
    if meldebereich1_changed and meldebereich1_besetzt:
        lok.speed = 120
        LokControl().lok_fahre(lok)
        meldebereich1_changed = False
    elif meldebereich2_changed and meldebereich2_besetzt:
        lok.speed = 120
        LokControl().lok_fahre(lok)
        meldebereich2_changed = False
    elif meldebereich3_changed and meldebereich3_besetzt:
        lok.speed = 30
        LokControl().lok_fahre(lok)
        meldebereich3_changed = False
    elif meldebereich4_changed and meldebereich4_besetzt:
        lok.speed = 0
        LokControl().lok_fahre(lok)
        meldebereich4_changed = False


    # --- Limit to 60 frames per second --> umbauen auf nur alle x ticks ausführen
    clock.tick(5)

# Close the window and quit.
pygame.quit()

# tear down serial port
SerialConnector.de_initialisation()
