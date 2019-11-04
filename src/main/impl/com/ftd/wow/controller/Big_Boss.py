'''
Created on Oct 10, 2019

@author: ftd
'''
from src.main.impl.com.ftd.wow.scene.base.SceneMode_Enum import SceneMode_Enum
from src.main.api.com.ftd.wow.controller.IController import IController
from src.main.impl.com.ftd.wow.controller.Login_Guide import Login_Guide
from src.main.impl.com.ftd.wow.controller.Abyss_Overlord import Abyss_Overlord
from src.main.impl.com.ftd.wow.controller.Maze_Walker import MapSize_Enum

class Big_Boss(object):
    '''
    
    '''
    
    def __init__(self, resourceDTO):
        self.__current_controller = None
        self.__current_scene_mode = None
        self.__resource_DTO = resourceDTO


    def get_current_scene(self):
        return self.__current_controller.get_current_scene()


    def get_current_scene_mode(self):
        return self.__current_scene_mode


    def get_current_controller(self):
        return self.__current_controller
    

    def set_current_scene(self, value):
        self.__current_controller.set_current_scene(value)


    def set_current_scene_mode(self, value):
        self.__current_scene_mode = value
        

    def set_current_controller(self, value):
        if isinstance(value, IController):
            self.__current_controller = value
        else:
            self.__current_controller = None


    def del_current_scene(self):
        del self.__current_scene


    def del_current_scene_mode(self):
        del self.__current_scene_mode


    current_scene = property(get_current_scene, set_current_scene, del_current_scene, "current_scene's docstring")
    current_scene_mode = property(get_current_scene_mode, set_current_scene_mode, del_current_scene_mode, "current_scene_mode's docstring")
    
    
    def update_controller(self, contextDTO, scene_mode=None):
        self.__current_scene_mode = scene_mode
        
        if self.__current_scene_mode:
            # disable the current leader
            if self.__current_controller:
                self.__current_controller.fall_asleep_controller()
                
            if self.__current_scene_mode == SceneMode_Enum.MENU_SCENE:
                self.__current_controller = Login_Guide(self.__resource_DTO)
                self.__current_controller.wake_up_controller()
                
            elif self.__current_scene_mode == SceneMode_Enum.FIGHT_SCENE:
                self.__current_controller = Abyss_Overlord(self.__resource_DTO)
                self.__current_controller.wake_up_controller(contextDTO)
        else:
            self.__current_controller = None
    
    
    def wakeup_next_controller(self, contextDTO):
        '''
        @todo: complete the whole scene flow: MENU_SCENE -> Loop: <CITY_SCENE -> PREPARE_SCENE -> FIGHT_SCENE>
        '''
        if not self.__current_controller.get_in_hibernation():
            return
        
        if self.__current_scene_mode:
            if self.__current_scene_mode == SceneMode_Enum.MENU_SCENE:
                self.__current_scene_mode = SceneMode_Enum.FIGHT_SCENE
                self.__current_controller = Abyss_Overlord(self.__resource_DTO)
                '''
                @todo: set map size
                '''
                contextDTO.get_ContextDto_InMap().set_map_size(MapSize_Enum.SIZE_SMALL)
                self.__current_controller.wake_up_controller(contextDTO)
                
    
    def render_scene(self, screen_ins, contextDTO):
        if not self.__current_controller:
            return False, 'No leader available!'
        
        if not self.__current_controller.get_current_scene():
            return False, 'No available scene for the current leader!'
        
        if not self.__current_controller.render_scene:
            return False, 'Scene renderer is not valid!'
        
        # arrange render task to current leader
        self.__current_controller.render_scene(screen_ins, contextDTO)
    
    
    # ========================================================== #
    #                         Event                              #
    # ========================================================== #
    def event_mouse_click(self, pressed_mouse, contextDTO):
        if not self.__current_controller:
            return False, 'No leader available!'
        
        if not self.__current_controller.get_current_scene():
            return False, 'No available scene for the current leader!'
        
        if not self.__current_controller.mouse_click_event:
            return False, 'Scene mouse click event is not valid!'
        
        # arrange event task to current leader
        self.__current_controller.mouse_click_event(pressed_mouse, contextDTO)
        
    
    def event_cursor(self, cursor_x, cursor_y, contextDTO):
        if not self.__current_controller:
            return False, 'No leader available!'
        
        if not self.__current_controller.get_current_scene():
            return False, 'No available scene for the current leader!'
        
        # arrange event task to current leader
        self.__current_controller.cursor_event(cursor_x, cursor_y, contextDTO)