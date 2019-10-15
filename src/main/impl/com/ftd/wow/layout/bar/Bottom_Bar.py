'''
Created on Sep 12, 2019

@author: ftd
'''
import pygame
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant
from src.main.impl.com.ftd.wow.util.Image_Util import Image_Util
from src.main.api.com.ftd.wow.character.ICharacter import ICharacter

class Bottom_Bar(object):
    '''
    
    '''
    
    def __init__(self, size_w=None, size_h=None):
        # size
        self.__size_w = 1280
        self.__size_h = 250
        # position
        self.__pos_x = 0
        self.__pos_y = 470
        # current character
        self.__current_character = None
        # active skills
        self.__active_skills = None
        # cover skill
        self.__current_cover_skill = None
        # select skill
        self.__current_select_skill = None
        
        # images
        self.__image = pygame.image.load(Materials_Constant.bottom_bar_image_filename).convert_alpha()
        if size_w and size_h:
            self.__size_w = size_w
            self.__size_h = Image_Util.calculate_bottom_bar_height_by_screen_size(size_h)
            self.__pos_y = Image_Util.calculate_bottom_bar_positionY_by_screen_size(size_h)
            self.__image = pygame.transform.scale(self.__image, (self.__size_w, self.__size_h))
            
    
    def render_image(self, screen_ins, screen_w, screen_h):
        
        if screen_w and screen_h:
            self.__size_w = screen_w
            self.__size_h = Image_Util.calculate_bottom_bar_height_by_screen_size(screen_h)
            self.__pos_y = Image_Util.calculate_bottom_bar_positionY_by_screen_size(screen_h)
            self.__image = pygame.transform.scale(self.__image, (self.__size_w, self.__size_h))
        
        screen_ins.blit(self.__image, (0, self.__pos_y), (0,0,self.__size_w,self.__size_h))
        self.render_skills(screen_ins)
        
    
    def render_skills(self, screen_ins, character=None):
        
        if character:
            self.__current_character = character
        
        if not self.__current_character or not isinstance(self.__current_character, ICharacter):
            return False, 'Invalid character, no skills load!'
        
        self.__active_skills = self.__current_character.get_active_skills()
        # render the skill bar
        idx = 0
        for active_skill in self.__active_skills:
            temp_pos_x = Image_Util.calculate_skill_in_fight_positionX_by_screen_size(self.__size_w, idx)
            temp_pos_y = Image_Util.calculate_skill_in_fight_positionY_by_screen_size(self.__size_h + self.__pos_y)
            temp_size = Image_Util.calculate_skill_in_fight_size_by_screen_size(self.__size_h + self.__pos_y)
            
            if self.__current_select_skill and self.__current_select_skill.get_skill_name() == active_skill.get_skill_name():
                active_skill_image = active_skill.get_skill_image_select()
            elif self.__current_cover_skill and self.__current_cover_skill.get_skill_name() == active_skill.get_skill_name():
                active_skill_image = active_skill.get_skill_image_select()
            else:
                active_skill_image = active_skill.get_skill_image()
            active_skill_image = pygame.transform.scale(active_skill_image, (temp_size, temp_size))
            
            idx = idx + 1
            screen_ins.blit(active_skill_image, (temp_pos_x, temp_pos_y), (0, 0, temp_size, temp_size))
            
            
    def set_current_character(self, current_character):
        self.__current_character = current_character
            
            
    def render_cover_skill(self, cursor_x, cursor_y):
        if not self.__active_skills:
            return
        
        temp_pos_x = []
        idx = 0
        for idx in [0,1,2,3]:
            temp_pos_x.append(Image_Util.calculate_skill_in_fight_positionX_by_screen_size(self.__size_w, idx))
            temp_pos_y = Image_Util.calculate_skill_in_fight_positionY_by_screen_size(self.__size_h + self.__pos_y)
            temp_size = Image_Util.calculate_skill_in_fight_size_by_screen_size(self.__size_h + self.__pos_y)
            
        if (temp_pos_x[0] < cursor_x < temp_pos_x[0] + temp_size) and (temp_pos_y < cursor_y < temp_pos_y + temp_size) and self.__active_skills[0]:
            if not self.__current_select_skill:
                self.__current_cover_skill = self.__active_skills[0]
        elif (temp_pos_x[1] < cursor_x < temp_pos_x[1] + temp_size) and (temp_pos_y < cursor_y < temp_pos_y + temp_size) and self.__active_skills[1]:
            if not self.__current_select_skill:
                self.__current_cover_skill = self.__active_skills[1]
        elif (temp_pos_x[2] < cursor_x < temp_pos_x[2] + temp_size) and (temp_pos_y < cursor_y < temp_pos_y + temp_size) and self.__active_skills[2]:
            if not self.__current_select_skill:
                self.__current_cover_skill = self.__active_skills[2]
        elif (temp_pos_x[3] < cursor_x < temp_pos_x[3] + temp_size) and (temp_pos_y < cursor_y < temp_pos_y + temp_size) and self.__active_skills[3]:
            if not self.__current_select_skill:
                self.__current_cover_skill = self.__active_skills[3]
        else:
            self.__current_cover_skill = None
            
    
    def get_current_select_skill(self):
        return self.__current_select_skill
        
    
    def set_current_select_skill(self, current_select_skill):
        self.__current_select_skill = current_select_skill
    
    
    def mouse_click_event(self, pressed_mouse):
        
        if pressed_mouse[0]:
            if self.__current_cover_skill:
                self.__current_select_skill = self.__current_cover_skill
            else:
                pass
            
        elif pressed_mouse[2]:
            if self.__current_select_skill:
                self.__current_select_skill = None
            