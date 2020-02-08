import pygame
from pygame.locals import *
import sys
import pyganim  # used for animations
import random

pygame.init()
pygame.mixer.init()
pygame.font.init()

clock = pygame.time.Clock()

running = True

WINDOWWIDTH = 1600
WINDOWHEIGHT = 900

mainwin = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption("2084 - REPEL THE HORDE!")

background = pygame.image.load('sprites/background1.png')
leftidle = pygame.image.load("sprites/left.png")
rightidle = pygame.image.load("sprites/right.png")
upidle = pygame.image.load("sprites/up.png")
downidle = pygame.image.load("sprites/down.png")

charanim = {"walkleft": pyganim.PygAnimation([("sprites/left2.png", 100), ("sprites/left.png", 100), ("sprites/left3"
                                                                                                      ".png", 100),
                                              ("sprites/left.png", 10)]),
            "walkright": pyganim.PygAnimation(\
                [("sprites/right2.png", 100), ("sprites/right.png", 100), ("sprites/right3.png", 100),
                 ("sprites/right.png", 10)]), "walkup": pyganim.PygAnimation(
        [("sprites/up2.png", 100), ("sprites/up.png", 100), ("sprites/up3.png", 100), ("sprites/up.png", 10)]),
            "walkdown": pyganim.PygAnimation(
                [("sprites/down2.png", 100), ("sprites/down.png", 100), ("sprites/down3.png", 100),
                 ("sprites/down.png", 10)])}
moveConductor = pyganim.PygConductor(charanim)

demonanim = {"walkleft": pyganim.PygAnimation(
    [("sprites/demonsprites/demon1left2.png", 100), ("sprites/demonsprites/demon1left3.png", 100),
     ("sprites/demonsprites/demon1left4.png", 100), ("sprites/demonsprites/demon1left5.png", 100),
     ("sprites/demonsprites/demon1left6.png", 100), ("sprites/demonsprites/demon1left7.png", 100)])}
demonanim["walkright"] = demonanim["walkleft"].getCopy()
demonanim["walkright"].flip(True, False)
demonanim["walkright"].makeTransformsPermanent()
demonanimConductor = pyganim.PygConductor(demonanim)

mainmenuanim = {"splashscreen": pyganim.PygAnimation(
    [("sprites/menusprites/splash1.png", 500), ("sprites/menusprites/splash2.png", 500)])}
mainmenuConductor = pyganim.PygConductor(mainmenuanim)

endscreen = {"endscreen": pyganim.PygAnimation(
    [("sprites/menusprites/deadscreen1.png", 500), ("sprites/menusprites/deadscreen2.png", 500)])}
endscreenConductor = pyganim.PygConductor(endscreen)

winscreen = {"winscreen": pyganim.PygAnimation(
    [("sprites/menusprites/winscreen1.png", 500), ("sprites/menusprites/winscreen2.png", 500)])}
winscreenConductor = pyganim.PygConductor(winscreen)

muzzleflashanim = {"fire": pyganim.PygAnimation(
    [("sprites/muzzleflash.png", 100), ("sprites/muzzleflash2.png", 100), ("sprites/muzzleflash3.png", 100),
     ("sprites/muzzleflash4.png", 100)])}
muzzleflashanim["fireleft"] = muzzleflashanim["fire"].getCopy()
muzzleflashanim["fireleft"].flip(True, False)
muzzleflashanim["fireleft"].makeTransformsPermanent()
muzzleflashConductor = pyganim.PygConductor(muzzleflashanim)

fireanim = {"fireanim": pyganim.PygAnimation([("sprites/firesprites/fireanim1.png", 100), ("sprites/firesprites"
                                                                                           "/fireanim2.png", 100),
                                              ("sprites/firesprites/fireanim3.png", 100),
                                              ("sprites/firesprites/fireanim4.png", 100),
                                              ("sprites/firesprites/fireanim5.png", 100),
                                              ("sprites/firesprites/fireanim6.png", 100),
                                              ("sprites/firesprites/fireanim7.png", 100),
                                              ("sprites/firesprites/fireanim8.png", 100),
                                              ("sprites/firesprites/fireanim9.png", 100)])}
