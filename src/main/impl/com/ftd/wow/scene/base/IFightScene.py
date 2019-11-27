'''
Created on Jul 14, 2019

@author: ftd
'''
import random
import time

import pygame

from src.main.api.com.ftd.wow.scene.IScene import IScene
from src.main.impl.com.ftd.wow.const.Scene_Constant import Scene_Constant
from src.main.impl.com.ftd.wow.controller.Abyss_Overlord import StatusType_Enum
from src.main.impl.com.ftd.wow.util.Fight_Util import Fight_Util
from src.main.impl.com.ftd.wow.util.Image_Util import Image_Util


class IFightScene(IScene):
    '''
    
    '''
    
    def __init__(self, scene_image, bottom_bar=None, top_bar=None, size_w=None, size_h=None):
        
        self.__background = None
        self.__foreground = None
        # size
        self.__size_w = 1280
        self.__size_h = 720
        
        # character-screen properties
        self.__character_move_properties = {1:{'position':(200, 340), 'image_size':(0,0,0,0), 'character':None}, 
                                            2:{'position':(350, 340), 'image_size':(0,0,0,0), 'character':None}, 
                                            3:{'position':(500, 340), 'image_size':(0,0,0,0), 'character':None}, 
                                            4:{'position':(650, 340), 'image_size':(0,0,0,0), 'character':None}}
        self.__character_combat_properties = {1:{'position':(50, 420), 'image_size':(0,0,0,0), 'character':None}, 
                                              2:{'position':(150, 420), 'image_size':(0,0,0,0), 'character':None}, 
                                              3:{'position':(250, 420), 'image_size':(0,0,0,0), 'character':None}, 
                                              4:{'position':(350, 420), 'image_size':(0,0,0,0), 'character':None}}
        self.__enemy_properties = {1:{'position':(700, 420), 'image_size':(0,0,0,0), 'enemy':None, "merge":None}, 
                                   2:{'position':(830, 420), 'image_size':(0,0,0,0), 'enemy':None, "merge":None}, 
                                   3:{'position':(960, 420), 'image_size':(0,0,0,0), 'enemy':None, "merge":None}, 
                                   4:{'position':(10900, 420), 'image_size':(0,0,0,0), 'enemy':None, "merge":None}}
        
        # load the scene pictures in order
        self.__background = pygame.image.load(scene_image).convert()
        # adjust the scene size
        if (size_w and size_h):
            self.__size_w = size_w
            self.__size_h = size_h
            self.__background = pygame.transform.scale(self.__background, (size_w, size_h))
            
        # load top and bottom
        self.__bottom_bar = bottom_bar 
        self.__top_bar = top_bar
    
    
    def get_enemy_properties(self):
        return self.__enemy_properties
    
    
    def set_enemy_properties(self, value):
        self.__enemy_properties = value
    
    
    def get_character_properties(self):
        return self.__character_combat_properties
    
    
    def set_character_properties(self, value):
        self.__character_combat_properties = value
        
        
    def get_bottom_bar(self):
        return self.__bottom_bar
    
    
    def set_bottom_bar(self, value):
        self.__bottom_bar = value
        
        
    def get_top_bar(self):
        return self.__top_bar
    
    
    def set_top_bar(self, value):
        self.__top_bar = value
        
        
    def get_foreground(self):
        return self.__foreground
    
    
    def set_foreground(self, value):
        self.__foreground = value
        
        
    def darken(self, screen_ins, value):
        "Value is 0 to 255. So 128 would be 50% darken"
        dark = pygame.Surface(screen_ins.get_size(), 32)
        dark.set_alpha(value, pygame.RLEACCEL)
        screen_ins.blit(dark, (0, 0), (0,0,self.__size_w,self.__size_h))
        
    
    def gradual_darken(self, screen_ins, darken_rate):
        darken_value = 255 * darken_rate
        self.darken(screen_ins, round(darken_value))
        
        
    def gradual_brighten(self, screen_ins, darken_rate):
        darken_value = 255 * (1 - darken_rate)
        self.darken(screen_ins, round(darken_value))
    
    
    def render(self, screen_ins, screen_w=None, screen_h=None, contextDTO=None, screen_status=None, \
               gradual_darken=False, gradual_brighten=False, darken_rate=0, character_moving_timer=0):
        
        new_moving_timer = 0
        
        if (screen_w and screen_h):
            self.__size_w = screen_w
            self.__size_h = screen_h
            self.__background = pygame.transform.scale(self.__background, (screen_w, screen_h))
        
        screen_ins.blit(self.__background, (0,0), (0,0,self.__size_w,self.__size_h))
        
        # gradual darken or brighten
        if gradual_darken:
            self.gradual_darken(screen_ins, darken_rate)
        elif gradual_brighten:
            self.gradual_brighten(screen_ins, darken_rate)
        
        # render the bottom bar
        self.__bottom_bar.render_image(screen_ins, self.__size_w, self.__size_h, contextDTO)
        
        # render the top bar
        self.__top_bar.render_image(screen_ins, self.__size_w, self.__size_h, contextDTO)
        
        if screen_status == StatusType_Enum.STATUS_MOVE:
            # in move
            new_moving_timer = self.render_characters_in_move(screen_ins, contextDTO, character_moving_timer)
            
        elif screen_status == StatusType_Enum.STATUS_COMBAT:
            # in combat
            '''
            @todo: render combat round count
            '''
            # render the combat round count
            
            
            # render the characters
            self.render_characters_in_combat(screen_ins, contextDTO)
            
            # render the enemies
            self.render_enemies_in_combat(screen_ins, contextDTO)
            
            # render the fighting image
            self.render_fighting(screen_ins, contextDTO)
        
        elif screen_status == StatusType_Enum.STATUS_CAMP:
            # in camp
            '''
            @todo: add method
            '''
            self.render_characters_in_camp(screen_ins, contextDTO)
        
        "FONT TESTING"
        self.render_font(screen_ins)
        
        return new_moving_timer
    
    
    def render_characters_in_move(self, screen_ins, contextDTO, character_moving_timer):
        
        new_moving_timer = 0
        
        # render the character
        if not contextDTO.get_active_team():
            return new_moving_timer
        characters = contextDTO.get_active_team().get_teammembers()
        
        # character move
        characters_move = contextDTO.get_contextDTO_InMap().get_characters_move()
        if character_moving_timer > 0:
            if not characters_move:
                # initialize characters_move
                characters_move = {}
                for temp_char in characters:
                    if not temp_char:
                        continue
                    # random a pace index for character's moving
                    random_pace_idx = random.randint(1,4)
                    characters_move[temp_char.get_character_name()] = random_pace_idx
                
                contextDTO.get_contextDTO_InMap().set_characters_move(characters_move)
            else:
                for temp_char in characters:
                    if not temp_char:
                        continue
                    character_name = temp_char.get_character_name()
                    if not character_name in characters_move.keys():
                        # random a pace index for character's moving
                        random_pace_idx = random.randint(1,4)
                        characters_move[temp_char.get_character_name()] = random_pace_idx
                        
                contextDTO.get_contextDTO_InMap().set_characters_move(characters_move)
        
        idx = 0
        for temp_char in characters:
            idx = idx + 1
            if not temp_char:
                continue
            
            character_name = temp_char.get_character_name()
            character_img = temp_char.get_stand_image()
            
            # get move image if necessary
            if character_moving_timer > 0:
                current_time = time.time()*1000
                current_pace_idx = characters_move[character_name]
                
                if not current_pace_idx:
                    current_pace_idx = random.randint(1,4)
                
                if current_time - character_moving_timer <= Scene_Constant.MOVE_PACE_TIMER_MAX:
                    character_img = temp_char.get_moving_image(current_pace_idx)
                else:
                    character_img, current_pace_idx = temp_char.get_next_moving_image_and_idx(current_pace_idx)
                    new_moving_timer = current_time
                
                characters_move[character_name] = current_pace_idx
                contextDTO.get_contextDTO_InMap().set_characters_move(characters_move)
            else:
                contextDTO.get_contextDTO_InMap().set_characters_move(None)
            
            # re-calculate character stand image position
            calc_w, calc_h = character_img.get_size()
            temp_prof_rate = temp_char.get_character_profession_rate()
            
            (x,y) = Image_Util.calculate_character_move_position_by_screen_size(self.__size_w, self.__size_h, idx, temp_prof_rate)
            self.__character_move_properties[idx]['position'] = (x,y)
            self.__character_move_properties[idx]['image_size'] = (0, 0, calc_w, calc_h)
            
            # render characters in move
            screen_ins.blit(character_img, (x,y), (0, 0, calc_w, calc_h))
            
        return new_moving_timer
            
             
    def render_characters_in_combat(self, screen_ins, contextDTO):
        # render the character
        if not contextDTO.get_active_team():
            return
        characters = contextDTO.get_active_team().get_teammembers()
        
        idx = 0
        for temp_char in characters:
            idx = idx + 1
            if not temp_char:
                continue
            
            # resize character stand image
            calc_h = Image_Util.calculate_character_combat_height_by_screen_size(self.__size_h)
            calc_w = Image_Util.calculate_character_combat_width_by_height(temp_char.get_stand_image(), calc_h)
            calc_in_fight_h = Image_Util.calculate_character_in_fight_height_by_screen_size(self.__size_h)
            calc_in_fight_w = Image_Util.calculate_character_combat_width_by_height(temp_char.get_fighting_image(), calc_in_fight_h)

            temp_char.resize_character_images_by_height(calc_h, calc_in_fight_h)
            temp_prof_rate = temp_char.get_character_profession_rate()
            
            # re-calculate character stand image position
            (x,y) = Image_Util.calculate_character_combat_position_by_screen_size(self.__size_w, self.__size_h, idx, temp_prof_rate)
            self.__character_combat_properties[idx]['position'] = (x,y)
            self.__character_combat_properties[idx]['image_size'] = (0, 0, calc_w, calc_h)
            
            if contextDTO.get_contextDTO_InCombat().get_current_selection() and \
               contextDTO.get_contextDTO_InCombat().get_current_selection().get_character_name() == temp_char.get_character_name():
                # skip the fighting character
                if contextDTO.get_contextDTO_InCombat().get_is_fight_in_round():
                    continue
                
                new_w, new_h = temp_char.get_stand_select_image().get_size()
                screen_ins.blit(temp_char.get_stand_select_image(), (x,y), (0, 0, new_w, new_h))
                
            elif contextDTO.get_contextDTO_InCombat().get_current_target() and \
                 contextDTO.get_contextDTO_InCombat().get_current_target().get_character_name() == temp_char.get_character_name():
                # skip the fighting character
                if contextDTO.get_contextDTO_InCombat().get_is_fight_in_round():
                    continue
            else:
                new_w, new_h = temp_char.get_stand_image().get_size()
                screen_ins.blit(temp_char.get_stand_image(), (x,y), (0, 0, new_w, new_h))
    
    
    def render_characters_in_camp(self, screen_ins, contextDTO):
        # render the character
        if not contextDTO.get_active_team():
            return
        characters = contextDTO.get_active_team().get_teammembers()
        
    
    def render_enemies_in_combat(self, screen_ins, contextDTO):             
        # render the character
        if not contextDTO.get_contextDTO_InCombat().get_active_enemies():
            return
        enemies = contextDTO.get_contextDTO_InCombat().get_active_enemies().get_teammembers()
        target_enemy_position = None
        is_valid_target_enemy = False
        
        idx = 0
        for temp_char in enemies:
            idx = idx + 1
            if not temp_char:
                continue
            
            # resize character
            calc_h = Image_Util.calculate_character_combat_height_by_screen_size(self.__size_h)
            calc_w = Image_Util.calculate_character_combat_width_by_height(temp_char.get_stand_image(), calc_h)
            calc_in_fight_h = Image_Util.calculate_character_in_fight_height_by_screen_size(self.__size_h)
            
            temp_char.resize_character_images_by_height(calc_h, calc_in_fight_h)
            temp_prof_rate = temp_char.get_character_enemy_type_rate()
            
            # re-calculate character position
            (x,y) = Image_Util.calculate_enemy_position_by_screen_size(self.__size_w, self.__size_h, idx, temp_prof_rate)
            self.__enemy_properties[idx]['position'] = (x,y)
            self.__enemy_properties[idx]['image_size'] = (0, 0, calc_w, calc_h)
            
            if contextDTO.get_contextDTO_InCombat().get_current_target() and \
               contextDTO.get_contextDTO_InCombat().get_current_target().get_character_name() == temp_char.get_character_name():
                # skip the fighting character
                if contextDTO.get_contextDTO_InCombat().get_is_fight_in_round():
                    continue
                
                target_enemy_position = (x,y)
                is_valid_target_enemy = True
            
            elif contextDTO.get_contextDTO_InCombat().get_current_selection() and \
                 contextDTO.get_contextDTO_InCombat().get_current_selection().get_character_name() == temp_char.get_character_name():
                # skip the fighting character
                if contextDTO.get_contextDTO_InCombat().get_is_fight_in_round():
                    continue
            else:
                new_w, new_h = temp_char.get_stand_image().get_size()
                screen_ins.blit(temp_char.get_stand_image(), (x,y), (0, 0, new_w, new_h))
        
        if not contextDTO.get_contextDTO_InCombat().get_is_fight_in_round() and \
           contextDTO.get_contextDTO_InCombat().get_current_target() and \
           is_valid_target_enemy == True:
            
            new_w, new_h = contextDTO.get_contextDTO_InCombat().get_current_target().get_stand_select_image().get_size()
            screen_ins.blit(contextDTO.get_contextDTO_InCombat().get_current_target().get_stand_select_image(), \
                            target_enemy_position, \
                            (0, 0, new_w, new_h))
    
    
    def render_fighting(self, screen_ins, contextDTO):
        # image timer
        current_time = time.time()*1000.0
        
        # in fight
        if contextDTO.get_contextDTO_InCombat().get_is_fight_in_round() and \
           contextDTO.get_contextDTO_InCombat().get_fighting_timer() > 0 and \
           current_time - contextDTO.get_contextDTO_InCombat().get_fighting_timer() <= Scene_Constant.FIGHTING_TIMER_MAX:
            '''
            Calculate attack result
            @todo: remove self.__is_fighting_in_round for skill calculation testing
            '''
            if not contextDTO.get_contextDTO_InCombat().get_is_fight_calculate():
                Fight_Util.calculate_fighting(contextDTO.get_contextDTO_InCombat().get_current_selection(), \
                                              contextDTO.get_contextDTO_InCombat().get_current_target(), \
                                              contextDTO.get_contextDTO_InCombat().get_current_select_skill())
                contextDTO.get_contextDTO_InCombat().set_is_fight_calculate(True)
                
            # render the character
            if contextDTO.get_active_team():
                characters = contextDTO.get_active_team().get_teammembers()
            
                idx = 0
                for temp_char in characters:
                    idx = idx + 1
                    if not temp_char:
                        continue
                    
                    if contextDTO.get_contextDTO_InCombat().get_current_selection() and \
                       contextDTO.get_contextDTO_InCombat().get_current_selection().get_character_name() == temp_char.get_character_name():
                        
                        temp_prof_rate = temp_char.get_character_profession_rate()
                        (calc_w, calc_h) = Image_Util.calculate_character_in_fight_position_by_screen_size(self.__size_w, self.__size_h, idx, temp_prof_rate)
                
                        screen_ins.blit(contextDTO.get_contextDTO_InCombat().get_current_selection().get_fighting_image(), (calc_w,calc_h))
                        break
                    
                    if contextDTO.get_contextDTO_InCombat().get_current_target() and \
                       contextDTO.get_contextDTO_InCombat().get_current_target().get_character_name() == temp_char.get_character_name():
                        
                        temp_prof_rate = temp_char.get_character_profession_rate()
                        (calc_w, calc_h) = Image_Util.calculate_character_in_fight_position_by_screen_size(self.__size_w, self.__size_h, idx, temp_prof_rate)
                
                        screen_ins.blit(contextDTO.get_contextDTO_InCombat().get_current_target().get_fighting_image(), (calc_w,calc_h))
                        break
            
            # render the enemy
            if contextDTO.get_contextDTO_InCombat().get_active_enemies():
                enemies = contextDTO.get_contextDTO_InCombat().get_active_enemies().get_teammembers()
            
                idx = 0
                for temp_char in enemies:
                    idx = idx + 1
                    if not temp_char:
                        continue
                
                    if contextDTO.get_contextDTO_InCombat().get_current_selection() and \
                       contextDTO.get_contextDTO_InCombat().get_current_selection().get_character_name() == temp_char.get_character_name():
                        
                        temp_prof_rate = temp_char.get_character_enemy_type_rate()
                        (calc_w, calc_h) = Image_Util.calculate_enemy_in_fight_position_by_screen_size(self.__size_w, self.__size_h, idx, temp_prof_rate)
                
                        screen_ins.blit(contextDTO.get_contextDTO_InCombat().get_current_selection().get_fighting_image(), (calc_w,calc_h))
                        break
                    
                    if contextDTO.get_contextDTO_InCombat().get_current_target() and \
                       contextDTO.get_contextDTO_InCombat().get_current_target().get_character_name() == temp_char.get_character_name():
                        
                        temp_prof_rate = temp_char.get_character_enemy_type_rate()
                        (calc_w, calc_h) = Image_Util.calculate_enemy_in_fight_position_by_screen_size(self.__size_w, self.__size_h, idx, temp_prof_rate)
                        
                        screen_ins.blit(contextDTO.get_contextDTO_InCombat().get_current_target().get_fighting_image(), (calc_w,calc_h))
                        break
            
            # render the skill effect
            if contextDTO.get_contextDTO_InCombat().get_current_select_skill():
                effect_img = contextDTO.get_contextDTO_InCombat().get_current_select_skill().get_effect_image()
                screen_ins.blit(effect_img, Image_Util.calculate_skill_effect_size_by_screen_size(self.__size_w, self.__size_h))
            
        else:
            if contextDTO.get_contextDTO_InCombat().get_fighting_timer() > 0 and \
               current_time - contextDTO.get_contextDTO_InCombat().get_fighting_timer() > Scene_Constant.FIGHTING_TIMER_MAX:
                # release select skill
                contextDTO.get_contextDTO_InCombat().set_current_select_skill(None)
            
            # initialize fighting in round properties
            contextDTO.get_contextDTO_InCombat().set_is_fight_in_round(False)
            contextDTO.get_contextDTO_InCombat().set_fighting_timer(0)
            contextDTO.get_contextDTO_InCombat().set_is_fight_calculate(False)
            
    
    def get_cover_character(self, cursor_x, cursor_y, contextDTO):
        if contextDTO.get_contextDTO_InCombat().get_is_fight_in_round():
            return
        
        for temp_idx in self.__character_combat_properties:
            temp_char = self.__character_combat_properties[temp_idx]
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
                if temp_char['enemy']:
                    print(temp_char['enemy'].get_character_name())
                if contextDTO.get_contextDTO_InCombat().get_current_select_skill():
                    contextDTO.get_contextDTO_InCombat().set_current_target(temp_char['enemy'])
                    break
                else:
                    contextDTO.get_contextDTO_InCombat().set_current_target(None)
            else:
                contextDTO.get_contextDTO_InCombat().set_current_target(None)
        
    
    def render_font(self, sceneInst):
        font1 = pygame.font.SysFont('arial', 16)
        text = font1.render("Room change !!!",True,(255, 255, 255))
        
        textRectObj = text.get_rect()
        textRectObj.center = (200, 150)
        
        sceneInst.blit(text, textRectObj)