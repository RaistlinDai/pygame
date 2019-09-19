'''
Created on Sep 19, 2019

@author: ftd
'''
from enum import Enum, unique


@unique
class SceneMode_Enum(Enum):
    '''
    classdocs
    @attention: the value structure: scene constructor
    '''
    
    MENU_SCENE = 0
    LOAD_SCENE = 1
    CITY_SCENE = 2
    PREPARE_SCENE = 3
    FIGHT_SCENE = 4