'''
Created on Sep 04, 2019

@author: ftd
'''

from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant
from src.main.api.com.ftd.wow.enemy.IEnemy import IEnemy
from src.main.impl.com.ftd.wow.skill.enemy.volcaicElemental.VolcaicElemental_Skill_Enum import VolcaicElemental_Skill_Enum

class VolcanicElemental (IEnemy):
    '''
    
    '''
    
    def __init__(self):
        super().__init__(Materials_Constant.enemy_volcanicelemental_image_filename, VolcaicElemental_Skill_Enum, [20, 7, 6, 5, 2, 2, 1.2])