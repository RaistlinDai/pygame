'''
Created on Aug 27, 2019

@author: ftd
'''
import pygame
from src.main.impl.com.ftd.wow.scene.base.IMenuScene import IMenuScene
from src.main.impl.com.ftd.wow.scene.Scene_Enum import Scene_Enum

class Scene_Login(IMenuScene):
    '''
    
    '''
    
    def __init__(self, size_w, size_h):
        super().__init__(Scene_Enum.LOGIN, size_w, size_h)
        
        
    def show_background(self):
        return self.__background
    
    
    def render_scene(self, screen_ins):
        super().render_scene(screen_ins)