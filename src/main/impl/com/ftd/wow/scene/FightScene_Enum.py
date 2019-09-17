'''
Created on Sep 13, 2019

@author: ftd
'''
from enum import Enum, unique
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant


@unique
class FightScene_Enum(Enum):
    '''
    classdocs
    @attention: the value structure: scene constructor
    '''
    
    MC_BOSS_10 = Materials_Constant.background_Molten_Core_filename