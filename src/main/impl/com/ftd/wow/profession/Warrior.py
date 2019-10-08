'''
Created on Sep 04, 2019

@author: ftd
'''

import pygame
from src.main.api.com.ftd.wow.profession.IProfession import IProfession
from src.main.impl.com.ftd.wow.skill.warroir.Warrior_Skill_Enum import Warrior_Skill_Enum
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant

class Warrior (IProfession):
    '''
    
    '''
    
    def __init__(self):
        super().__init__(Materials_Constant.character_warrior_image_filenames, Warrior_Skill_Enum, \
                         [15, 5, 4, 2, 20, 10, 1.2])
