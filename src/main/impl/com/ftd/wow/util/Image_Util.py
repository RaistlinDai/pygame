'''
Created on Sep 11, 2019

@author: ftd
'''
import pygame

class Image_Util(object):
    '''
    
    '''
    
    @staticmethod
    def calculate_character_height_by_screen_size(screen_h):
        '''
        Calculate the standard character height according to the screen's height
        The default value is 150 in 1280*720
        @param screen_h: the height of screen
        @return: the standard height of character 
        '''
        standard_h = 150 * screen_h / 720
        return int(standard_h)
    
    
    @staticmethod
    def calculate_character_width_by_height(character_image, standard_h):
        '''
        @param character_image: the height of character
        @param: standard_h: the standard height of character 
        '''
        w, h = character_image.get_size()
        standard_w = w * standard_h / h
        return int(standard_w)
    
    
    @staticmethod
    def calculate_skill_in_fight_height_by_screen_size(screen_h):
        '''
        Calculate the skill label height according to the screen's height
        The default value is 50 in 1280*720
        @param skill_image: the height of skill label
        @return: standard_h: the standard height of skill 
        '''
        standard_h = 70 * screen_h / 720
        return int(standard_h)
    
    
    @staticmethod
    def calculate_skill_in_fight_width_by_height(skill_label_image, standard_h):
        '''
        @param skill_label_image: the height of skill label
        @param: standard_h: the standard height of label skill 
        '''
        w, h = skill_label_image.get_size()
        standard_w = w * standard_h / h
        return int(standard_w)
    
    