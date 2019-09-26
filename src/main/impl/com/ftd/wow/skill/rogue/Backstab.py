'''
Created on Sep 10, 2019

@author: ftd
'''
import pygame
from src.main.api.com.ftd.wow.skill.ISkill import ISkill
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant

class Backstab(ISkill):
    '''
    
    '''
    
    
    def __init__(self):
        super().__init__('Backstab', pygame.image.load(Materials_Constant.rogue_backstab_image_filename).convert_alpha(),\
                         pygame.image.load(Materials_Constant.rogue_backstab_select_image_filename).convert_alpha(), \
                         pygame.image.load(Materials_Constant.rogue_backstab_inactive_image_filename).convert_alpha(), \
                         pygame.image.load(Materials_Constant.action_effect_vertical_cut_image_filename).convert_alpha())
        