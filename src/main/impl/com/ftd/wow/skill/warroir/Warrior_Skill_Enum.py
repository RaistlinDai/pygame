'''
Created on Sep 20, 2019

@author: ftd
'''
from enum import Enum, unique
from src.main.impl.com.ftd.wow.skill.warroir.Demoralizing import Demoralizing
from src.main.impl.com.ftd.wow.skill.warroir.Gluten import Gluten
from src.main.impl.com.ftd.wow.skill.warroir.Assault import Assault
from src.main.impl.com.ftd.wow.skill.warroir.Herocistrike import Herocistrike

@unique
class Warrior_Skill_Enum(Enum):
    '''
    classdocs
    @attention: the value structure: skills constructor
    '''

    DEMORALIZING = Demoralizing
    GLUTEN = Gluten
    ASSAULT = Assault
    HEROCISTRIKE = Herocistrike
