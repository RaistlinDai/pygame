'''
Created on Oct 10, 2019

@author: ftd
'''
from src.main.impl.com.ftd.wow.scene.FightScene_Enum import FightScene_Enum
from src.main.api.com.ftd.wow.controller.IController import IController
import time
from src.main.impl.com.ftd.wow.controller.Combat_Judgment import Combat_Judgment

class Abyss_Overlord(IController):
    '''
    
    '''
    
    def __init__(self, resourceDTO):
        super().__init__()
        self.__current_scene = resourceDTO.get_scene(FightScene_Enum.MC_BOSS_10.name)
        
        # combat judgment
        self.__combat_judgment = Combat_Judgment()
        

    def get_current_scene(self):
        return self.__current_scene


    def set_current_scene(self, value):
        self.__current_scene, value
        
    
    def get_current_scene_bottom_bar(self):
        return self.__current_scene.get_bottom_bar()
    
    
    def set_current_scene_bottom_bar(self, value):
        self.__current_scene.set_bottom_bar(value)
        
    
    def render_scene(self, screen_ins, contextDTO):
        # re-load the character to background
        self.available_active_team(contextDTO)
        self.available_active_enemies(contextDTO)
        
        '''
        @todo: trigger the combat and start Combat_Judgment
        '''
        if not self.__combat_judgment.get_is_start_combat():
            self.start_combat(contextDTO)
        
        temp_status = None
        if self.__combat_judgment.get_is_start_combat():
            temp_status = "COMBAT"
            
        # render the background & characters
        temp_scene = self.get_current_scene()
        temp_scene.render(screen_ins, contextDTO.get_screen_width(), contextDTO.get_screen_height(), contextDTO, temp_status)
        
    
    def start_combat(self, contextDTO):
        # mark combat flag in contextDTO
        contextDTO.get_ContextDto_InCombat().set_in_fight(True)
        # trigger the combat judgment
        self.__combat_judgment.set_is_start_combat(True)
        # initialize the combat judgment
        self.__combat_judgment.initialize(contextDTO.get_ContextDto_InCombat().get_active_team().get_teammembers, \
                                          contextDTO.get_ContextDto_InCombat().get_active_enemies().get_teammembers())
        
        '''
        @todo: Combat_Judgment generate the order list and the current character
        '''
        # set the current character
        self.set_current_character(contextDTO)
        
        
    def close_combat(self):
        # close the combat judgment
        self.__combat_judgment.set_is_start_as_False()
        
            
    def available_active_team(self, contextDTO):
        active_team = contextDTO.get_ContextDto_InCombat().get_active_team()
        temp_character_properties = self.__current_scene.get_character_properties()
        if active_team:
            idx = 0
            characters = active_team.get_teammembers()
            for temp_char in characters:
                idx = idx + 1
                if temp_char:
                    temp_character_properties[idx]['character'] = temp_char
        self.__current_scene.set_character_properties(temp_character_properties)
    
    
    def available_active_enemies(self, contextDTO):
        active_enemies = contextDTO.get_ContextDto_InCombat().get_active_enemies()
        temp_enemy_properties = self.__current_scene.get_enemy_properties()
        if active_enemies:
            idx = 0
            for temp_char in active_enemies.get_teammembers():
                idx = idx + 1
                if temp_char:
                    temp_enemy_properties[idx]['enemy'] = temp_char
        self.__current_scene.set_enemy_properties(temp_enemy_properties)
                    
        
    def set_current_character(self, contextDTO):
        current_character = contextDTO.get_ContextDto_InCombat().get_active_team().get_teammember04()
        contextDTO.get_ContextDto_InCombat().set_current_selection(current_character)
        self.get_current_scene_bottom_bar().set_current_character(current_character)
            
            
    # ========================================================== #
    #                         Event                              #
    # ========================================================== #
    def mouse_click_event(self, pressed_mouse, contextDTO):
        super().mouse_click_event(pressed_mouse, contextDTO)
        
        '''
        if pressed_mouse[0]:
            if self.get_active_enemies().get_current_select_skill() and self.__current_target:
                # trigger fighting image
                self.__is_fighting = True
                self.__fighting_timer = time.time()*1000.0
        
        # bottom bar click event
        self.get_active_enemies().mouse_click_event(pressed_mouse)
        '''
    
    
    def cursor_event(self, cursor_x, cursor_y, contextDTO):
        self.__current_scene.get_cover_character(cursor_x, cursor_y, contextDTO)
        # bottom bar
        self.get_current_scene_bottom_bar().render_cover_skill(cursor_x, cursor_y)