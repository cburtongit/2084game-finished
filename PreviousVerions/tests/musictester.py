# Welcome to 2084 ver 0.0.0.1
# Created by Cameron Burton, with help from the Pygame and Python community!

# importing modules
import pygame

pygame.init()
# this innitialises pygame, was told this was necessary
pygame.mixer.init()
pygame.mixer.music.load("track1enolagay.ogg")
pygame.mixer.music.play(-1)
mainwin = pygame.display.set_mode((1000, 1000))
# this sets height and width of my window and creates a window.
pygame.display.set_caption("2084 Ver 0.0.0.1")
# sets window title

# character creation, these are the definitions of what a drawn character will look like, used later.
x = 100
y = 100
width = 50
height = 100
vel = 5

running = True
while running:
    pygame.time.delay(10) # this is a way to create a "clock" in pygame apparently, I can probably use this to set the speed of animations or actions later
# music test
    for event in pygame.event.get():# pygame programs usually have a main loop, this checks for player input or events such as mouse or keyboard input.
        if event.type == pygame.QUIT:#upon clicking the close window button the game will end the loop thus closing the game as the next line quits the game.
            running = False


    kbinput = pygame.key.get_pressed()# sets up keyboard input NOTE: Pygame's movement engine has the point 0,0 at the TOP left of the window as opposed to the BOTTOM left like on most graphs, so +y would go DOWN rather than up

    if kbinput[pygame.K_LEFT] and x > 0:
        x -= vel
    if kbinput[pygame.K_RIGHT] and x < 1000:
        x += vel
    if kbinput[pygame.K_UP] and y > 0:
        y -= vel
    if kbinput[pygame.K_DOWN] and y < 1000:
        y += vel
        
    mainwin.fill((0,0,0)) # because the movement engine I just made only draws new rectangels, by filling the screen black again it covers them, effectively making it seem as if there is only 1 rectangle and it is moving. Need to redo this once I imlpement a background picture for the level.
    pygame.draw.rect(mainwin, (200, 200, 0), (x, y, width, height))# draws character using previously defined values
    pygame.display.update()# in order for new information to appear on screen, this command updates what is drawn.


pygame.quit()
