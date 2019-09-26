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
        super().__init__('Herocistrike', pygame.image.load(Materials_Constant.warrior_herocistrike_image_filename).convert_alpha(),\
                         pygame.image.load(Materials_Constant.warrior_herocistrike_select_image_filename).convert_alpha(), \
                         pygame.image.load(Materials_Constant.warrior_herocistrike_inactive_image_filename).convert_alpha(), \
                         pygame.image.load(Materials_Constant.action_effect_vertical_cut_image_filename).convert_alpha())
    