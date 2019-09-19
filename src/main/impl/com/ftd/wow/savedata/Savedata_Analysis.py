'''
Created on Sep 17, 2019

@author: ftd
'''
import json
from src.main.impl.com.ftd.wow.character.Character import Character_Skill


class Savedata_Analsis (object):
    '''
    
    '''
    
    @staticmethod
    def load_savedata():
        '''
        
        '''
        
        load_character_skills = {}
        
        with open('savedata01.json', 'r') as f:
            distros_dict = json.load(f)
        
        # load characters
        characters = distros_dict["Characters"]
        for temp_char in characters:
            for skill in temp_char['Skills']:
                for item in skill:
                    character_skill = Character_Skill(item, bool(skill[0]), bool(skill[1], skill[2]))
                    load_character_skills[bool(skill[0])] = character_skill
        
        return load_character_skills