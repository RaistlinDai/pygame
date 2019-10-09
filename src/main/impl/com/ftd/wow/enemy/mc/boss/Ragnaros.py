'''
Created on Sep 04, 2019

@author: ftd
'''

from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant
from src.main.api.com.ftd.wow.enemy.IEnemy import IEnemy
from src.main.impl.com.ftd.wow.skill.enemy.ragnaros.Ragnaros_Skill_Enum import Ragnaros_Skill_Enum

class Ragnaros (IEnemy):
    '''
    
    '''
    
    def __init__(self):
        super().__init__(Materials_Constant.boss_ragnaros_image_filename, Ragnaros_Skill_Enum, [100, 12, 8, 10, 5, 5])