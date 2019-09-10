'''
Created on Sep 04, 2019

@author: ftd
'''

import pygame
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant
from src.main.api.com.ftd.wow.profession.IProfession import IProfession

class Rogue (IProfession):
    '''
    
    '''
    
    def __init__(self):
        # image
        self.__images = []
        self.__images.append(Materials_Constant.character_rogue_image_filename)
        
        # basic properties
        # healthy
        
        # amour
        
        # speed
        
        # strong
        
        # agility
        
        # fight skills
        
        # camping skills
        
        
        
    def get_images(self):
        return self.__images
    
    
    