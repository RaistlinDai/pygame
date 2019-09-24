'''
Created on Sep 23, 2019

@author: ftd
'''

import pygame
from src.main.api.com.ftd.wow.character.ICharacter import ICharacter
from src.main.impl.com.ftd.wow.enemy.mc.Enemy_MC_Enum import Enemy_MC_Enum
from src.main.api.com.ftd.wow.enemy.IEnemy import IEnemy

class CharacterAgainst (ICharacter):
    '''
    
    '''
    
    def __init__(self, name, enemy_type):
        
        # super class constructor
        super().__init__()
        # character name
        self.__character_name = name
        # character images
        self.__enemy_images = []

        # profession
        self.__enemy_type = None
        if enemy_type and isinstance(enemy_type, IEnemy):
            self.__enemy_type = enemy_type
        
        # images
        self.load_enemy_images()
        
    
    def load_enemy_images(self):
        if not self.__enemy_type:
            return
        # load profession images into pygame
        temp_images = self.__enemy_type.get_images()
        for img in temp_images:
            self.__enemy_images.append(img)
    
        
    def get_stand_image(self):
        return self.__enemy_images[0]
    
    
    def get_stand_select_image(self):
        return self.__enemy_images[1]
    
    
    def resize_character_images(self, size_w, size_h):            
        idx1 = 0
        # retrieve profession image rage
        rate = self.get_character_enemy_type_rate()
        for img in self.__enemy_images:
            self.__enemy_images[idx1] = pygame.transform.scale(img, (int(size_w*rate), int(size_h*rate)))
            idx1 = idx1 + 1
            
            
    def get_character_enemy_type_rate(self):
        # retrieve profession image rage
        rate = 1
        for enemy_type in Enemy_MC_Enum:
            if enemy_type.value[0] == self.__enemy_type.__class__ :
                rate = enemy_type.value[1]
        return rate
    
    
    def get_character_name(self):
        return self.__character_name