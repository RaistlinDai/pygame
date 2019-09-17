'''
Created on Sep 11, 2019

@author: ftd
'''
from enum import Enum, unique
from src.main.impl.com.ftd.wow.skill.rogue.Backstab import Backstab
from src.main.impl.com.ftd.wow.skill.rogue.Blind import Blind
from src.main.impl.com.ftd.wow.skill.rogue.Disapper import Disapper
from src.main.impl.com.ftd.wow.skill.rogue.Gouge import Gouge
from src.main.impl.com.ftd.wow.skill.rogue.Evilatt import Evilatt
from src.main.impl.com.ftd.wow.skill.rogue.Poision import Poision
from src.main.impl.com.ftd.wow.skill.rogue.Speedup import Speedup
from src.main.impl.com.ftd.wow.skill.rogue.Strangle import Strangle
from src.main.impl.com.ftd.wow.skill.rogue.Sworddance import Sworddance


@unique
class Rogue_Skill_Enum(Enum):
    '''
    classdocs
    @attention: the value structure: skills constructor
    '''

    EVILATT = Evilatt
    DISAPPER = Disapper
    GOUGE = Gouge
    POISION = Poision
    SPEEDUP = Speedup
    
    BACKSTAB = Backstab
    SWORDDANCE = Sworddance
    BLIND = Blind
    STRANGLE = Strangle
