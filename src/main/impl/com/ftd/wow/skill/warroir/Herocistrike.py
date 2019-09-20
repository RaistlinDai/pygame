'''
Created on Sep 10, 2019

@author: ftd
'''
import pygame
from src.main.api.com.ftd.wow.skill.ISkill import ISkill
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant

class Herocistrike(ISkill):
    '''
    
    '''
    
    
    def __init__(self):
        # give a name
        self.__name = 'Herocistrike'
        # images
        self.__image = pygame.image.load(Materials_Constant.warrior_herocistrike_image_filename).convert_alpha()
        self.__image_select = pygame.image.load(Materials_Constant.warrior_herocistrike_select_image_filename).convert_alpha()
        self.__image_inactive = pygame.image.load(Materials_Constant.warrior_herocistrike_inactive_image_filename).convert_alpha()
        
    
    def get_skill_image(self):
        return self.__image


    def get_skill_image_select(self):
        return self.__image_select
    
    
    def get_skill_image_inactive(self):
        return self.__image_inactive
    
    
    def get_skill_name(self):
        return self.__name
    