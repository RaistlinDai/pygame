'''
Created on Sep 11, 2019

@author: ftd
'''
from enum import Enum, unique
from src.main.impl.com.ftd.wow.skill.rogue.Backstab import Backstab
from src.main.impl.com.ftd.wow.skill.rogue.Biting import Biting
from src.main.impl.com.ftd.wow.skill.rogue.Disapper import Disapper
from src.main.impl.com.ftd.wow.skill.rogue.Gouge import Gouge


@unique
class Rogue_Skill_Enum(Enum):
    '''
    classdocs
    @attention: the value structure: skills constructor
    '''

    BACKSTAB = Backstab
    BITING = Biting
    DISAPPER = Disapper
    GOUGE = Gouge
