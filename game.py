import pygame
import sys
from pygame.locals import *

pygame.init()

gravity=1

#Game loop begins 
while True:
    # this below is the quit code inside the game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    #this updates the screen
    pygame.display.update()
