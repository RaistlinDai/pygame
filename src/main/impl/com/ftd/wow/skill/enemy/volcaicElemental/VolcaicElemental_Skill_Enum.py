'''
Created on Oct 09, 2019

@author: ftd
'''
from enum import Enum, unique
from src.main.impl.com.ftd.wow.skill.enemy.fireElemental.Blasting import Blasting
from src.main.impl.com.ftd.wow.skill.enemy.fireElemental.Flameshock import Flameshock
from src.main.impl.com.ftd.wow.skill.enemy.fireElemental.Radiation import Radiation


@unique
class VolcaicElemental_Skill_Enum(Enum):
    '''
    classdocs
    @attention: the value structure: skills constructor
    '''

    BLASTING = Blasting
    FLAMESHOCK = Flameshock
    RADIATION = Radiation