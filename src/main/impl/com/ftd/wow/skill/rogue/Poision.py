'''
Created on Sep 10, 2019

@author: ftd
'''
from src.main.api.com.ftd.wow.skill.ISkill import ISkill
import pygame
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant

class Poision(ISkill):
    '''
    
    '''
    
    
    def __init__(self):
        skill_images = [pygame.image.load(Materials_Constant.rogue_poision_image_filename).convert_alpha(),\
                         pygame.image.load(Materials_Constant.rogue_poision_select_image_filename).convert_alpha(), \
                         pygame.image.load(Materials_Constant.rogue_poision_inactive_image_filename).convert_alpha(), \
                         pygame.image.load(Materials_Constant.action_effect_vertical_cut_image_filename).convert_alpha()]
        
        skill_properties = []
        
        super().__init__('Poision', skill_images, skill_properties)
