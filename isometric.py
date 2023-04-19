import pygame, sys, time, random

from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
scr = pygame.display.set_mode((1300, 900))
#display = pygame.Surface((650, 450))
#display = pygame.Surface((1300, 900))
display = pygame.Surface((1300*2, 900*2))

grass_img = pygame.image.load('wall.png').convert_alpha()
grass_img.set_colorkey((0, 0, 0))
#floor_img = pygame.image.load('floors.png').convert_alpha()
floor_img = pygame.image.load('ground.png').convert_alpha()
floor_img.set_colorkey((0, 0, 0))
sel_img = pygame.image.load('sel.png').convert_alpha()
sel_img.set_colorkey((0, 0, 0))
gen = pygame.image.load('gen.png')

f = open('mp.txt')
map_data = [[int(c) for c in row] for row in f.read().split('\n')]
f.close()
cx,cy = 0,0
while True:
    display.fill((0,0,0))
    #scr.fill((0,0,0))

    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            X = x + 10
            Y = y
            if tile:
                #display.blit(grass_img, ((X-Y)*77,(X+Y)*38.5))#16,8
                display.blit(gen, (((X-Y)*77),((X+Y)*38.5)-100))#16,8
                display.blit(floor_img, (((X-Y)*77),((X+Y)*38.5) +16))
            else:
                display.blit(floor_img, (((X-Y)*77),((X+Y)*38.5) +16))
              

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    scr.blit(pygame.transform.scale(display, scr.get_size()), (0, 0))
    pygame.display.update()
    time.sleep(1)
