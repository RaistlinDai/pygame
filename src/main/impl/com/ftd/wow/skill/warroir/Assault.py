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
        super().__init__('Assault', pygame.image.load(Materials_Constant.warrior_assault_image_filename).convert_alpha(),\
                         pygame.image.load(Materials_Constant.warrior_assault_select_image_filename).convert_alpha(), \
                         pygame.image.load(Materials_Constant.warrior_assault_inactive_image_filename).convert_alpha(), \
                         pygame.image.load(Materials_Constant.action_effect_strike_image_filename).convert_alpha())
