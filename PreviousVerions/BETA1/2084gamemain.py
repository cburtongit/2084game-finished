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
width = 16
height = 16
vel = 5
left = False
right = False
up = False
down = False
still = False

# loading sprites
down1 = pygame.image.load('link_down1.png')
down2 = pygame.image.load('link_down2.png')
up1   = pygame.image.load('link_up1.png')
up2   = pygame.image.load('link_up2.png')
left1 = pygame.image.load('link_left1.png')
left2 = pygame.image.load('link_left2.png')
right1 = pygame.transform.flip(left1, True, False) #tried a new way to flip the sprite as the previous one gave me errors
background = pygame.image.load('backgrounddevmap.png')
charstill = pygame.image.load('link_down1.png')

# flipping the left sprite after making a copy makes it look like a right walking sprite except it saves on memory
#right1 = left1.getCopy()
#right1.flip(True, False)
#right1.makeTransformsPermanent()


def drawmainwin():
    global stepCount
    mainwin.blit(background, (0,0))

    if left:
        mainwin.blit(left1, (x,y))
    elif right:
        mainwin.blit(right1, (x,y))
    elif up:
        mainwin.blit(up1, (x,y))
    elif down:
        mainwin.blit(down1, (x,y))
    else:
        mainwin.blit(charstill, (x,y))
    pygame.display.update()# in order for new information to appear on screen, this command updates what is drawn.

# def mainloop():
running = True
while running:
    pygame.time.delay(10) # this is a way to create a "clock" in pygame apparently, I can probably use this to set the speed of animations or actions later

    for event in pygame.event.get():# pygame programs usually have a main loop, this checks for player input or events such as mouse or keyboard input.
        if event.type == pygame.QUIT:# lupon clicking the close window button the game will end the loop thus closing the game as the next line quits the game.
            running = False

    kbinput = pygame.key.get_pressed()# sets up keyboard input NOTE: Pygame's movement engine has the point 0,0 at the TOP left of the window as opposed to the BOTTOM left like on most graphs, so +y would go DOWN rather than up

    if kbinput[pygame.K_LEFT] and x > 0:
        x -= vel
        left = True
        right = False
        still = False
        chardir = 'LEFT'
    elif kbinput[pygame.K_RIGHT] and x < 1000:
        x += vel
        left = False
        right = True
        still = False
        chardir = 'RIGHT'
    elif kbinput[pygame.K_UP] and y > 0:
        y -= vel
        up = True
        down = False
        still = False
        chardir = 'UP'
    elif kbinput[pygame.K_DOWN] and y < 1000:
        y += vel
        up = False
        down = True
        still = False
        chardir = 'DOWN'
    else:
        left = False
        right = False
        up = False
        down = False
        still = True


    drawmainwin()

pygame.quit()
