'''
Created on Oct 10, 2019

@author: ftd
'''
from src.main.impl.com.ftd.wow.scene.base.SceneMode_Enum import SceneMode_Enum
from src.main.api.com.ftd.wow.controller.ILeader import ILeader
from src.main.impl.com.ftd.wow.controller.Login_Guide import Login_Guide
from src.main.impl.com.ftd.wow.controller.Abyss_Overlord import Abyss_Overlord

class Big_Boss(object):
    '''
    
    '''
    
    def __init__(self, resourceDTO):
        self.__current_leader = None
        self.__current_scene_mode = None
        self.__resource_DTO = resourceDTO


    def get_current_scene(self):
        return self.__current_leader.get_current_scene()


    def get_current_scene_mode(self):
        return self.__current_scene_mode


    def get_current_leader(self):
        return self.__current_leader
    

    def set_current_scene(self, value):
        self.__current_leader.set_current_scene(value)


    def set_current_scene_mode(self, value):
        self.__current_scene_mode = value
        

    def set_current_leader(self, value):
        if isinstance(value, ILeader):
            self.__current_leader = value
        else:
            self.__current_leader = None


    def del_current_scene(self):
        del self.__current_scene


    def del_current_scene_mode(self):
        del self.__current_scene_mode


    current_scene = property(get_current_scene, set_current_scene, del_current_scene, "current_scene's docstring")
    current_scene_mode = property(get_current_scene_mode, set_current_scene_mode, del_current_scene_mode, "current_scene_mode's docstring")
    
    
    def update_leader(self, scene_mode=None):
        self.__current_scene_mode = scene_mode
        
        if self.__current_scene_mode:
            # disable the current leader
            if self.__current_leader:
                self.__current_leader.fall_asleep_leader()
                
            if self.__current_scene_mode == SceneMode_Enum.MENU_SCENE:
                self.__current_leader = Login_Guide(self.__resource_DTO)
                self.__current_leader.wake_up_leader()
                
            elif self.__current_scene_mode == SceneMode_Enum.FIGHT_SCENE:
                self.__current_leader = Abyss_Overlord(self.__resource_DTO)
                self.__current_leader.wake_up_leader()
        else:
            self.__current_leader = None
    
    
    def wakeup_next_leader(self):
        '''
        @todo: complete the whole scene flow: MENU_SCENE -> Loop: <CITY_SCENE -> PREPARE_SCENE -> FIGHT_SCENE>
        '''
        if not self.__current_leader.get_in_hibernation():
            return
        
        if self.__current_scene_mode:
            if self.__current_scene_mode == SceneMode_Enum.MENU_SCENE:
                self.__current_scene_mode = SceneMode_Enum.FIGHT_SCENE
                self.__current_leader = Abyss_Overlord(self.__resource_DTO)
                self.__current_leader.wake_up_leader()
                
    
    def render_scene(self, screen_ins, contextDTO):
        if not self.__current_leader:
            return False, 'No leader available!'
        
        if not self.__current_leader.get_current_scene():
            return False, 'No available scene for the current leader!'
        
        if not self.__current_leader.render_scene:
            return False, 'Scene renderer is not valid!'
        
        # arrange render task to current leader
        self.__current_leader.render_scene(screen_ins, contextDTO)
    
    
    def event_mouse_click(self, pressed_mouse):
        if not self.__current_leader:
            return False, 'No leader available!'
        
        if not self.__current_leader.get_current_scene():
            return False, 'No available scene for the current leader!'
        
        if not self.__current_leader.mouse_click_event:
            return False, 'Scene mouse click event is not valid!'
        
        # arrange event task to current leader
        self.__current_leader.mouse_click_event(pressed_mouse)