fireanimConductor = pyganim.PygConductor(fireanim)


def main_menu(yeet, ttime):
    vcrfont = pygame.font.SysFont('VCR OSD Mono', 30)
    text = vcrfont.render((f'TIME TAKEN: {ttime} SECONDS'), False, (0, 0, 0))
    if yeet == 1:
        pygame.mixer.music.load("music/track2.ogg")
        pygame.mixer.music.play(1)
        while 2 == 2:
            endscreenConductor.play()
            endscreen["endscreen"].blit(mainwin, (0, 0))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        pygame.mixer.music.stop()
                        main_loop()

                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()

    elif yeet == 2:
        pygame.mixer.music.load("music/track3.ogg")
        pygame.mixer.music.play(1)
        while 2 == 2:
            winscreenConductor.play()
            winscreen["winscreen"].blit(mainwin, (0, 0))
            mainwin.blit(text, (16, 16))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        pygame.mixer.music.stop()
                        main_loop()

                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()
    else:
        pygame.mixer.music.load("music/track1.ogg")
        pygame.mixer.music.play(-1)
        while 2 == 2:
            mainmenuConductor.play()
            mainmenuanim["splashscreen"].blit(mainwin, (0, 0))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        main_loop()

                if event.type == pygame.QUIT:
                    pygame.quit()

            pygame.display.update()


def main_loop():
    global running
    starttime = pygame.time.get_ticks()
    print(starttime)
    running = True
    char1 = Character()
    demon_list = []
    # for demon in range(5):
    for demon in range(random.randint(5, 15)):
        demon = Demon()
        demon_list.append(demon)
    prop_list = []
    for prop in range(16):
        prop = PropRock()
        prop_list.append(prop)
    pygame.mixer.music.load("music/track0.ogg")
    pygame.mixer.music.play(-1)

    while running and len(demon_list) > 0:
        print(len(demon_list))
        mainwin.blit(background, (0, 0))
        for event in pygame.event.get():
            char1.get_key(event)
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                running = False
                pygame.quit()

        all_rocks = [i.random_size() for i in prop_list]
        all_demons_patrol = [i.patrol() for i in demon_list]
        all_demons_anim = [i.anim() for i in demon_list]
        all_demon_collide = [i.check_collide(char1) for i in demon_list]
        all_demon_shot = [i.check_shot(char1, demon_list) for i in demon_list]
        char1.anim_and_move()
        char1.shoot()
        clock.tick(30)

        pygame.display.update()

    endtime = pygame.time.get_ticks()
    print("You Win!")
    print(endtime - starttime)
    ttime = ((endtime - starttime) / 1000)
    main_menu(yeet=2, ttime=ttime)


