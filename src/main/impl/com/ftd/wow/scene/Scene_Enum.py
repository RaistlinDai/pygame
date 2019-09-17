'''
Created on Sep 13, 2019

@author: ftd
'''
from enum import Enum, unique
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant


@unique
class Scene_Enum(Enum):
    '''
    classdocs
    @attention: the value structure: scene constructor
    '''
    
    LOGIN = Materials_Constant.mainframe_image_filename

    MC_BOSS_10 = Materials_Constant.background_Molten_Core_filename