'''
Created on Aug 27, 2019

@author: ftd
'''
import pygame
from pygame.locals import *
from sys import exit
from src.main.pydev.com.ftd.wow.const.materials_constant import materials_constant

# initialize pygame for hardware
pygame.init()

# create a window
screen = pygame.display.set_mode((770, 470), 0, 32)
# set window title
pygame.display.set_caption("Hello, World!")

background = pygame.image.load(materials_constant.background_image_filename).convert()
mouse_cursor = pygame.image.load(materials_constant.mouse_image_filename).convert_alpha()
character = pygame.image.load(materials_constant.character_image_filename).convert_alpha()
chaos_bolt = pygame.image.load(materials_constant.chaos_bolt_image_filename).convert_alpha()

char_x, char_y = 0, 50
move_x, move_y = 0, 0
bolt_x = 0

# main loop
while True:

    # render the background
    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        # leave event
        if event.type == QUIT:
            exit()
            
        # keyboard event
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -1
            elif event.key == K_RIGHT:
                move_x = 1
            elif event.key == K_UP:
                move_y = -1
            elif event.key == K_DOWN:
                move_y = 1
        elif event.type == KEYUP:
            move_x = 0
            move_y = 0
    
    char_x += move_x
    char_y += move_y
    # render the character
    screen.blit(character, (char_x, char_y))

    # get the cursor position
    x, y = pygame.mouse.get_pos()
    # calculate the cursor left-top position
    x-= mouse_cursor.get_width() / 2
    y-= mouse_cursor.get_height() / 2
    # render the cursor
    screen.blit(mouse_cursor, (x, y))
    
    # clipping
    screen.set_clip(0, 50, 770, 380)
    
    # chaos blot
    screen.blit(chaos_bolt, (bolt_x, 100))
    bolt_x += 2
    if bolt_x > 770:
        bolt_x = 0

    # render the screen
    pygame.display.update()
    
    