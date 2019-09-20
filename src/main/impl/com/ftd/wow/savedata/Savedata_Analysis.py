'''
Created on Sep 17, 2019

@author: ftd
'''
import json
from src.main.impl.com.ftd.wow.character.Character import Character_Skill,\
    Character
from src.main.impl.com.ftd.wow.profession.base.Profession_Enum import Profession_Enum


class Savedata_Analsis (object):
    '''
    
    '''
    
    @staticmethod
    def load_savedata(resource_DTO):
        '''
        
        '''
        load_characters = []
        
        with open('savedata01.json', 'r') as f:
            distros_dict = json.load(f)
        
        # load characters
        characters = distros_dict["Characters"]
        for temp_char in characters:
            load_character_skills = {}    # {skill_name: Character_skill_obj}
            
            # valid the profession
            is_valid = False
            for temp_prof in Profession_Enum:
                if temp_prof.name == temp_char['Profession']:
                    is_valid = True
                    break
            if not is_valid:
                # TODO: process invalid profession
                continue
            
            for skill in temp_char['Skills']:
                for skill_name in skill:
                    print(skill_name, skill[skill_name][0], skill[skill_name][1], skill[skill_name][2])
                    character_skill = Character_Skill(skill_name, skill[skill_name][0], skill[skill_name][1], skill[skill_name][2])
                    load_character_skills[skill_name] = character_skill
            
            # create character
            load_character = Character(temp_char['Name'], resource_DTO.get_profession(temp_char['Profession']), load_character_skills)
            
            load_characters.append(load_character)
            
        return load_characters