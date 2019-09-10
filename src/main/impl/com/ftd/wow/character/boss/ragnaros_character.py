'''
Created on Sep 04, 2019

@author: ftd
'''

import pygame
from src.main.impl.com.ftd.wow.const.materials_constant import materials_constant
from src.main.api.com.ftd.wow.character.ICharacter import ICharacter

class ragnaros_character (ICharacter):
    '''
    
    '''
    
    def __init__(self, pos_x, pos_y, size_w, size_h):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__size_w = size_w
        self.__size_h = size_h
        self.__stand_image = pygame.image.load(materials_constant.boss_ragnaros_image_filename).convert_alpha()
        self.__stand_image = pygame.transform.scale(self.__stand_image, (size_w, size_h))
        
    def show_stand_image(self):
        return self.__stand_image
    
    def get_character_properties(self):
        return (0, 0, self.__size_w, self.__size_h)   
    
    def get_position(self):
        return (self.__pos_x, self.__pos_y)