'''
Created on Oct 10, 2019

@author: ftd
'''
from src.main.impl.com.ftd.wow.scene.MenuScene_Enum import MenuScene_Enum
from src.main.impl.com.ftd.wow.scene.base.SceneMode_Enum import SceneMode_Enum

class Scene_Manager(object):
    '''
    
    '''
    
    def __init__(self):
        self.__current_scene = None
        self.__current_scene_mode = None


    def get_current_scene(self):
        return self.__current_scene


    def get_current_scene_mode(self):
        return self.__current_scene_mode


    def set_current_scene(self, value):
        self.__current_scene = value


    def set_current_scene_mode(self, value):
        self.__current_scene_mode = value


    def del_current_scene(self):
        del self.__current_scene


    def del_current_scene_mode(self):
        del self.__current_scene_mode


    current_scene = property(get_current_scene, set_current_scene, del_current_scene, "current_scene's docstring")
    current_scene_mode = property(get_current_scene_mode, set_current_scene_mode, del_current_scene_mode, "current_scene_mode's docstring")
    
    
    def change_to_next_scene(self):
        '''
        @todo: complete the whole scene flow: MENU_SCENE -> LOAD_SCENE -> Loop: <CITY_SCENE -> PREPARE_SCENE -> FIGHT_SCENE>
        '''
        temp_scene = None
        if self.__current_scene:
            if self.__current_scene == SceneMode_Enum.MENU_SCENE:
                self.__current_scene_mode = SceneMode_Enum.FIGHT_SCENE
                
                