'''
Created on Oct 10, 2019

@author: ftd
'''
from src.main.impl.com.ftd.wow.scene.FightScene_Enum import FightScene_Enum
from src.main.api.com.ftd.wow.controller.ILeader import ILeader
import time

class Abyss_Overlord(ILeader):
    '''
    
    '''
    
    def __init__(self, resourceDTO):
        super().__init__()
        self.__current_scene = resourceDTO.get_scene(FightScene_Enum.MC_BOSS_10.name)
        
        
        '''
         re-load the background
        self.__manager.get_current_scene().add_active_team(self.__context_DTO.get_active_team())
        self.__manager.get_current_scene().set_current_character(load_characters[1])
        
        self.__context_DTO.set_in_fight(True)
        if self.__context_DTO.get_in_fight() == True:
            self.__manager.get_current_scene().add_active_enemies(self.__context_DTO.get_active_enemies())
        
         Mouse cursor event
        self.__manager.get_current_scene().cursor_event(cursor_x, cursor_y)
            '''


    def get_current_scene(self):
        return self.__current_scene


    def set_current_scene(self, value):
        self.__current_scene, value
        
    
    def render_scene(self, screen_ins, contextDTO):
        # clocker
        current_timer = time.time()*1000.0
        
        temp_scene = self.get_current_scene()
        # render the button & determine the background
        if (not super().get_is_going_hibernate() and not super().get_in_hibernation()):
            temp_scene.render(screen_ins, contextDTO.get_screen_width(), contextDTO.get_screen_height())
        elif (super().get_is_going_hibernate() and not super().get_in_hibernation()):
            if (self.__button_click_timer > 0 and current_timer - self.__button_click_timer < 2000):
                temp_scene.render(screen_ins, contextDTO.get_screen_width(), contextDTO.get_screen_height(), True)
            elif (current_timer - self.__button_click_timer >= 2000):
                super().set_is_going_hibernate(False)
                super().set_in_hibernation(True)
        else:
            return