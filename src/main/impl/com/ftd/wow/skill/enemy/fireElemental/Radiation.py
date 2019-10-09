'''
Created on Oct 09, 2019

@author: ftd
'''
from src.main.api.com.ftd.wow.skill.ISkill import ISkill

class Radiation(ISkill):
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
                            90, \
                            95, \
                            0, \
                            1, \
                            2, \
                            0, \
                            1, \
                            []]
        
        super().__init__('Radiation', skill_images, skill_properties)
        