'''
Created on Sep 04, 2019

@author: ftd
'''

import pygame
from src.main.impl.com.ftd.wow.const.materials_constant import materials_constant

class horde_button (object):
    '''
    
    '''
    
    def __init__(self, pos_x, pos_y, size_w, size_h):
        self._image_up = pygame.image.load(materials_constant.button_horde_image_filename).convert_alpha()
        self._image_cover = pygame.image.load(materials_constant.button_horde_cover_image_filename).convert_alpha()
        self._image_click = pygame.image.load(materials_constant.button_horde_click_image_filename).convert_alpha()
        if (size_w and size_h):
            self._image_up = pygame.transform.scale(self._image_up, (size_w, size_h))
            self._image_cover = pygame.transform.scale(self._image_cover, (size_w, size_h))
            self._image_click = pygame.transform.scale(self._image_click, (size_w, size_h))
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__size_w = size_w
        self.__size_h = size_h
        
    def get_position(self):
        return (self.__pos_x, self.__pos_y)    
        
    def is_over(self):
        point_x, point_y = pygame.mouse.get_pos()
        x = self.__pos_x
        y = self.__pos_y
        w, h = self._image_up.get_size()
    
        in_x = x < point_x < x + w
        in_y = y < point_y < y + h
        return in_x and in_y
    
    def show_button(self):
        return self._image_up
    
    def show_button_cover(self):
        return self._image_cover
        
    def show_button_click(self):
        return self._image_click
    