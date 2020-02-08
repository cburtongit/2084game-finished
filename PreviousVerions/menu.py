import pygame
from pygame.locals import *
import sys
import time
import pyganim #used for animations

#initialises pygame, was told this was necessary
pygame.init()
#pygame.mixer.init()
#pygame.mixer.music.load('track0.ogg')
#pygame.mixer.music.play()

#mainmenu animations
mainmenuanim = {}
mainmenuanim["splashscreen"] = pyganim.PygAnimation([("sprites/splash1.png", 500), ("sprites/splash2.png", 500)])
mainmenuConductor = pyganim.PygConductor(mainmenuanim)
pygame.mixer.init()
pygame.mixer.music.load('track0.ogg')
#pygame.mixer.music.play()

WINDOWWIDTH = 1600
WINDOWHEIGHT = 900

mainwin = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))# this sets height and width of my window and creates a window.
pygame.display.set_caption("2084 Ver 0.1.0.3")# sets window title

running = True
#menulive = True

def mainMenu():
    menulive = True
    pygame.mixer.music.play(-1)
    while menulive:
        mainmenuConductor.play()
        mainmenuanim["splashscreen"].blit(mainwin, (0,0))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    pygame.quit()
                    running = False
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                
        pygame.display.update()

mainMenu()
while running:  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.update()


pygame.quit()
