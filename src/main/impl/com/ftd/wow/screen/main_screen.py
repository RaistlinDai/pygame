'''
Created on Aug 27, 2019

@author: ftd
'''
import pygame
from pygame.locals import *
from sys import exit
from src.main.impl.com.ftd.wow.const.materials_constant import materials_constant
from src.main.impl.com.ftd.wow.button.horde_button import horde_button
from src.main.impl.com.ftd.wow.screen.scene_01 import scene_01
import time; 

class main_screen(object):
    '''
    
    '''
    
    def __init__(self, width=640, height=480):
        self._width = width
        self._height = height
    
    def execute(self):
        # initialize pygame for hardware
        pygame.init()
        
        # create a window
        screen = pygame.display.set_mode((self._width, self._height), 0, 32)
        # set window title
        pygame.display.set_caption("Hello, World!")
        
        background = pygame.image.load(materials_constant.mainframe_image_filename).convert()
        background = pygame.transform.scale(background, (self._width, self._height))
        
        mouse_cursor = pygame.image.load(materials_constant.mouse_image_filename).convert_alpha()
        
        # horde button
        horde_start_button = horde_button(200, 100, 200, 200)
        is_horde_button_click = False
        horde_button_click_timer = 0
        
        character = pygame.image.load(materials_constant.character_image_filename).convert_alpha()
        character = pygame.transform.scale(character, (120, 150))
        
        chaos_bolt = pygame.image.load(materials_constant.chaos_bolt_image_filename).convert_alpha()
        
        char_x, char_y = 0, 50
        move_x, move_y = 0, 0
        
        # Clock obj
        clock = pygame.time.Clock()
        speed = 200
        bolt_x = 0
        bolt_y = 0
        is_filed = False
        
        # main loop
        while True:
        
            # clocker
            time_passed = clock.tick() / 1000.0
            current_timer = time.time()*1000.0
            
            # render the background
            screen.blit(background, (0, 0))
            
            # render the button
            if (not is_horde_button_click):
                if (not horde_start_button.is_over()):
                    screen.blit(horde_start_button.show_button(), horde_start_button.get_position())
                else:
                    screen.blit(horde_start_button.show_button_cover(), horde_start_button.get_position())
            elif (is_horde_button_click and horde_button_click_timer > 0 and current_timer - horde_button_click_timer < 2000):
                screen.blit(horde_start_button.show_button_click(), horde_start_button.get_position())
            elif (is_horde_button_click):
                # re-load the background
                sce01 = scene_01(0, 0, self._width, self._height)
                background = sce01.get_background()
            
            
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
            
            # get the keyboard and mouse click
            pressed_keys = pygame.key.get_pressed()
            pressed_mouse = pygame.mouse.get_pressed()
        
            char_x += move_x
            char_y += move_y
            # render the character
            screen.blit(character, (char_x, char_y))
            
            if pressed_mouse[0]:
                # horde button click
                if (horde_start_button.is_over()):
                    is_horde_button_click = True
                    horde_button_click_timer = time.time()*1000.0
                
                # chaos blot flying
                bolt_x = char_x + 20
                bolt_y = char_y + 10
                is_filed = True
            elif pressed_mouse[2]:
                is_filed = False
                
            if is_filed:
                screen.blit(chaos_bolt, (bolt_x, bolt_y))
                bolt_x += time_passed * speed
                if bolt_x > 770:
                    bolt_x = 0
                    
            # get the cursor position
            x, y = pygame.mouse.get_pos()
            # calculate the cursor left-top position
            x-= mouse_cursor.get_width() / 2
            y-= mouse_cursor.get_height() / 2
            # render the cursor
            screen.blit(mouse_cursor, (x, y))
            
            # clipping in middle
            #screen.set_clip(0, 50, 770, 380)
                
            # render the screen
            pygame.display.update()