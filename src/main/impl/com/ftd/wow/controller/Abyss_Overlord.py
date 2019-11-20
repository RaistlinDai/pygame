'''
Created on Oct 10, 2019

@author: ftd
'''
from src.main.impl.com.ftd.wow.scene.FightScene_Enum import FightScene_Enum
from src.main.api.com.ftd.wow.controller.IController import IController
import time
from src.main.impl.com.ftd.wow.controller.Combat_Judgment import Combat_Judgment
from src.main.impl.com.ftd.wow.controller.Maze_Walker import Maze_Walker
from enum import Enum, unique

@unique
class StatusType_Enum(Enum):
    '''
    classdocs
    @attention: the status in Abyss
    '''
    
    STATUS_COMBAT = "COMBAT"
    STATUS_MOVE = "MOVE"
    STATUS_CAMP = "CAMP"
    
    
class Abyss_Overlord(IController):
    '''
    
    '''
    
    def __init__(self, resourceDTO):
        super().__init__()
        # maze walker
        self.__maze_walker = Maze_Walker()
        # combat judgment
        self.__combat_judgment = Combat_Judgment()
        # scene changing timer
        self.__scene_changing_timer = 0
        
        self.__current_scene = resourceDTO.get_scene(FightScene_Enum.MC_BOSS_10.name)
        

    def get_current_scene(self):
        return self.__current_scene


    def set_current_scene(self, value):
        self.__current_scene, value
        
    
    def get_current_scene_bottom_bar(self):
        return self.__current_scene.get_bottom_bar()
    
    
    def set_current_scene_bottom_bar(self, value):
        self.__current_scene.set_bottom_bar(value)
    
    
    def wake_up_controller(self, contextDto=None):
        super().wake_up_controller(contextDto)
        # active Maze_Walker
        if contextDto:
            self.__maze_walker.wake_up_controller(contextDto)
        
    
    def render_scene(self, screen_ins, contextDTO):
        
        # calculate scene changing timer
        if self.__scene_changing_timer > 0:
            current_time = time.time()*1000.0
            if current_time - self.__scene_changing_timer < 2000:
                pass
            else:
                self.__scene_changing_timer = 0 
                
        # re-load the character to background
        self.available_active_team(contextDTO)
        
        '''
        @todo: trigger the combat and start Combat_Judgment
        
        if not self.__combat_judgment.get_is_start_combat():
            self.start_combat(contextDTO)
        '''
        
        temp_status = StatusType_Enum.STATUS_MOVE
        if self.__combat_judgment.get_is_start_combat():
            temp_status = StatusType_Enum.STATUS_COMBAT
            
        # render the background & characters
        temp_scene = self.get_current_scene()
        temp_scene.render(screen_ins, contextDTO.get_screen_width(), contextDTO.get_screen_height(), contextDTO, temp_status)
        
    
    def start_combat(self, contextDTO):
        '''
        @todo: load enemies
        '''
        self.available_active_enemies(contextDTO)
        
        # mark combat flag in contextDTO
        contextDTO.get_ContextDto_InCombat().set_combat(True)
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
            
            
    # ========================================================== #
    #                         Event                              #
    # ========================================================== #
    def mouse_click_event(self, pressed_mouse, contextDTO):
        '''
        Mouse click event
        '''
        super().mouse_click_event(pressed_mouse, contextDTO)
        
        if pressed_mouse[0]:
            
            if contextDTO.get_ContextDto_InCombat().get_current_cover_skill():
                temp_skill = contextDTO.get_ContextDto_InCombat().get_current_cover_skill()
                contextDTO.get_ContextDto_InCombat().set_current_select_skill(temp_skill)
            else:
                pass
            
            if contextDTO.get_ContextDto_InCombat().get_current_select_skill() and \
               contextDTO.get_ContextDto_InCombat().get_current_target():
                # trigger fighting image
                contextDTO.get_ContextDto_InCombat().set_is_fight_in_round(True)
                contextDTO.get_ContextDto_InCombat().set_fighting_timer(time.time()*1000.0)
        
        elif pressed_mouse[2]:
            if contextDTO.get_ContextDto_InCombat().get_current_select_skill():
                contextDTO.get_ContextDto_InCombat().set_current_select_skill(None)
    
    
    def event_keyboard_keydown(self, move_a, move_d, move_w, move_s, contextDTO):
        '''
        Keyboard event
        '''
        # ignore keyboard event once changing the scene
        if self.__scene_changing_timer > 0:
            return 
        
        super().event_keyboard_keydown(move_a, move_d, move_w, move_s, contextDTO)

        if not self.__maze_walker.get_in_hibernation():
            # characters move in map
            self.__scene_changing_timer, error_msg = \
                self.__maze_walker.manage_characters_move_in_map(move_a, move_d, move_w, move_s, contextDTO)

    
    def cursor_event(self, cursor_x, cursor_y, contextDTO):
        '''
        Cursor event
        '''
        # cover character
        self.get_current_scene().get_cover_character(cursor_x, cursor_y, contextDTO)
        # cover skill
        self.get_current_scene_bottom_bar().get_cover_skill(cursor_x, cursor_y, contextDTO)