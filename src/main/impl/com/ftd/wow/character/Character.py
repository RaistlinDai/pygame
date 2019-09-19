'''
Created on Sep 04, 2019

@author: ftd
'''

import pygame
from src.main.api.com.ftd.wow.character.ICharacter import ICharacter
from src.main.api.com.ftd.wow.profession.IProfession import IProfession
from src.main.api.com.ftd.wow.skill.ISkill import ISkill

class Character (ICharacter):
    '''
    
    '''
    
    def __init__(self, name, prof, character_skills):
        
        # super class constructor
        super().__init__()
        # character name
        self.__character_name = name
        # character images
        self.__fight_skills = {}    # {name:{"skill_obj":A, "isActive":B, "isLearned":C, "Level":D}}
        self.__camp_skills_images = []
        self.__profession_images = []

        # profession
        self.__prof = None
        if prof and isinstance(prof, IProfession):
            self.__prof = prof
        
        # images
        self.load_profession_images()
        # skills
        self.load_skills(character_skills)
        
    
    def load_profession_images(self):
        if not self.__prof:
            return
        # load profession images into pygame
        temp_images = self.__prof.get_images()
        for img in temp_images:
            self.__profession_images.append(img)
            
    
    def load_skills(self, character_skills):
        if not self.__prof:
            return
        # load skill images into pygame
        prof_skills = self.__prof.get_skills()
        for skill in prof_skills:
            load_character_skill = character_skills[skill.get_skill_name()]
            
            if load_character_skill and isinstance(load_character_skill, Character_Skill):
                self.__fight_skills[skill.get_skill_name()] = {"skill_obj":skill, 
                                                               "isActive": load_character_skill.get_is_active(), 
                                                               "isLearned": load_character_skill.get_is_learned(), 
                                                               "Level": load_character_skill.get_level()}
            else:    
                self.__fight_skills[skill.get_skill_name()] = {"skill_obj":skill, 
                                                               "isActive": False, 
                                                               "isLearned": False, 
                                                               "Level": 0}
    
        
    def get_stand_image(self):
        return self.__profession_images[0]
    
    
    def get_stand_select_image(self):
        return self.__profession_images[1]
    
    
    def resize_character_images(self, size_w, size_h):            
        idx1 = 0
        for img in self.__profession_images:
            self.__profession_images[idx1] = pygame.transform.scale(img, (size_w, size_h))
            idx1 = idx1 + 1
    
    
    def get_character_name(self):
        return self.__character_name
    
    
    def get_active_skills(self):
        active_skills = []
        for skill_name in self.__fight_skills:
            if self.__fight_skills[skill_name]["isActive"] == True:
                active_skills.append(self.__fight_skills[skill_name]["skill_obj"])
            
        return active_skills
        
        

class Character_Skill (object):
    '''
    '''
    
    def __init__(self, name=None, isActive=None, isLearned=None, level=None, skill=None):
        self.__name = None
        self.__isActive = False
        self.__isLearned = False
        self.__level = 0
        self.__skill = None
        
        if name:
            self.__name = name
        if isActive:
            self.__isActive = isActive
        if isLearned:
            self.__isLearned = isLearned
        if level:
            self.__level = level
        if skill and isinstance(skill, ISkill):
            self.__skill = skill


    def setup_skill(self, skill):
        if isinstance(skill, ISkill):
            self.__skill = skill
            
            
    def get_name(self):
        return self.__name


    def get_is_active(self):
        return self.__isActive


    def get_is_learned(self):
        return self.__isLearned


    def get_level(self):
        return self.__level


    def set_name(self, value):
        self.__name = value


    def set_is_active(self, value):
        self.__isActive = value


    def set_is_learned(self, value):
        self.__isLearned = value


    def set_level(self, value):
        self.__level = value


    def del_name(self):
        del self.__name


    def del_is_active(self):
        del self.__isActive


    def del_is_learned(self):
        del self.__isLearned


    def del_level(self):
        del self.__level

            
    name = property(get_name, set_name, del_name, "name's docstring")
    isActive = property(get_is_active, set_is_active, del_is_active, "isActive's docstring")
    isLearned = property(get_is_learned, set_is_learned, del_is_learned, "isLearned's docstring")
    level = property(get_level, set_level, del_level, "level's docstring")
            
    