'''
Created on Sep 12, 2019

@author: ftd
'''
import pygame
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant

class Bottom_Bar(object):
    '''
    
    '''
    
    
    def __init__(self, size_w, size_h):
        # size
        self.__size_w = size_w
        self.__size_h = size_h
        # images
        self.__image = Materials_Constant.rogue_backstab_image_filename