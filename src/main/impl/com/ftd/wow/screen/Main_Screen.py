'''
Created on Aug 27, 2019

@author: ftd
'''
import pygame
from pygame.locals import *
from sys import exit
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant
from src.main.impl.com.ftd.wow.button.Horde_Button import Horde_Button
import time; 
from src.main.impl.com.ftd.wow.scene.Scene_Login import Scene_Login
from src.main.impl.com.ftd.wow.character.Character import Character
from src.main.impl.com.ftd.wow.enemy.boss.Ragnaros import Ragnaros
from src.main.impl.com.ftd.wow.profession.Profession_Enum import Profession_Enum
from src.main.impl.com.ftd.wow.util.Image_Util import Image_Util

class Main_Screen(object):
    '''
    
    '''
    
    def __init__(self, width=640, height=480):
        self._width = width
        self._height = height
        
        # initialize pygame for hardware
        pygame.init()
        # create a window
        self._screen = pygame.display.set_mode((self._width, self._height), 0, 32)
        # set window title
        pygame.display.set_caption("Hello, World!")
        
        # screen background
        self._background = Scene_Login(self._width, self._height)
        self._background_prop = (0, 0, self._width, self._height)
        
    
    def execute(self):
        
        # load image
        mouse_cursor = pygame.image.load(Materials_Constant.mouse_image_filename).convert_alpha()
        
        # background
        scene_MC = pygame.image.load(Materials_Constant.background_Molten_Core_filename).convert()
        # bottom bar
        bottom_bar = pygame.image.load(Materials_Constant.bottom_bar_image_filename).convert_alpha()
        # character
        character_rogue = Character(Profession_Enum.PROF_ROGUE)
        character_h = Image_Util.calculate_character_height_by_screen_size(self._height)
        character_w = Image_Util.calculate_character_width_by_height(character_rogue.get_stand_image(), character_h)
        character_rogue.resize_character_images(950, 420, character_w, character_h)
        # enemy
        cahracter_ragnaros = Ragnaros(70,70,550,550)
        
        temp_scene = self._background.show_background()
        
        # horde button
        horde_start_button = Horde_Button(200, 100, 200, 200)
        is_horde_button_click = False
        horde_button_click_timer = 0
                
        char_x, char_y = 0, 50
        move_x, move_y = 0, 0
        
        # main loop
        while True:
            # clocker
            current_timer = time.time()*1000.0
            
            # render the background
            self._screen.blit(temp_scene, (0,0), self._background_prop)
            
            # render the button & determine the background
            if (not is_horde_button_click):
                if (not horde_start_button.is_over()):
                    self._screen.blit(horde_start_button.show_button(), horde_start_button.get_position())
                else:
                    self._screen.blit(horde_start_button.show_button_cover(), horde_start_button.get_position())
            elif (is_horde_button_click and horde_button_click_timer > 0 and current_timer - horde_button_click_timer < 2000):
                self._screen.blit(horde_start_button.show_button_click(), horde_start_button.get_position())
            elif (is_horde_button_click):
                # re-load the background
                temp_scene = scene_MC
                # render the bottom bar
                self._screen.blit(bottom_bar, (0, 470), (0, 0, self._width, 250))
                # render the character
                self._screen.blit(character_rogue.get_stand_image(), character_rogue.get_position(), character_rogue.get_position_and_size())
                # render the skill bar
                idx = 0
                for char_skill_image in character_rogue.get_active_skills():
                    temp_pos_x = 800 + idx * 100
                    idx = idx + 1
                    self._screen.blit(char_skill_image, (temp_pos_x, 600), (0, 0, 70, 70))
                    
                # render the enemy
                self._screen.blit(cahracter_ragnaros.get_stand_image(), cahracter_ragnaros.get_position(), cahracter_ragnaros.get_position_and_size())
            
            #==========================================#
            #               Event handler              #
            #==========================================#
            for event in pygame.event.get():
                # leave event
                if event.type == QUIT:
                    pygame.quit()
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
            pressed_mouse = pygame.mouse.get_pressed()
        
            char_x += move_x
            char_y += move_y
            
            if pressed_mouse[0]:
                # horde button click
                if (horde_start_button.is_over()):
                    is_horde_button_click = True
                    horde_button_click_timer = time.time()*1000.0
                    
            # get the cursor position
            x, y = pygame.mouse.get_pos()
            # calculate the cursor left-top position
            x-= mouse_cursor.get_width() / 2
            y-= mouse_cursor.get_height() / 2
            # render the cursor
            self._screen.blit(mouse_cursor, (x, y))
            
            # clipping in middle
            #screen.set_clip(0, 50, 770, 380)
                
            # render the screen
            pygame.display.update()