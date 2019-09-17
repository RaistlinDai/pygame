'''
Created on Jul 14, 2019

@author: ftd
'''
import pygame
from src.main.impl.com.ftd.wow.layout.bar.Bottom_Bar import Bottom_Bar
from src.main.impl.com.ftd.wow.layout.bar.Top_Bar import Top_Bar
from src.main.api.com.ftd.wow.scene.IScene import IScene
from src.main.impl.com.ftd.wow.util.Image_Util import Image_Util

class IFightScene(IScene):
    '''
    
    '''
    
    def __init__(self, scene_image, size_w, size_h, active_team, bottom_bar, top_bar):
        
        self.__background = None
        # size
        self.__size_w = 1280
        self.__size_h = 720
        
        # character positions
        self.__character_position = {1:(50, 420), 2:(150, 420), 3:(250, 420), 4:(350, 420)}
        
        self.__bottom_bar = None
        self.__top_bar = None
        self.__team = active_team
        self.__enemies = []
        
        # load the scene pictures in order
        self.__background = pygame.image.load(scene_image.value).convert()
        # adjust the scene size
        if (size_w and size_h):
            self.__size_w = size_w
            self.__size_h = size_h
            self.__background = pygame.transform.scale(self.__background, (size_w, size_h))
            
        # load top and bottom
        self.__bottom_bar = bottom_bar 
        self.__top_bar = top_bar
    
    
    def render_scene(self, screen_ins):
        screen_ins.blit(self.__background, (0,0), (0,0,self.__size_w,self.__size_h))
        self.__bottom_bar.render_image(screen_ins)
        self.__top_bar.render_image(screen_ins)
        self.render_characters(screen_ins)
        
             
    def render_characters(self, screen_ins):             
        # render the character
        characters = self.__team.get_teammembers()
        idx = 0
        for temp_char in characters:
            idx = idx + 1
            if not temp_char:
                continue
            
            # resize character
            calc_h = Image_Util.calculate_character_height_by_screen_size(self.__size_h)
            calc_w = Image_Util.calculate_character_width_by_height(temp_char.get_stand_image(), calc_h)
            temp_char.resize_character_images(calc_w, calc_h)
            
            # re-calculate character position
            (x,y) = self.__character_position[idx]
            (x,y) = Image_Util.calculate_character_position_by_screen_size(self.__size_w, self.__size_h, idx)
            
            screen_ins.blit(temp_char.get_stand_image(), (x,y), (0, 0, calc_w, calc_h))
            
            
    
