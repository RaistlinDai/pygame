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
        super().__init__('Evilatt', pygame.image.load(Materials_Constant.rogue_evilatt_image_filename).convert_alpha(),\
                         pygame.image.load(Materials_Constant.rogue_evilatt_select_image_filename).convert_alpha(), \
                         pygame.image.load(Materials_Constant.rogue_evilatt_inactive_image_filename).convert_alpha(), \
                         pygame.image.load(Materials_Constant.action_effect_vertical_cut_image_filename).convert_alpha())
    