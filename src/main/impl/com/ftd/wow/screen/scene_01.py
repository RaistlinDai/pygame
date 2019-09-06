'''
Created on Aug 27, 2019

@author: ftd
'''
import pygame
from pygame.locals import *
from sys import exit
from src.main.impl.com.ftd.wow.const.materials_constant import materials_constant

class scene_01(object):
    '''
    
    '''
    
    def __init__(self, pos_x, pos_y, size_w, size_h):
        self._background = pygame.image.load(materials_constant.scene01_image_filename).convert()
        if (size_w and size_h):
            self._background = pygame.transform.scale(self._background, (size_w, size_h))
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__size_w = size_w
        self.__size_h = size_h
        
    def get_background(self):
        return self._background