'''
Created on Sep 10, 2019

@author: ftd
'''
from src.main.api.com.ftd.wow.skill.ISkill import ISkill
import pygame
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant

class Evilatt(ISkill):
    '''
    
    '''
    
    
    def __init__(self):
        # give a name
        self.__name = 'Evilatt'
        # images
        self.__image = Materials_Constant.rogue_evilatt_image_filename
        
    
    def get_skill_image(self):
        return self.__image

    
    def get_skill_name(self):
        return self.__name
    
    
    def get_size(self):
        return (self.__size_w, self.__size_h)
    