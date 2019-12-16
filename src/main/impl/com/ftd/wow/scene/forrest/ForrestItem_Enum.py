'''
Created on Dec 16, 2019

@author: ftd
'''

from enum import Enum, unique
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant


@unique
class ForrestItem_Enum(Enum):
    '''
    classdocs
    @attention: the value structure: scene constructor
    '''
    
    Forrest_Foreground_Trees = Materials_Constant.foreground_Forrest_tree