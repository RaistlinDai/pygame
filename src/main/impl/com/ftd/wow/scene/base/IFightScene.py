'''
Created on Jul 14, 2019

@author: ftd
'''
import pygame
from src.main.api.com.ftd.wow.scene.IScene import IScene
from src.main.impl.com.ftd.wow.util.Image_Util import Image_Util
from src.main.impl.com.ftd.wow.util.Enemy_Util import Enemy_Util

class IFightScene(IScene):
    '''
    
    '''
    
    def __init__(self, scene_image, bottom_bar=None, top_bar=None, size_w=None, size_h=None, active_team=None, current_character=None):
        
        self.__background = None
        # size
        self.__size_w = 1280
        self.__size_h = 720
        
        # character-screen properties
        self.__character_properties = {1:{'position':(50, 420), 'image_size':(0,0,0,0), 'character':None}, 
                                       2:{'position':(150, 420), 'image_size':(0,0,0,0), 'character':None}, 
                                       3:{'position':(250, 420), 'image_size':(0,0,0,0), 'character':None}, 
                                       4:{'position':(350, 420), 'image_size':(0,0,0,0), 'character':None}}
        self.__enemy_properties = {1:{'position':(700, 420), 'image_size':(0,0,0,0), 'enemy':None, "merge":None}, 
                                   2:{'position':(830, 420), 'image_size':(0,0,0,0), 'enemy':None, "merge":None}, 
                                   3:{'position':(960, 420), 'image_size':(0,0,0,0), 'enemy':None, "merge":None}, 
                                   4:{'position':(10900, 420), 'image_size':(0,0,0,0), 'enemy':None, "merge":None}}
        
        self.__bottom_bar = None
        self.__top_bar = None
        self.__current_character = None
        self.__active_team = None
        self.__active_enemies = None
        self.__target_enemy = None
        
        # setup the active team and characters
        self.add_active_team(active_team)
        
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
        
        # set the current character
        self.set_current_character(current_character)
    
    
    def render_scene(self, screen_ins, screen_w=None, screen_h=None):
        if (screen_w and screen_h):
            self.__size_w = screen_w
            self.__size_h = screen_h
            self.__background = pygame.transform.scale(self.__background, (screen_w, screen_h))
            
        screen_ins.blit(self.__background, (0,0), (0,0,self.__size_w,self.__size_h))
        
        # render the bottom bar
        self.__bottom_bar.render_image(screen_ins, self.__size_w, self.__size_h)
        
        # render the top bar
        self.__top_bar.render_image(screen_ins, self.__size_w, self.__size_h)
        
        # render the characters
        self.render_characters(screen_ins)
        
        # render the enemies
        self.render_enemies(screen_ins)
        
             
    def render_characters(self, screen_ins):             
        # render the character
        if not self.__active_team:
            return
        characters = self.__active_team.get_teammembers()
        
        idx = 0
        for temp_char in characters:
            idx = idx + 1
            if not temp_char:
                continue
            
            # resize character
            calc_h = Image_Util.calculate_character_height_by_screen_size(self.__size_h)
            calc_w = Image_Util.calculate_character_width_by_height(temp_char.get_stand_image(), calc_h)
            temp_char.resize_character_images(calc_w, calc_h)
            temp_prof_rate = temp_char.get_character_profession_rate()
            
            # re-calculate character position
            (x,y) = Image_Util.calculate_character_position_by_screen_size(self.__size_w, self.__size_h, idx, temp_prof_rate)
            self.__character_properties[idx]['position'] = (x,y)
            self.__character_properties[idx]['image_size'] = (0, 0, calc_w, calc_h)
            
            if self.__current_character and self.__current_character.get_character_name() == temp_char.get_character_name():
                new_w, new_h = temp_char.get_stand_select_image().get_size()
                screen_ins.blit(temp_char.get_stand_select_image(), (x,y), (0, 0, new_w, new_h))
            else:
                new_w, new_h = temp_char.get_stand_image().get_size()
                screen_ins.blit(temp_char.get_stand_image(), (x,y), (0, 0, new_w, new_h))
    
    
    def render_enemies(self, screen_ins):             
        # render the character
        if not self.__active_enemies:
            return
        enemies = self.__active_enemies.get_teammembers()
        target_enemy_position = None
        is_valid_target_enemy = False
        
        idx = 0
        for temp_char in enemies:
            idx = idx + 1
            if not temp_char:
                continue
            
            # resize character
            calc_h = Image_Util.calculate_character_height_by_screen_size(self.__size_h)
            calc_w = Image_Util.calculate_character_width_by_height(temp_char.get_stand_image(), calc_h)
            temp_char.resize_character_images(calc_w, calc_h)
            temp_prof_rate = temp_char.get_character_enemy_type_rate()
            
            # re-calculate character position
            (x,y) = Image_Util.calculate_enemy_position_by_screen_size(self.__size_w, self.__size_h, idx, temp_prof_rate)
            self.__enemy_properties[idx]['position'] = (x,y)
            self.__enemy_properties[idx]['image_size'] = (0, 0, calc_w, calc_h)
            
            if self.__target_enemy and self.__target_enemy.get_character_name() == temp_char.get_character_name():
                target_enemy_position = (x,y)
                is_valid_target_enemy = True
            else:
                new_w, new_h = temp_char.get_stand_image().get_size()
                screen_ins.blit(temp_char.get_stand_image(), (x,y), (0, 0, new_w, new_h))
        
        if self.__target_enemy and is_valid_target_enemy == True:
            new_w, new_h = self.__target_enemy.get_stand_select_image().get_size()
            screen_ins.blit(self.__target_enemy.get_stand_select_image(), target_enemy_position, (0, 0, new_w, new_h))
        
            
    def add_active_team(self, active_team):
        self.__active_team = active_team
        if self.__active_team:
            idx = 0
            characters = self.__active_team.get_teammembers()
            for temp_char in characters:
                idx = idx + 1
                if temp_char:
                    self.__character_properties[idx]['character'] = temp_char
    
    
    def add_active_enemies(self, active_enemies):
        self.__active_enemies = active_enemies
        if self.__active_enemies:
            idx = 0
            for temp_char in self.__active_enemies.get_teammembers():
                idx = idx + 1
                if temp_char:
                    self.__enemy_properties[idx]['enemy'] = temp_char
                    
        
    def set_current_character(self, current_character):
        self.__current_character = current_character
        if self.__bottom_bar:
            self.__bottom_bar.set_current_character(self.__current_character)
            
    
    def get_cover_character(self, cursor_x, cursor_y):
        for temp_idx in self.__character_properties:
            temp_char = self.__character_properties[temp_idx]
            (temp_char_x, temp_char_y) = temp_char['position']
            (temp_char_p1, temp_char_p2, temp_char_w, temp_char_h) = temp_char['image_size']
            
            in_x = temp_char_x < cursor_x < temp_char_x + temp_char_w
            in_y = temp_char_y < cursor_y < temp_char_y + temp_char_h
            
            if in_x and in_y:
                print(temp_char['character'].get_character_name())
                break
    
        for temp_idx in self.__enemy_properties:
            temp_char = self.__enemy_properties[temp_idx]
            (temp_char_x, temp_char_y) = temp_char['position']
            (temp_char_p1, temp_char_p2, temp_char_w, temp_char_h) = temp_char['image_size']
            
            in_x = temp_char_x < cursor_x < temp_char_x + temp_char_w
            in_y = temp_char_y < cursor_y < temp_char_y + temp_char_h
            
            if in_x and in_y:
                if self.__bottom_bar.get_current_select_skill():
                    self.__target_enemy = temp_char['enemy']
                    break
                else:
                    self.__target_enemy = None
            else:
                self.__target_enemy = None
            
    
    def render_fighting(self):
        pass
    
    # ========================================================== #
    #                         Event                              #
    # ========================================================== #
    def mouse_click_event(self, pressed_mouse):
        if pressed_mouse[0]:
            if self.__bottom_bar.get_current_select_skill() and self.__target_enemy:
                self.render_fighting()
        
        # bottom bar click event
        self.__bottom_bar.mouse_click_event(pressed_mouse)
    
    
    def cursor_event(self, cursor_x, cursor_y):
        self.get_cover_character(cursor_x, cursor_y)
        # bottom bar
        self.__bottom_bar.render_cover_skill(cursor_x, cursor_y)