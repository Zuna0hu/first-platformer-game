# import libraries
import os
import random
import math
import pygame

# for read files quicker
from os import listdir
from os.path import isfile, join

# initialize the game
pygame.init()

# set the title (caption) of the window
pygame.display.set_caption("My First Game")

# set the background color
BG_COLOR = (255, 255, 255) # white

# set the height and width 
WIDTH, HEIGHT = 1000, 800

# frames per sec
FPS = 60

# play velocity
PLAYER_VEL = 5

# display the window
window = pygame.display.set_mode((WIDTH, HEIGHT))

def main(window):
    # set the clock
    clock = pygame.time.Clock()

    # event loop
    run = True
    while (run):
        clock.tick(FPS) # to ensure the game loop does not run faster than 60 frames per sec

        # to deal with different events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

    

# if the file is run directly
if __name__ == "__main__":
    main(window)

