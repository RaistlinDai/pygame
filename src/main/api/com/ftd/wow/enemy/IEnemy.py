'''
Created on Sep 23, 2019

@author: ftd
'''
import pygame

class IEnemy(object):
    '''
    
    '''
    
    def __init__(self, enemy_images):
        # image
        self.__images = []
        # skills
        self.__skills = []
        # image
        self._load_images(enemy_images)
        
        
    def _load_images(self, enemy_images):
        for temp_image in enemy_images:
            enemy_image = pygame.image.load(temp_image).convert_alpha()
            self.__images.append(enemy_image)
    
    
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
    
    
