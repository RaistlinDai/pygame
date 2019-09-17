'''
Created on Sep 12, 2019

@author: ftd
'''
import pygame
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant
from src.main.impl.com.ftd.wow.util.Image_Util import Image_Util

class Top_Bar(object):
    '''
    
    '''
    
    def __init__(self, size_w=None, size_h=None):
        # size
        self.__size_w = 1280
        self.__size_h = 96
        # position
        self.__pos_x = 0
        self.__pos_y = 0
        # images
        self.__image = pygame.image.load(Materials_Constant.top_bar_image_filename).convert_alpha()
        if size_w and size_h:
            self.__size_w = size_w
            self.__size_h = Image_Util.calculate_top_bar_height_by_screen_size(size_h)
            self.__image = pygame.transform.scale(self.__image, (self.__size_w, self.__size_h))

    
    def render_image(self, screen_ins, screen_w, screen_h):
        if screen_w and screen_h:
            self.__size_w = screen_w
            self.__size_h = Image_Util.calculate_top_bar_height_by_screen_size(screen_h)
            self.__image = pygame.transform.scale(self.__image, (self.__size_w, self.__size_h))
            
        screen_ins.blit(self.__image, (0,0), (0,0,self.__size_w,self.__size_h))