'''
Created on Jul 14, 2019

@author: ftd
'''
import pygame
from src.main.api.com.ftd.wow.scene.IScene import IScene
from src.main.impl.com.ftd.wow.util.Image_Util import Image_Util

class IFightScene(IScene):
    '''
    
    '''
    
    def __init__(self, scene_image, bottom_bar=None, top_bar=None, size_w=None, size_h=None, active_team=None, current_character=None):
        
        self.__background = None
        # size
        self.__size_w = 1280
        self.__size_h = 720
        
        # character-screen properties
        self.__character_properties = {1:{'position':(50, 420), 'image_size':(0,0,0,0), 'character':None}, 
                                       2:{'position':(150, 420), 'image_size':(0,0,0,0), 'character':None}, 
                                       3:{'position':(250, 420), 'image_size':(0,0,0,0), 'character':None}, 
                                       4:{'position':(350, 420), 'image_size':(0,0,0,0), 'character':None}}
        
        self.__bottom_bar = None
        self.__top_bar = None
        self.__current_character = None
        self.__enemies = []
        self.__active_team = None
        
        # setup the active team and characters
        self.add_active_team(active_team)
        
        # load the scene pictures in order
        self.__background = pygame.image.load(scene_image.value).convert()
        # adjust the scene size
        if (size_w and size_h):
            self.__size_w = size_w
            self.__size_h = size_h
            self.__background = pygame.transform.scale(self.__background, (size_w, size_h))
            
        # load top and bottom
        self.__bottom_bar = bottom_bar 
        self.__top_bar = top_bar
        
        # set the current character
        self.set_current_character(current_character)
    
    
    def render_scene(self, screen_ins, screen_w=None, screen_h=None):
        if (screen_w and screen_h):
            self.__size_w = screen_w
            self.__size_h = screen_h
            self.__background = pygame.transform.scale(self.__background, (screen_w, screen_h))
            
        screen_ins.blit(self.__background, (0,0), (0,0,self.__size_w,self.__size_h))
        
        # render the bottom bar
        self.__bottom_bar.render_image(screen_ins, self.__size_w, self.__size_h)
        
        # render the top bar
        self.__top_bar.render_image(screen_ins, self.__size_w, self.__size_h)
        
        # render the characters
        self.render_characters(screen_ins)
        
        # render the enemies
        
             
    def render_characters(self, screen_ins):             
        # render the character
        if not self.__active_team:
            return
        characters = self.__active_team.get_teammembers()
        
        idx = 0
        for temp_char in characters:
            idx = idx + 1
            if not temp_char:
                continue
            
            # resize character
            calc_h = Image_Util.calculate_character_height_by_screen_size(self.__size_h)
            calc_w = Image_Util.calculate_character_width_by_height(temp_char.get_stand_image(), calc_h)
            temp_char.resize_character_images(calc_w, calc_h)
            
            # re-calculate character position
            (x,y) = Image_Util.calculate_character_position_by_screen_size(self.__size_w, self.__size_h, idx)
            self.__character_properties[idx]['position'] = (x,y)
            self.__character_properties[idx]['image_size'] = (0, 0, calc_w, calc_h)
            
            if self.__current_character and self.__current_character.get_character_name() == temp_char.get_character_name():
                screen_ins.blit(temp_char.get_stand_select_image(), (x,y), (0, 0, calc_w, calc_h))
            else:
                screen_ins.blit(temp_char.get_stand_image(), (x,y), (0, 0, calc_w, calc_h))
            
            
    def add_active_team(self, active_team):
        self.__active_team = active_team
        if self.__active_team:
            idx = 0
            characters = self.__active_team.get_teammembers()
            for temp_char in characters:
                idx = idx + 1
                if temp_char:
                    self.__character_properties[idx]['character'] = temp_char
    
        
    def set_current_character(self, current_character):
        self.__current_character = current_character
        if self.__bottom_bar:
            self.__bottom_bar.set_current_character(self.__current_character)
            
    
    def get_cover_character(self, cursor_x, cursor_y):
        for temp_idx in self.__character_properties:
            temp_char = self.__character_properties[temp_idx]
            (temp_char_x, temp_char_y) = temp_char['position']
            (temp_char_p1, temp_char_p2, temp_char_w, temp_char_h) = temp_char['image_size']
            
            in_x = temp_char_x < cursor_x < temp_char_x + temp_char_w
            in_y = temp_char_y < cursor_y < temp_char_y + temp_char_h
            
            if in_x and in_y:
                print(temp_char['character'].get_character_name())
                
    