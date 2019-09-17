'''
Created on Sep 13, 2019

@author: ftd
'''
from enum import Enum, unique
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant


@unique
class MenuScene_Enum(Enum):
    '''
    classdocs
    @attention: the value structure: scene constructor
    '''
    
    HORDE_LOGIN = Materials_Constant.mainframe_image_filename
