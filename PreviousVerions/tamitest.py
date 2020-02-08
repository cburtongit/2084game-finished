import pygame
from pygame.locals import *
import sys
import time

def mainMenu:
    menurunning = True
    while menurunning = True:



# Better Input Handling
UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

SHOOT = "shoot"
ATTACK = "attack"

currentInputs = []

for event in pygame.event.get():
    if event.type == KEYDOWN:
        if event.key == K_LEFT:
            currentInputs.append(LEFT)

        if event.key == K_RIGHT:
            currentInputs.append(RIGHT)

        if event.key == K_UP:
            currentInputs.append(UP)

        if event.key == K_DOWN:
            currentInputs.append(DOWN)

    elif event.type == KEYUP:
        if event.key == K_LEFT:
            currentInputs.remove(LEFT)

        if event.key == K_RIGHT:
            currentInputs.remove(RIGHT)

        if event.key == K_UP:
            currentInputs.remove(UP)

        if event.key == K_DOWN:
            currentInputs.remove(DOWN)
        
