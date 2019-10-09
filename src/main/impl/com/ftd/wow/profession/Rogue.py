'''
Created on Sep 04, 2019

@author: ftd
'''

from src.main.api.com.ftd.wow.profession.IProfession import IProfession
from src.main.impl.com.ftd.wow.skill.rogue.Rogue_Skill_Enum import Rogue_Skill_Enum
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant

class Rogue (IProfession):
    '''
    
    '''
    
    def __init__(self):
        super().__init__(Materials_Constant.character_rogue_image_filenames, Rogue_Skill_Enum, \
                         [10, 4, 2, 5, 8, 10, 1.2])
