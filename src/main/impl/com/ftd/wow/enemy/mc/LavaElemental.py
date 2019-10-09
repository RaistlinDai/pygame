'''
Created on Sep 04, 2019

@author: ftd
'''

from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant
from src.main.api.com.ftd.wow.enemy.IEnemy import IEnemy
from src.main.impl.com.ftd.wow.skill.enemy.lavaElemental.LavaElemental_Skill_Enum import LavaElemental_Skill_Enum

class LavaElemental (IEnemy):
    '''
    
    '''
    
    def __init__(self):
        super().__init__(Materials_Constant.enemy_lavaelemental_image_filename, LavaElemental_Skill_Enum, [12, 10, 4, 15, 1, 8, 1.2])

