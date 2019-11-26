'''
Created on Nov 25, 2019

@author: ftd
'''

from enum import Enum, unique
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant


@unique
class ForrestScene_Enum(Enum):
    '''
    classdocs
    @attention: the value structure: scene constructor
    '''
    
    Forrest_Background_Corridors = Materials_Constant.background_Forrest_back_corridor
    Forrest_Background_Rooms = Materials_Constant.background_Forrest_back_room
    Forrest_Foreground_Trees = Materials_Constant.background_Forrest_fore