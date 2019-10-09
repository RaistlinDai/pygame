'''
Created on Sep 04, 2019

@author: ftd
'''

from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant
from src.main.api.com.ftd.wow.enemy.IEnemy import IEnemy
from src.main.impl.com.ftd.wow.skill.enemy.fireElemental.FireElemental_Skill_Enum import FireElemental_Skill_Enum

class FireElemental (IEnemy):
    '''
    
    '''
    
    def __init__(self):
        super().__init__(Materials_Constant.enemy_fireelemental_image_filename, FireElemental_Skill_Enum, \
                         [16, 12, 6, 11, 30, 15, 1.2])
    