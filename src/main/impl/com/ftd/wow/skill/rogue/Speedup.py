'''
Created on Sep 10, 2019

@author: ftd
'''
from src.main.api.com.ftd.wow.skill.ISkill import ISkill
import pygame
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant

class Speedup(ISkill):
    '''
    
    '''
    
    
    def __init__(self):
        super().__init__('Speedup', pygame.image.load(Materials_Constant.rogue_speedup_image_filename).convert_alpha(),\
                         pygame.image.load(Materials_Constant.rogue_speedup_select_image_filename).convert_alpha(), \
                         pygame.image.load(Materials_Constant.rogue_speedup_inactive_image_filename).convert_alpha(), \
                         pygame.image.load(Materials_Constant.action_effect_vertical_cut_image_filename).convert_alpha())
