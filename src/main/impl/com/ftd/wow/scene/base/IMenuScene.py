'''
Created on Jul 14, 2019

@author: ftd
'''
import pygame
from src.main.api.com.ftd.wow.scene.IScene import IScene
from _overlapped import NULL
from src.main.impl.com.ftd.wow.button.Horde_Button import Horde_Button

class IMenuScene(IScene):
    '''
    
    '''
    
    def __init__(self, scene_image, size_w=None, size_h=None):
        
        self.__background = NULL
        # size
        self.__size_w = 1280
        self.__size_h = 720
        
        # button
        self.__start_button = Horde_Button(585, 270, 100, 100)
        
        # load the scene pictures in order
        self.__background = pygame.image.load(scene_image.value).convert()

        # adjust the scene size
        if (size_w and size_h):
            self.__size_w = size_w
            self.__size_h = size_h
            self.__background = pygame.transform.scale(self.__background, (size_w, size_h))
            

    def render(self, screen_ins, screen_w=None, screen_h=None, scene_status=None):
        if (screen_w and screen_h):
            self.__size_w = screen_w
            self.__size_h = screen_h
            self.__background = pygame.transform.scale(self.__background, (screen_w, screen_h))
            
        screen_ins.blit(self.__background, (0,0), (0,0,self.__size_w,self.__size_h))
        
        # render the button
        self.render_button(screen_ins, scene_status)

    
    def render_button(self, screen_ins, scene_status=None):
        # render the button
        if (not scene_status):
            if (not self.is_button_cover()):
                screen_ins.blit(self.__start_button.show_button(), self.__start_button.get_position())
            else:
                screen_ins.blit(self.__start_button.show_button_cover(), self.__start_button.get_position())
        else:
            screen_ins.blit(self.__start_button.show_button_click(), self.__start_button.get_position())
        
    
    def is_button_cover(self):
        return self.__start_button.is_over()
    
    