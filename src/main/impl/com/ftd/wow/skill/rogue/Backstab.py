'''
Created on Sep 10, 2019

@author: ftd
'''
from src.main.api.com.ftd.wow.skill.ISkill import ISkill
import pygame
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant

class Backstab(ISkill):
    '''
    
    '''
    
    
    def __init__(self, size_w, size_h):
        
        # size
        self.__size_w = size_w
        self.__size_h = size_h
        
        # give a name
        self.__name = 'Backstab'
        
        # images
        self.__image = pygame.image.load(Materials_Constant.rogue_backstab_image_filename).convert_alpha()
        self.__image = pygame.transform.scale(self.__image, (self.__size_w, self.__size_h))
        
    
    def show_skill_image(self):
        return self.__image

    
    def get_skill_name(self):
        return self.__name
    
    
    def get_size(self):
        return (self.__size_w, self.__size_h)
    