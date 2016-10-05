import pygame
from pygame.locals import *
from pokemon_class import Pokemon

import pokemon_class

pygame.init()

clock = pygame.time.Clock()

display = pygame.display.set_mode((999,666))

screen = display

assets = {}

menu = 'main'

def asset(path):
    try:
        return assets[path]
    except KeyError:
        assets[path] = pygame.image.load(path).convert_alpha()
        return assets[path]

frame = 0

do_quit = False

def upd():
    global frame, do_quit
    frame += 1
    for event in pygame.event.get():
        if event.type == QUIT:
            do_quit = True
    pygame.display.update()
    clock.tick(60)

while 1:
    if frame < 200:
        screen.fill((255, 255, 255))
        screen.blit(asset('assets/textures/splash.png'), (frame*20 - 999 if frame < 50 else (0 if frame < 150 else frame*20-3000),0))
        upd()
        if do_quit: break
        continue
    
    if menu == 'main':
        screen.blit(asset('assets/textures/main_bg.jpg'), (0,0))
        upd()
        if do_quit: break
        continue
