'''
Created on Sep 12, 2019

@author: ftd
'''
import pygame
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant
from src.main.impl.com.ftd.wow.util.Image_Util import Image_Util
from src.main.api.com.ftd.wow.character.ICharacter import ICharacter

class Bottom_Bar(object):
    '''
    
    '''
    
    def __init__(self, size_w=None, size_h=None, current_character=None):
        # size
        self.__size_w = 1280
        self.__size_h = 250
        # position
        self.__pos_x = 0
        self.__pos_y = 470
        # current character
        self.__current_character = None
        # active skills
        self.__active_skills = None
        
        if current_character:
            self.__current_character = current_character
            self.__active_skills = self.__current_character.get_active_skills()
        
        # images
        self.__image = pygame.image.load(Materials_Constant.bottom_bar_image_filename).convert_alpha()
        if size_w and size_h:
            self.__size_w = size_w
            self.__size_h = Image_Util.calculate_bottom_bar_height_by_screen_size(size_h)
            self.__pos_y = Image_Util.calculate_bottom_bar_positionY_by_screen_size(size_h)
            self.__image = pygame.transform.scale(self.__image, (self.__size_w, self.__size_h))
            
    
    def render_image(self, screen_ins, screen_w, screen_h):
        
        if screen_w and screen_h:
            self.__size_w = screen_w
            self.__size_h = Image_Util.calculate_bottom_bar_height_by_screen_size(screen_h)
            self.__pos_y = Image_Util.calculate_bottom_bar_positionY_by_screen_size(screen_h)
            self.__image = pygame.transform.scale(self.__image, (self.__size_w, self.__size_h))
        
        screen_ins.blit(self.__image, (0, self.__pos_y), (0,0,self.__size_w,self.__size_h))
        self.render_skills(screen_ins)
        
    
    def render_skills(self, screen_ins, character=None):
        
        if character:
            self.__current_character = character
        
        if not self.__current_character or not isinstance(self.__current_character, ICharacter):
            return False, 'Invalid character, no skills load!'
        
        self.__active_skills = self.__current_character.get_active_skills()
        # render the skill bar
        idx = 0
        for char_skill_image in self.__current_character.get_active_skills():
            temp_pos_x = Image_Util.calculate_skill_in_fight_positionX_by_screen_size(self.__size_w, idx)
            temp_pos_y = Image_Util.calculate_skill_in_fight_positionY_by_screen_size(self.__size_h + self.__pos_y)
            temp_size = Image_Util.calculate_skill_in_fight_size_by_screen_size(self.__size_h + self.__pos_y)
            
            char_skill_image = pygame.transform.scale(char_skill_image, (temp_size, temp_size))
            
            idx = idx + 1
            screen_ins.blit(char_skill_image, (temp_pos_x, temp_pos_y), (0, 0, temp_size, temp_size))
            
            
    def set_current_character(self, current_character):
        self.__current_character = current_character
            