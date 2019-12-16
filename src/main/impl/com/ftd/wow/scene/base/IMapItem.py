'''
Created on Dec 16, 2019

@author: ftd
'''
import pygame

class IMapItem(object):
    '''
    classdocs
    '''


    
    def __init__(self, item_images):
        '''
        @param enemy_images: 
        '''
        # image
        self.__images = []
        # image
        self._load_images(item_images)


    def _load_images(self, item_images):
        for temp_image in item_images:
            item_image = pygame.image.load(temp_image).convert_alpha()
            self.__images.append(item_image)
            
    
    def get_item_images(self):
        return self.__images