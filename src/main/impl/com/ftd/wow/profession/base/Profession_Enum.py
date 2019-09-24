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
    # Enum name = [Profession name, image size rage]
    PROF_WARROIR = [Warrior, 1.3]
    PROF_ROGUE = [Rogue, 1]