class Character:

    def __init__(self):
        self.x = (WINDOWWIDTH * 0.5)
        self.y = (WINDOWHEIGHT * 0.5)
        self.vel = 10
        self.width = 64
        self.height = 64
        self.moveleft = False
        self.moveright = False
        self.moveup = False
        self.movedown = False
        self.direction = 'left'
        self.shooting = False

    def shoot(self):
        if self.shooting:
            print("Shot my gun!")

    def anim_and_move(self):
        # print("animate and move char")
        if self.shooting:
            muzzleflashConductor.play()
            if self.direction == "right":
                muzzleflashanim["fire"].blit(mainwin, (self.x + 64, self.y + 28))
            elif self.direction == "left":
                muzzleflashanim["fireleft"].blit(mainwin, (self.x - 8, self.y + 28))
                # print("Shooting left!")
            elif self.direction == "up":
                print("Shooting up!")
            elif self.direction == "down":
                print("Shooting down!")
            else:
                muzzleflashConductor.stop()

        if self.moveleft or self.moveright or self.moveup or self.movedown:
            moveConductor.play()

            # draws animations for each of the directions
            if self.direction == "left":
                charanim["walkleft"].blit(mainwin, (self.x, self.y))
            elif self.direction == "right":
                charanim["walkright"].blit(mainwin, (self.x, self.y))
            elif self.direction == "up":
                charanim["walkup"].blit(mainwin, (self.x, self.y))
            elif self.direction == "down":
                charanim["walkdown"].blit(mainwin, (self.x, self.y))

            # moving the physicial character
            if self.moveleft and self.x > 0:
                self.x -= self.vel
            if self.moveright and self.x < (WINDOWWIDTH - 64):
                self.x += self.vel
            if self.moveup and self.y > 0:
                self.y -= self.vel
            if self.movedown and self.y < (WINDOWHEIGHT - 64):
                self.y += self.vel
        else:
            moveConductor.stop()
            if self.direction == "left":
                mainwin.blit(pygame.image.load("sprites/left.png"), (self.x, self.y))
            elif self.direction == "right":
                mainwin.blit(pygame.image.load("sprites/right.png"), (self.x, self.y))
            elif self.direction == "up":
                mainwin.blit(pygame.image.load("sprites/up.png"), (self.x, self.y))
            elif self.direction == "down":
                mainwin.blit(pygame.image.load("sprites/down.png"), (self.x, self.y))

    def get_key(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                self.moveleft = True
                self.moveright = False
                if not self.moveup and not self.movedown:
                    self.direction = "left"
            elif event.key == K_RIGHT or event.key == K_d:
                self.moveleft = False
                self.moveright = True
                if not self.moveup and not self.movedown:
                    self.direction = "right"
            elif event.key == K_UP or event.key == K_w:
                self.moveup = True
                self.movedown = False
                if not self.moveleft and not self.moveright:
                    self.direction = "up"
            elif event.key == K_DOWN or event.key == K_s:
                self.moveup = False
                self.movedown = True
                if not self.moveleft and not self.moveright:
                    self.direction = "down"
            if event.key == K_SPACE:
                self.shooting = True
                # self.shoot()

        elif event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_a:
                self.moveleft = False
                if self.moveup:
                    self.direction = "up"
                if self.movedown:
                    self.direction = "down"
            elif event.key == K_RIGHT or event.key == K_d:
                self.moveright = False
                if self.moveup:
                    self.direction = "up"
                if self.movedown:
                    self.direction = "down"
            elif event.key == K_UP or event.key == K_w:
                self.moveup = False
                if self.moveleft:
                    self.direction = "left"
                if self.moveright:
                    self.direction = "right"
            elif event.key == K_DOWN or event.key == K_s:
                self.movedown = False
                if self.moveleft:
                    self.direction = "left"
                if self.moveright:
                    self.direction = "right"
            if event.key == K_SPACE:
                self.shooting = False

            pygame.display.update()


class Demon:

    def __init__(self):
        self.x = random.randint(0, WINDOWWIDTH - 256)
        self.y = random.randint(0, WINDOWHEIGHT - 256)
        self.vel = 15
        self.width = 64
        self.height = 64
        self.moveleft = False
        self.moveright = False
        self.moveup = False
        self.movedown = False
        self.direction = 'right'
        self.shot = False

    def death(self):
        if self.shot:
            print("DEMON SHOT!!")

    def patrol(self):
        if self.direction == "left" and self.x >= 0:
            self.moveleft = True
            self.moveright = False
            self.x -= self.vel
        elif self.direction == "right" and self.x <= (WINDOWWIDTH - 64):
            self.moveleft = False
            self.moveright = True
            self.x += self.vel
        if self.x >= (WINDOWWIDTH - 64):
            self.direction = "left"
        if self.x <= 0:
            self.direction = "right"

    def anim(self):
        if self.moveleft or self.moveright or self.moveup or self.movedown:
            demonanimConductor.play()

            # draws animations for each of the directions
            if self.direction == "left":
                demonanim["walkleft"].blit(mainwin, (self.x, self.y))
            elif self.direction == "right":
                demonanim["walkright"].blit(mainwin, (self.x, self.y))
            elif self.direction == "up":
                # demonanim["walkup"].blit(mainwin, (self.x, self.y))
                print("Demon walking up.")
            elif self.direction == "down":
                # demonanim["walkdown"].blit(mainwin, (self.x, self.y))
                print("Demon walking down.")
        else:
            demonanimConductor.stop()
            if self.direction == "left":
                mainwin.blit(pygame.image.load("sprites/demonsprites/demon1left1.png"), (self.x, self.y))
            elif self.direction == "right":
                mainwin.blit(pygame.image.load("sprites/demonsprites/demon1right1.png"), (self.x, self.y))
            elif self.direction == "up":
                # mainwin.blit(pygame.image.load("sprites/demonsprites/demon1up1.png"), (self.x, self.y))
                pass
            elif self.direction == "down":
                # mainwin.blit(pygame.image.load("sprites/demonsprites/demon1down1.png"), (self.x, self.y))
                pass

    def check_collide(self, character):
        if character.x == self.x and character.y == self.y:
            mainwin.blit(pygame.image.load("sprites/menusprites/deadscreen0.png"), (0, 0))
            main_menu(yeet=1, ttime=0)
            print("collision - same x same y")
        if (character.x < self.x) and ((character.x + 64) > self.x) and (character.y < self.y) and (
                (character.y + 64) > self.y):
            mainwin.blit(pygame.image.load("sprites/menusprites/deadscreen0.png"), (0, 0))
            main_menu(yeet=1, ttime=0)
            print("collision - character's RIGHT or BOTTOM")
        if (self.x < character.x) and ((self.x + 64) > character.x) and (self.y < character.y) and (
                (self.y + 64) > character.y):
            mainwin.blit(pygame.image.load("sprites/menusprites/deadscreen0.png"), (0, 0))
            main_menu(yeet=1, ttime=0)

    def check_shot(self, character, demon_list):
        if character.shooting:
            fireanimConductor.play()
            if character.direction == "left" and (character.x > self.x) and (character.y < (self.y + 64)) and (
                    (character.y + 64) > self.y):
                print("SHOT character on the right")
                fireanim["fireanim"].blit(mainwin, (self.x, self.y))
                demon_list.remove(self)
            if character.direction == "right" and (character.x < self.x) and (character.y < (self.y + 64)) and (
                    (character.y + 64) > self.y):
                print("SHOT character on the left")
                fireanim["fireanim"].blit(mainwin, (self.x, self.y))
                demon_list.remove(self)
            # Shooting up
            if character.direction == "up" and (character.y > self.y) and (character.x < (self.x + 64)) and (
                    (character.x + 64) > self.x):
                print("SHOT character UP")
                fireanim["fireanim"].blit(mainwin, (self.x, self.y))
                demon_list.remove(self)
            # Shooting Down
            if character.direction == "down" and (character.y < self.y) and (character.x < (self.x + 64)) and (
                    (character.x + 64) > self.x):
                print("SHOT character DOWN")
                fireanim["fireanim"].blit(mainwin, (self.x, self.y))
                demon_list.remove(self)


class PropRock:

    def __init__(self):
        self.x = random.randint(0, WINDOWWIDTH - 64)
        self.y = random.randint(0, WINDOWHEIGHT - 64)
        # self.sizenum = random.randint(0, 2)
        self.lock = False
        self.sizer = []

    def random_size(self):
        if not self.lock:
            self.sizer = random.randint(0, 2)
            self.lock = True
        else:
            if self.sizer == 0:
                self.spawn32()
            elif self.sizer == 1:
                self.spawn128()
            else:
                self.spawn64()

    def spawn64(self):
        mainwin.blit(pygame.image.load("sprites/envirosprites/ROCK64.png"), (self.x, self.y))

    def spawn128(self):
        mainwin.blit(pygame.image.load("sprites/envirosprites/ROCK128.png"), (self.x, self.y))

    def spawn32(self):
        mainwin.blit(pygame.image.load("sprites/envirosprites/ROCK32.png"), (self.x, self.y))


main_menu(yeet=0, ttime=0)

pygame.quit()
