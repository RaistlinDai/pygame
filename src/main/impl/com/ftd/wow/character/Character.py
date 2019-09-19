'''
Created on Sep 04, 2019

@author: ftd
'''

import pygame
from src.main.api.com.ftd.wow.character.ICharacter import ICharacter
from src.main.api.com.ftd.wow.profession.IProfession import IProfession

class Character (ICharacter):
    '''
    
    '''
    
    def __init__(self, name, prof):
        
        # super class constructor
        super().__init__()
        # character name
        self.__character_name = name
        # character images
        self.__fight_skills_images = []
        self.__camp_skills_images = []
        self.__profession_images = []

        # profession
        self.__prof = None
        if prof and isinstance(prof, IProfession):
            self.__prof = prof
        
        # images
        self.load_profession_images()
        
        # skills
        self.load_skills_images()
        
    
    def load_profession_images(self):
        if not self.__prof:
            return
        # load profession images into pygame
        temp_images = self.__prof.get_images()
        for img in temp_images:
            convert_image = pygame.image.load(img).convert_alpha()
            self.__profession_images.append(convert_image)
            
    
    def load_skills_images(self):
        if not self.__prof:
            return
        # load skill images into pygame
        temp_skills = self.__prof.get_skills()
        for skill in temp_skills:
            convert_image = pygame.image.load(skill.get_skill_image()).convert_alpha()
            self.__fight_skills_images.append(convert_image)
    
        
    def get_stand_image(self):
        return self.__profession_images[0]
    
    
    def get_stand_select_image(self):
        return self.__profession_images[1]
    
    
    def resize_character_images(self, size_w, size_h):            
        idx1 = 0
        for img in self.__profession_images:
            self.__profession_images[idx1] = pygame.transform.scale(img, (size_w, size_h))
            idx1 = idx1 + 1
        idx2 = 0
        for img in self.__fight_skills_images:
            self.__fight_skills_images[idx2] = pygame.transform.scale(img, (70, 70))
            idx2 = idx2 + 1
    
    
    def get_character_name(self):
        return self.__character_name
    
    
    def get_active_skills(self):
        # TODO: need to invoke special character properties later
        return self.__fight_skills_images
        