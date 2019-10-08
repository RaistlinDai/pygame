'''
Created on Jul 14, 2019

@author: ftd
'''
import pygame
from src.main.api.com.ftd.wow.scene.IScene import IScene
from src.main.impl.com.ftd.wow.util.Image_Util import Image_Util
from src.main.impl.com.ftd.wow.util.Enemy_Util import Enemy_Util
import time
from src.main.impl.com.ftd.wow.util.Fight_Util import Fight_Util

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
        
        self.__current_selection = None
        self.__current_target = None
        self.__current_target_extension = []
        
        self.__active_team = None
        self.__active_enemies = None
        
        self.__is_fighting = False
        self.__fighting_timer = 0
        self.__is_fighting_in_round = False
        
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
        
        # render the fighting image
        self.render_fighting(screen_ins)
        
             
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
            
            # resize character stand image
            calc_h = Image_Util.calculate_character_height_by_screen_size(self.__size_h)
            calc_w = Image_Util.calculate_character_width_by_height(temp_char.get_stand_image(), calc_h)
            calc_in_fight_h = Image_Util.calculate_character_in_fight_height_by_screen_size(self.__size_h)
            calc_in_fight_w = Image_Util.calculate_character_width_by_height(temp_char.get_fighting_image(), calc_in_fight_h)

            temp_char.resize_character_images(calc_w, calc_h, calc_in_fight_w, calc_in_fight_h)
            temp_prof_rate = temp_char.get_character_profession_rate()
            
            # re-calculate character stand image position
            (x,y) = Image_Util.calculate_character_position_by_screen_size(self.__size_w, self.__size_h, idx, temp_prof_rate)
            self.__character_properties[idx]['position'] = (x,y)
            self.__character_properties[idx]['image_size'] = (0, 0, calc_w, calc_h)
            
            if self.__current_selection and self.__current_selection.get_character_name() == temp_char.get_character_name():
                # skip the fighting character
                if self.__is_fighting:
                    continue
                
                new_w, new_h = temp_char.get_stand_select_image().get_size()
                screen_ins.blit(temp_char.get_stand_select_image(), (x,y), (0, 0, new_w, new_h))
                
            elif self.__current_target and self.__current_target.get_character_name() == temp_char.get_character_name():
                # skip the fighting character
                if self.__is_fighting:
                    continue
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
            calc_in_fight_h = Image_Util.calculate_character_in_fight_height_by_screen_size(self.__size_h)
            calc_in_fight_w = Image_Util.calculate_character_width_by_height(temp_char.get_fighting_image(), calc_in_fight_h)
            
            temp_char.resize_character_images(calc_w, calc_h, calc_in_fight_w, calc_in_fight_h)
            temp_prof_rate = temp_char.get_character_enemy_type_rate()
            
            # re-calculate character position
            (x,y) = Image_Util.calculate_enemy_position_by_screen_size(self.__size_w, self.__size_h, idx, temp_prof_rate)
            self.__enemy_properties[idx]['position'] = (x,y)
            self.__enemy_properties[idx]['image_size'] = (0, 0, calc_w, calc_h)
            
            if self.__current_target and self.__current_target.get_character_name() == temp_char.get_character_name():
                # skip the fighting character
                if self.__is_fighting:
                    continue
                
                target_enemy_position = (x,y)
                is_valid_target_enemy = True
            
            elif self.__current_selection and self.__current_selection.get_character_name() == temp_char.get_character_name():
                # skip the fighting character
                if self.__is_fighting:
                    continue
            else:
                new_w, new_h = temp_char.get_stand_image().get_size()
                screen_ins.blit(temp_char.get_stand_image(), (x,y), (0, 0, new_w, new_h))
        
        if not self.__is_fighting and self.__current_target and is_valid_target_enemy == True:
            new_w, new_h = self.__current_target.get_stand_select_image().get_size()
            screen_ins.blit(self.__current_target.get_stand_select_image(), target_enemy_position, (0, 0, new_w, new_h))
    
    
    def render_fighting(self, screen_ins):
        # image timer
        current_time = time.time()*1000.0
        
        # in fight
        if self.__is_fighting and self.__fighting_timer > 0 and current_time - self.__fighting_timer <= 1000:
            # calculate attack result
            '''
            @todo: remove self.__is_fighting_in_round for skill calculation testing
            '''
            if not self.__is_fighting_in_round:
                Fight_Util.calculate_fighting(self.__current_selection, self.__current_target, self.__bottom_bar.get_current_select_skill())
                self.__is_fighting_in_round = True
                
            # render the character
            if self.__active_team:
                characters = self.__active_team.get_teammembers()
            
                idx = 0
                for temp_char in characters:
                    idx = idx + 1
                    if not temp_char:
                        continue
                    
                    if self.__current_selection and self.__current_selection.get_character_name() == temp_char.get_character_name():
                        temp_prof_rate = temp_char.get_character_profession_rate()
                        (calc_w, calc_h) = Image_Util.calculate_character_in_fight_position_by_screen_size(self.__size_w, self.__size_h, idx, temp_prof_rate)
                
                        screen_ins.blit(self.__current_selection.get_fighting_image(), (calc_w,calc_h))
                        break
                    
                    if self.__current_target and self.__current_target.get_character_name() == temp_char.get_character_name():
                        temp_prof_rate = temp_char.get_character_profession_rate()
                        (calc_w, calc_h) = Image_Util.calculate_character_in_fight_position_by_screen_size(self.__size_w, self.__size_h, idx, temp_prof_rate)
                
                        screen_ins.blit(self.__current_target.get_fighting_image(), (calc_w,calc_h))
                        break
            
            # render the enemy
            if self.__active_enemies:
                enemies = self.__active_enemies.get_teammembers()
            
                idx = 0
                for temp_char in enemies:
                    idx = idx + 1
                    if not temp_char:
                        continue
                
                    if self.__current_selection and self.__current_selection.get_character_name() == temp_char.get_character_name():
                        temp_prof_rate = temp_char.get_character_enemy_type_rate()
                        (calc_w, calc_h) = Image_Util.calculate_enemy_in_fight_position_by_screen_size(self.__size_w, self.__size_h, idx, temp_prof_rate)
                
                        screen_ins.blit(self.__current_selection.get_fighting_image(), (calc_w,calc_h))
                        break
                    
                    if self.__current_target and self.__current_target.get_character_name() == temp_char.get_character_name():
                        temp_prof_rate = temp_char.get_character_enemy_type_rate()
                        (calc_w, calc_h) = Image_Util.calculate_enemy_in_fight_position_by_screen_size(self.__size_w, self.__size_h, idx, temp_prof_rate)
                        
                        screen_ins.blit(self.__current_target.get_fighting_image(), (calc_w,calc_h))
                        break
            
            # render the skill effect
            if self.__bottom_bar.get_current_select_skill():
                effect_img = self.__bottom_bar.get_current_select_skill().get_effect_image()
                screen_ins.blit(effect_img, Image_Util.calculate_skill_effect_size_by_screen_size(self.__size_w, self.__size_h))
            
        else:
            if self.__fighting_timer > 0 and current_time - self.__fighting_timer > 1000:
                # release select skill
                self.__bottom_bar.set_current_select_skill(None)
                
            self.__is_fighting = False
            self.__fighting_timer = 0
            self.__is_fighting_in_round = False
            
            
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
        self.__current_selection = current_character
        if self.__bottom_bar:
            self.__bottom_bar.set_current_character(self.__current_selection)
            
    
    def get_cover_character(self, cursor_x, cursor_y):
        if self.__is_fighting:
            return
        
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
                    self.__current_target = temp_char['enemy']
                    break
                else:
                    self.__current_target = None
            else:
                self.__current_target = None
            
    
    # ========================================================== #
    #                         Event                              #
    # ========================================================== #
    def mouse_click_event(self, pressed_mouse):
        if pressed_mouse[0]:
            if self.__bottom_bar.get_current_select_skill() and self.__current_target:
                # trigger fighting image
                self.__is_fighting = True
                self.__fighting_timer = time.time()*1000.0
        
        # bottom bar click event
        self.__bottom_bar.mouse_click_event(pressed_mouse)
    
    
    def cursor_event(self, cursor_x, cursor_y):
        self.get_cover_character(cursor_x, cursor_y)
        # bottom bar
        self.__bottom_bar.render_cover_skill(cursor_x, cursor_y)
        
    
    