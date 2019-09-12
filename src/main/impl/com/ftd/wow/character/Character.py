'''
Created on Sep 04, 2019

@author: ftd
'''

import pygame
from src.main.api.com.ftd.wow.character.ICharacter import ICharacter
from src.main.impl.com.ftd.wow.profession.Profession_Enum import Profession_Enum

class Character (ICharacter):
    '''
    
    '''
    
    def __init__(self, prof, char_pos_x=None, char_pos_y=None, size_w=None, size_h=None):
        
        # super class constructor
        super().__init__()
        # character images
        self.__fight_skills_images = []
        self.__camp_skills_images = []
        self.__profession_images = []
        
        # character position
        self.__character_char_pos_x = char_pos_x
        self.__character_char_pos_y = char_pos_y
        
        # character size
        self.__character_size_w = size_w
        self.__character_size_h = size_h
        
        # profession
        if isinstance(prof, Profession_Enum):
            self.__prof = prof.value()
        
        # images
        self.load_profession_images()
        
        # skills
        self.load_skills_images()
        
    
    def load_profession_images(self):
        # load profession images into pygame
        temp_images = self.__prof.get_images()
        for img in temp_images:
            convert_image = pygame.image.load(img).convert_alpha()
            if (self.__character_size_w and self.__character_size_h):
                convert_image = pygame.transform.scale(convert_image, (self.__character_size_w, self.__character_size_h))
            self.__profession_images.append(convert_image)
            
    
    def load_skills_images(self):
        # load skill images into pygame
        temp_skills = self.__prof.get_skills()
        for skill in temp_skills:
            convert_image = pygame.image.load(skill.get_skill_image()).convert_alpha()
            if (self.__character_size_w and self.__character_size_h):
                convert_image = pygame.transform.scale(convert_image, (self.__character_size_w, self.__character_size_h))
            self.__fight_skills_images.append(convert_image)
    
        
    def get_stand_image(self):
        return self.__profession_images[0]
    
    
    def get_position_and_size(self):
        return (0, 0, self.__character_size_w, self.__character_size_h)
    
    
    def set_position_and_size(self, char_pos_x, char_pos_y, size_w, size_h):
        # position
        self.__character_char_pos_x = char_pos_x
        self.__character_char_pos_y = char_pos_y
        # size
        self.__character_size_w = size_w
        self.__character_size_h = size_h
    
    
    def resize_character_images(self, char_pos_x, char_pos_y, size_w, size_h):
        # position
        if char_pos_x and char_pos_y:
            self.__character_char_pos_x = char_pos_x
            self.__character_char_pos_y = char_pos_y
        # size
        if size_w and size_h:
            self.__character_size_w = size_w
            self.__character_size_h = size_h
            
        idx1 = 0
        for img in self.__profession_images:
            self.__profession_images[idx1] = pygame.transform.scale(img, (self.__character_size_w, self.__character_size_h))
            idx1 = idx1 + 1
        idx2 = 0
        for img in self.__fight_skills_images:
            self.__fight_skills_images[idx2] = pygame.transform.scale(img, (70, 70))
            idx2 = idx2 + 1
    
    
    def get_position(self):
        return (self.__character_char_pos_x, self.__character_char_pos_y)
    
    
    def get_active_skills(self):
        # TODO: need to invoke special character properties later
        return self.__fight_skills_images
        