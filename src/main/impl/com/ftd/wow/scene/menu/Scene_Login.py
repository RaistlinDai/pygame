'''
Created on Aug 27, 2019

@author: ftd
'''
import pygame
from src.main.impl.com.ftd.wow.scene.base.IMenuScene import IMenuScene
from src.main.impl.com.ftd.wow.scene.MenuScene_Enum import MenuScene_Enum

class Scene_Login(IMenuScene):
    '''
    
    '''
    
    def __init__(self, size_w, size_h):
        super().__init__(MenuScene_Enum.HORDE_LOGIN, size_w, size_h)
        
        
    def show_background(self):
        return self.__background
    
    
    def render_scene(self, screen_ins, screen_w=None, screen_h=None):
        super().render_scene(screen_ins, screen_w, screen_h)