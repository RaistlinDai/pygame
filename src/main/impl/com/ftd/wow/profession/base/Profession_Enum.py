'''
Created on Sep 10, 2019

@author: ftd
'''
from enum import Enum, unique
from src.main.impl.com.ftd.wow.profession.Rogue import Rogue


@unique
class Profession_Enum(Enum):
    '''
    classdocs
    @attention: the value structure: profession constructor
    '''

    #PROF_WARROIR = None
    PROF_ROGUE = Rogue