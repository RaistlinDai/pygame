'''
Created on Jul 14, 2019

@author: ftd
'''
import pygame
from src.main.api.com.ftd.wow.scene.IScene import IScene
from _overlapped import NULL

class IMenuScene(IScene):
    '''
    
    '''
    
    def __init__(self, scene_image, size_w, size_h):
        
        self.__background = NULL
        # size
        self.__size_w = 1280
        self.__size_h = 720
        
        # load the scene pictures in order
        self.__background = pygame.image.load(scene_image.value).convert()

        # adjust the scene size
        if (size_w and size_h):
            self.__size_w = size_w
            self.__size_h = size_h
            self.__background = pygame.transform.scale(self.__background, (size_w, size_h))
            

    def render_scene(self, screen_ins):
        screen_ins.blit(self.__background, (0,0), (0,0,self.__size_w,self.__size_h))


