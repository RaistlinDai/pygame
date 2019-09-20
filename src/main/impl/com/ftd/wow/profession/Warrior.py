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
        super().__init__(Materials_Constant.character_warrior_image_filenames, Warrior_Skill_Enum)
        
        # basic properties
        # healthy
        self.__basic_healthy = 15
        # defence
        self.__basic_defence = 7
        # speed
        self.__basic_speed = 3
        # attack
        self.__basic_attack = 5
        # critical
        self.__basic_critical = 2
        # dodge
        self.__basic_dodge = 2
    

    def get_basic_healthy(self):
        return self.__basic_healthy


    def get_basic_defence(self):
        return self.__basic_defence


    def get_basic_speed(self):
        return self.__basic_speed


    def get_basic_attack(self):
        return self.__basic_attack


    def get_basic_critical(self):
        return self.__basic_critical


    def get_basic_dodge(self):
        return self.__basic_dodge
    
    
    def get_basic_skills(self):
        return self.__basic_skills
        
    
    basic_healthy = property(get_basic_healthy, None, None, None)
    basic_defence = property(get_basic_defence, None, None, None)
    basic_speed = property(get_basic_speed, None, None, None)
    basic_attack = property(get_basic_attack, None, None, None)
    basic_critical = property(get_basic_critical, None, None, None)
    basic_dodge = property(get_basic_dodge, None, None, None)
    
