'''
Created on Oct 09, 2019

@author: ftd
'''
import pygame
from src.main.api.com.ftd.wow.skill.ISkill import ISkill
from src.main.impl.com.ftd.wow.skill.SkillEffect import SkillEffect

class Flameshock(ISkill):
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
        temp_skill_effect = SkillEffect(SkillEffect.CONTROL_DIZZY, 0, 0, 1, False)
        skill_properties = [super().LOW_DAMAGE, \
                            70, \
                            80, \
                            0, \
                            0, \
                            1, \
                            0, \
                            1, \
                            [temp_skill_effect]]
        
        super().__init__('Flameshock', skill_images, skill_properties)
        