
# Welcome to 2084 ver 0.0.0.4
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
#pygame.mixer.music.load("track1.ogg")
#pygame.mixer.music.play(-1)

#by defining these as a variable I can simply change these variables latter to change the resolution rather than edit the program in every bit they're referenced.
WINDOWWIDTH = 1600
WINDOWHEIGHT = 900

mainwin = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))# this sets height and width of my window and creates a window.
pygame.display.set_caption("2084 Ver 0.1.0.3")# sets window title

# character creation, these are the definitions of what a drawn character will look like, used later.
x = 100
y = 100
vel = 10
width = 64
height = 64
direction = 'left' #start off as left facing
moveleft = moveright = moveup = movedown = False

#loading in characters and enviroment
background = pygame.image.load('sprites/background1.png')
leftidle = pygame.image.load("sprites/left.png")
rightidle = pygame.image.load("sprites/right.png")
upidle = pygame.image.load("sprites/up.png")
downidle = pygame.image.load("sprites/down.png")

#pyganim aminations for character
charanim = {}
charanim["walkleft"] = pyganim.PygAnimation([("sprites/left2.png", 100), ("sprites/left.png", 100), ("sprites/left3.png", 100), ("sprites/left.png", 10)])
charanim["walkright"] = pyganim.PygAnimation([("sprites/right2.png", 100), ("sprites/right.png", 100), ("sprites/right3.png", 100), ("sprites/right.png", 10)])
charanim["walkup"] = pyganim.PygAnimation([("sprites/up2.png", 100), ("sprites/up.png", 100), ("sprites/up3.png", 100), ("sprites/up.png", 10)])
charanim["walkdown"] = pyganim.PygAnimation([("sprites/down2.png", 100), ("sprites/down.png", 100), ("sprites/down3.png", 100), ("sprites/down.png", 10)])

charanim["shootright"] = pyganim.PygAnimation([("sprites/muzzleflash.png", 125), ("sprites/muzzleflash2.png", 125), ("sprites/muzzleflash3.png", 125), ("sprites/muzzleflash4.png", 125)])
# I can invert the right facing sprite to save time creating another image
charanim["shootleft"] = charanim["walkleft"].getCopy()
charanim["shootleft"].flip(True, False)
charanim["shootleft"].makeTransformsPermanent()

moveConductor = pyganim.PygConductor(charanim)

#mainmenu animations
mainmenuanim = {}
mainmenuanim["splashscreen"] = pyganim.PygAnimation([("sprites/splash1.png", 500), ("sprites/splash2.png", 500)])
mainmenuConductor = pyganim.PygConductor(mainmenuanim)
pygame.mixer.music.load('track0.ogg')


#def drawmainwin():
    #mainwin.blit(background, (0,0))


def mainMenu():
    global running
    menulive = True
    pygame.mixer.music.play(-1)
    while menulive:
        mainmenuConductor.play()
        mainmenuanim["splashscreen"].blit(mainwin, (0,0))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    pygame.mixer.music.stop()
                    mainLoop()
                    
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                
        pygame.display.update()


def mainLoop():
    global running
    global x
    global y
    global vel
    global width
    global height
    global direction
    global moveleft
    global moveright
    global moveup
    global movedown
    running = True
    pygame.mixer.music.load("track1.ogg")
    pygame.mixer.music.play(-1)
    while running:
        mainwin.blit(background, (0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == KEYDOWN: # KEYDOWN detects if a key is being pressed and is held down
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    
                if event.key == K_LEFT or event.key == K_a:
                    moveleft = True
                    moveright = False
                    if not moveup and not movedown:
                        direction = "left"
                elif event.key == K_RIGHT or event.key == K_d:
                    moveleft = False
                    moveright = True
                    if not moveup and not movedown:
                        direction = "right"
                elif event.key == K_UP or event.key == K_w:
                    moveup = True
                    movedown = False
                    if not moveleft and not moveright:
                        direction = "up"
                elif event.key == K_DOWN or event.key == K_s:
                    moveup = False
                    movedown = True
                    if not moveleft and not moveright:
                        direction = "down"
    # The KEYUP event means the user has stopped pressing the key, this is important as it makes movement much more fluid -> see documentation
            elif event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_a:
                    moveleft = False
                    if moveup:
                        direction = "up"
                    if movedown:
                        direction = "down"
                elif event.key == K_RIGHT or event.key == K_d:
                    moveright = False
                    if moveup:
                        direction = "up"
                    if movedown:
                        direction = "down"
                elif event.key == K_UP or event.key == K_w:
                    moveup = False
                    if moveleft:
                        direction = "left"
                    if moveright:
                        direction = "right"
                elif event.key == K_DOWN or event.key == K_s:
                    movedown = False
                    if moveleft:
                        direction = "left"
                    if moveright:
                        direction = "right"
        if moveleft or moveright or moveup or movedown:
            moveConductor.play()
            # draws animations for each of the directions
            if direction == "left":
                charanim["walkleft"].blit(mainwin, (x, y))
            elif direction == "right":
                charanim["walkright"].blit(mainwin, (x, y))
            elif direction == "up":
                charanim["walkup"].blit(mainwin, (x, y))
            elif direction == "down":
                charanim["walkdown"].blit(mainwin, (x, y))

            # moving the physicial character
            if moveleft and x > 0:
                x -= vel
            if moveright and x < (WINDOWWIDTH - 64):
                x += vel
            if moveup and y > 0:
                y -= vel
            if movedown and y < (WINDOWHEIGHT - 64):
                y += vel
        else:
            moveConductor.stop()
            if direction == "left":
                mainwin.blit(pygame.image.load("sprites/left.png"), (x, y))
            elif direction == "right":
                mainwin.blit(pygame.image.load("sprites/right.png"), (x, y))
            elif direction == "up":
                mainwin.blit(pygame.image.load("sprites/up.png"), (x, y))
            elif direction == "down":
                mainwin.blit(pygame.image.load("sprites/down.png"), (x, y))
     
        pygame.display.update()

mainMenu()

pygame.quit()
