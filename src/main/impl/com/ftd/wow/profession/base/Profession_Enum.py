'''
Created on Sep 10, 2019

@author: ftd
'''
from enum import Enum, unique
from src.main.impl.com.ftd.wow.profession.Rogue import Rogue
from src.main.impl.com.ftd.wow.profession.Warrior import Warrior


@unique
class Profession_Enum(Enum):
    '''
    classdocs
    @attention: the value structure: profession constructor
    '''

    PROF_WARROIR = Warrior
    PROF_ROGUE = Rogue