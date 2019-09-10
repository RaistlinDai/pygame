'''
Created on Sep 04, 2019

@author: ftd
'''

import pygame
from src.main.api.com.ftd.wow.character.ICharacter import ICharacter
from src.main.api.com.ftd.wow.profession.IProfession import IProfession
from src.main.impl.com.ftd.wow.profession.Profession_Enum import Profession_Enum

class Character (ICharacter):
    '''
    
    '''
    
    def __init__(self, prof, pos_x, pos_y, size_w, size_h):
        
        # position
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        
        # size
        self.__size_w = size_w
        self.__size_h = size_h
        
        # profession
        if isinstance(prof, Profession_Enum):
            self.__prof = prof.value()
        
        # images
        self.__images = []
        self.load_profession_images()
        
    
    def load_profession_images(self):
        # load images into pygame
        temp_images = self.__prof.get_images()
        for img in temp_images:
            convert_image = pygame.image.load(img).convert_alpha()
            convert_image = pygame.transform.scale(convert_image, (self.__size_w, self.__size_h))
            self.__images.append(convert_image)
    
        
    def show_stand_image(self):
        return self.__images[0]
    
    
    def get_character_properties(self):
        return (0, 0, self.__size_w, self.__size_h)   
    
    
    def get_position(self):
        return (self.__pos_x, self.__pos_y)