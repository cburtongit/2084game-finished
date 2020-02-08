# Welcome to 2084 ver 0.0.0.3
# Created by Cameron Burton, with help from the Pygame and Python community!

#importing modules
import pygame
from pygame.locals import *
import sys
import time
import pyganim #used for animations

#initialises pygame, was told this was necessary
pygame.init()

# def musicplayer():
# next 3 lines load and play a music track, setting the play argument to -1 simply repeats the usic endlessly
pygame.mixer.init()
pygame.mixer.music.load("track1enolagay.ogg")
pygame.mixer.music.play(-1)

mainwin = pygame.display.set_mode((1000, 1000))# this sets height and width of my window and creates a window.
pygame.display.set_caption("2084 Ver 0.0.0.4")# sets window title

# character creation, these are the definitions of what a drawn character will look like, used later.
x = 100
y = 100
vel = 5

#loading in stuff
background = pygame.image.load('backgrounddevmap.png')

def drawmainwin():
    mainwin.blit(background, (0,0))

#def mainLoop():
running = True
while running:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        
    keyinput = pygame.key.get_pressed() 

    drawmainwin()

pygame.quit()
