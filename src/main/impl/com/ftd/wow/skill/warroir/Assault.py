'''
Created on Sep 10, 2019

@author: ftd
'''
import pygame
from src.main.api.com.ftd.wow.skill.ISkill import ISkill
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant

class Assault(ISkill):
    '''
    
    '''
    
    
    def __init__(self):
        # give a name
        self.__name = 'Assault'
        # images
        self.__image = pygame.image.load(Materials_Constant.warrior_assault_image_filename).convert_alpha()
        self.__image_select = pygame.image.load(Materials_Constant.warrior_assault_select_image_filename).convert_alpha()
        self.__image_inactive = pygame.image.load(Materials_Constant.warrior_assault_inactive_image_filename).convert_alpha()
        
    
    def get_skill_image(self):
        return self.__image


    def get_skill_image_select(self):
        return self.__image_select
    
    
    def get_skill_image_inactive(self):
        return self.__image_inactive
    
    
    def get_skill_name(self):
        return self.__name
    