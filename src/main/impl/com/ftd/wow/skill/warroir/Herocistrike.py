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
        skill_images = [pygame.image.load(Materials_Constant.warrior_herocistrike_image_filename).convert_alpha(),\
                        pygame.image.load(Materials_Constant.warrior_herocistrike_select_image_filename).convert_alpha(), \
                        pygame.image.load(Materials_Constant.warrior_herocistrike_inactive_image_filename).convert_alpha(), \
                        pygame.image.load(Materials_Constant.action_effect_vertical_cut_image_filename).convert_alpha()]
        
        #0: skill_damage_range;
        #1: skill_damage_rate;
        #2: skill_hit_rate;
        #3: skill_setup;
        #4: skill_boot;
        #5: skill_range;
        #6: skill_extention_value;
        #7: skill_target;  0-self;1-target
        #8: skill_special_effects[];
        skill_properties = [super().MIDDLE_DAMAGE, \
                            100, \
                            90, \
                            0, \
                            0, \
                            1, \
                            0, \
                            1, \
                            []]
        
        super().__init__('Herocistrike', skill_images, skill_properties)
    