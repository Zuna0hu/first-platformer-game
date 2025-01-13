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
# BG_COLOR = (255, 255, 255) # white

# set the height and width 
WIDTH, HEIGHT = 1000, 800

# frames per sec
FPS = 60

# play velocity
PLAYER_VEL = 5

# display the window
window = pygame.display.set_mode((WIDTH, HEIGHT))

def get_background(name): # set the background
    # load the tile image
    image = pygame.image.load(join("..", "assets", "Background", name))
    _, _, width, height = image.get_rect() # get the dimenstion info
    tiles = []

    # fill the background with tiles
    for i in range(WIDTH // width + 1): # no space missing
        for j in range(HEIGHT // height + 1):
            pos = (i * width, j * height) # as we draw from topleft corner
            tiles.append(pos)

    return tiles, image

def draw(window, background, bg_image): # this will draw background in window
    for tile in background: # tile is tuple
        window.blit(bg_image, tile) # place image onto the pos


    pygame.display.update()

def main(window):
    # set clock
    clock = pygame.time.Clock()
    # get background info
    background, bg_image = get_background("Blue.png")

    # event loop
    run = True
    while (run):
        clock.tick(FPS) # to ensure the game loop does not run faster than 60 frames per sec

        # to deal with different events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # if click the x
                run = False
                break
        draw(window, background, bg_image)
        
    pygame.quit() # shut up modules of pygame
    quit() # stop execution of python program
    

# if the file is run directly
if __name__ == "__main__":
    main(window)

