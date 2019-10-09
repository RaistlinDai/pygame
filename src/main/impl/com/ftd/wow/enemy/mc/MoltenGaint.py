'''
Created on Sep 04, 2019

@author: ftd
'''

from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant
from src.main.api.com.ftd.wow.enemy.IEnemy import IEnemy
from src.main.impl.com.ftd.wow.skill.enemy.moltenGaint.MoltenGaint_Skill_Enum import MoltenGaint_Skill_Enum

class MoltenGaint (IEnemy):
    '''
    
    '''
    
    
    def __init__(self):
        super().__init__(Materials_Constant.enemy_moltengaint_image_filename, MoltenGaint_Skill_Enum, [50, 10, 10, 1, 4, 3, 1.2])