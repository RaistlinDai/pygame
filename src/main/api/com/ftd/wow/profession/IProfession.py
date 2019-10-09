'''
Created on Sep 10, 2019

@author: ftd
'''
import pygame

class IProfession(object):
    '''
    
    '''
    
    def __init__(self, prof_images, skill_enum, profession_properties=None):
        '''
        @param prof_images: 
        @param skill_enum: 
        @param profession_properties: 0: basic_healthy;
                                      1: basic_attack;
                                      2: basic_defense;
                                      3: basic_speed;
                                      4: basic_critical;
                                      5: basic_dodge;
                                      6: basic_level_upgrade_rate;
        '''
        # image
        self.__images = []
        # skills
        self.__skills = []
        # image
        self._load_images(prof_images)
        # fight skills
        self._load_skills(skill_enum)
        # camping skills
        
        
        if not profession_properties or len(profession_properties) != 7:
            return
        
        # basic properties
        # healthy
        self.__basic_healthy = profession_properties[0]
        # attack
        self.__basic_attack = profession_properties[1]
        # defense
        self.__basic_defense = profession_properties[2]
        # speed
        self.__basic_speed = profession_properties[3]
        # critical
        self.__basic_critical = profession_properties[4]
        # critical damage
        self.__basic_critical_damage = 150
        # dodge
        self.__basic_dodge = profession_properties[5]
        # level rate
        self.__basic_rate = profession_properties[6]
        
        
    def _load_images(self, prof_images):
        for temp_image in prof_images:
            char_image = pygame.image.load(temp_image).convert_alpha()
            self.__images.append(char_image)
            
    
    def _load_skills(self, skill_enum):
        for temp_skill in skill_enum:
            temp_skill = temp_skill.value()
            self.__skills.append(temp_skill)
    
    
    def get_skills(self):
        return self.__skills
        
        
    def get_images(self):
        '''
        0: stand
        1: stand-select
        2: atack1
        3: atack2
        4: suffer
        5: dead
        '''
        return self.__images
    

    def get_basic_healthy(self):
        return self.__basic_healthy


    def get_basic_defense(self):
        return self.__basic_defense


    def get_basic_speed(self):
        return self.__basic_speed


    def get_basic_attack(self):
        return self.__basic_attack


    def get_basic_critical(self):
        return self.__basic_critical


    def get_basic_dodge(self):
        return self.__basic_dodge
    
    
    def get_basic_skills(self):
        return self.__basic_skills
    
    
    def get_basic_rate(self):
        return self.__basic_rate


    def set_basic_critical_damage(self, value):
        self.__basic_critical_damage = value
        
    
    def get_basic_critical_damage(self):
        return self.__basic_critical_damage
        
        
    basic_healthy = property(get_basic_healthy, None, None, None)
    basic_defense = property(get_basic_defense, None, None, None)
    basic_speed = property(get_basic_speed, None, None, None)
    basic_attack = property(get_basic_attack, None, None, None)
    basic_critical = property(get_basic_critical, None, None, None)
    basic_dodge = property(get_basic_dodge, None, None, None)
    basic_rate = property(get_basic_rate, None, None, None)
    basic_critical_damage = property(get_basic_critical_damage, set_basic_critical_damage, None, None)
    
    
    