'''
Created on Aug 27, 2019

@author: ftd
'''
import pygame
from pygame.locals import *
from sys import exit
from src.main.impl.com.ftd.wow.const.materials_constant import materials_constant
from src.main.api.com.ftd.wow.scene.IBackground import IBackground

class scene_login(IBackground):
    '''
    
    '''
    
    def __init__(self, size_w, size_h):
        self._background = pygame.image.load(materials_constant.mainframe_image_filename).convert()
        self.__size_w = size_w
        self.__size_h = size_h
        
        w, h = self._background.get_size()
        
        if (size_w and size_h):
            self._background = pygame.transform.scale(self._background, (size_w, size_h))
        
        
    def show_background(self):
        return self._background
    
    
    