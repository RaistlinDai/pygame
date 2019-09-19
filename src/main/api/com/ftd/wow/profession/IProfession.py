'''
Created on Sep 10, 2019

@author: ftd
'''
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant

class IProfession(object):
    '''
    
    '''
    
    def __init__(self, prof_images, skill_enum):
        # image
        self.__images = []
        # skills
        self.__skills = []
        # image
        self._load_images(prof_images)
        # fight skills
        self._load_skills(skill_enum)
        # camping skills
        
        
    def _load_images(self, prof_images):
        for temp_image in prof_images:
            self.__images.append(temp_image)
            
    
    def _load_skills(self, skill_enum):
        for temp_skill in skill_enum:
            rogue_skill = temp_skill.value()
            self.__skills.append(rogue_skill)
    
    
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
    
    
    