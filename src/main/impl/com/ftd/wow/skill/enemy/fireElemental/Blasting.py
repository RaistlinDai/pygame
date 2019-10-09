'''
Created on Oct 09, 2019

@author: ftd
'''
import pygame
from src.main.api.com.ftd.wow.skill.ISkill import ISkill

class Blasting(ISkill):
    '''
    
    '''
    
    
    def __init__(self):
        skill_images = []
        
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
                            120, \
                            90, \
                            0, \
                            0, \
                            1, \
                            0, \
                            1, \
                            []]
        
        super().__init__('Blasting', skill_images, skill_properties)
        