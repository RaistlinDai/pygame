'''
Created on Aug 27, 2019

@author: ftd
'''
import pygame
from pygame.locals import *
from sys import exit

# initialize pygame for hardware
pygame.init()

# create a window
screen = pygame.display.set_mode((740, 370), 0, 32)
# set window title
pygame.display.set_caption("Hello, World!")

background_image_filename = 'main\\resource\\com\\ftd\\wow\\pic\\wow-classic-740x370.jpg'
mouse_image_filename = 'main\\resource\\com\\ftd\\wow\\pic\\cursor.png'
character_image_filename = 'main\\resource\\com\\ftd\\wow\\pic\\warlock.png'
background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
character = pygame.image.load(character_image_filename).convert_alpha()

arr_x, arr_y = 0, 0
move_x, move_y = 0, 0

# main loop
while True:

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
        
        arr_x += move_x
        arr_y += move_y
        
    # render the background
    screen.blit(background, (0, 0))

    # get the cursor position
    x, y = pygame.mouse.get_pos()
    # calculate the cursor left-top position
    x-= mouse_cursor.get_width() / 2
    y-= mouse_cursor.get_height() / 2
    # render the cursor
    screen.blit(mouse_cursor, (x, y))
    
    # render the character
    screen.blit(character, (arr_x, arr_y))

    # render the screen
    pygame.display.update()
    
    