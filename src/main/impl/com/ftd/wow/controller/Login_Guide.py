'''
Created on Oct 10, 2019

@author: ftd
'''
from src.main.impl.com.ftd.wow.scene.MenuScene_Enum import MenuScene_Enum
from src.main.api.com.ftd.wow.controller.ILeader import ILeader
import time

class Login_Guide(ILeader):
    '''
    
    '''
    
    def __init__(self, resourceDTO):
        super().__init__()
        self.__current_scene = resourceDTO.get_scene(MenuScene_Enum.HORDE_LOGIN.name)
        
        self.__button_click_timer = 0
        

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
            temp_scene.render(screen_ins, contextDTO.get_screen_width(), contextDTO.get_screen_height(), False)
        elif (super().get_is_going_hibernate() and not super().get_in_hibernation()):
            if (self.__button_click_timer > 0 and current_timer - self.__button_click_timer < 2000):
                temp_scene.render(screen_ins, contextDTO.get_screen_width(), contextDTO.get_screen_height(), True)
            elif (current_timer - self.__button_click_timer >= 2000):
                super().set_is_going_hibernate(False)
                super().set_in_hibernation(True)
        else:
            return
        

    def is_in_hiberation(self):
        return super().get_in_hibernation()

    # ========================================================== #
    #                         Event                              #
    # ========================================================== #
    def mouse_click_event(self, pressed_mouse):
        if pressed_mouse[0]:
            if self.__current_scene.is_button_cover() and not super().get_is_going_hibernate() and not super().get_in_hibernation():
                # trigger scene loading
                super().set_is_going_hibernate(True)
                self.__button_click_timer = time.time()*1000.0
    
    
    def cursor_event(self, cursor_x, cursor_y):
        self.get_cover_character(cursor_x, cursor_y)
        # bottom bar
        self.__bottom_bar.render_cover_skill(cursor_x, cursor_y)
        