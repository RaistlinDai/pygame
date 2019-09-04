'''
Created on Sep 04, 2019

@author: ftd
'''

import pygame
from src.main.pydev.com.ftd.wow.const.materials_constant import materials_constant

class horde_button (object):
    '''
    
    '''
    
    def __init__(self, upimage, downimage, position):
        self._image_up = pygame.image.load(materials_constant.button_horde_image_filename).convert_alpha()
        self._image_cover = pygame.image.load(materials_constant.button_horde_cover_image_filename).convert_alpha()
        self.position = position
        
    def is_over(self):
        point_x, point_y = pygame.mouse.get_pos()
        x, y = self.position
        w, h = self.imageUp.get_size()
    
        in_x = x - w/2 < point_x < x + w/2
        in_y = y - h/2 < point_y < y + h/2
        
        return in_x and in_y
    
    def show_button(self):
        return self._image_up
    
    def show_button_cover(self):
        return self._image_cover
        
    
    