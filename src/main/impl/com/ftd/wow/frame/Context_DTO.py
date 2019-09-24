'''
Created on Sep 17, 2019

@author: ftd
'''

class Context_DTO(object):
    '''
    
    '''
    
    def __init__(self):
        self.__active_team = None
        self.__active_enemies = None
        self.__current_scene = None
        self.__current_scene_mode = None
        self.__screen_width = 1280
        self.__screen_height = 720
        self.__in_fight = False


    def get_active_enemies(self):
        return self.__active_enemies


    def set_active_enemies(self, value):
        self.__active_enemies = value


    def del_active_enemies(self):
        del self.__active_enemies


    def get_in_fight(self):
        return self.__in_fight


    def set_in_fight(self, value):
        self.__in_fight = value


    def del_in_fight(self):
        del self.__in_fight


    def get_current_scene_mode(self):
        return self.__current_scene_mode


    def set_current_scene_mode(self, value):
        self.__current_scene_mode = value


    def del_current_scene_mode(self):
        del self.__current_scene_mode


    def get_screen_height(self):
        return self.__screen_height


    def set_screen_height(self, value):
        self.__screen_height = value


    def del_screen_height(self):
        del self.__screen_height


    def get_active_team(self):
        return self.__active_team


    def get_current_scene(self):
        return self.__current_scene


    def get_screen_width(self):
        return self.__screen_width


    def set_active_team(self, value):
        self.__active_team = value


    def set_current_scene(self, value):
        self.__current_scene = value


    def set_screen_width(self, value):
        self.__screen_width = value


    def del_active_team(self):
        del self.__active_team


    def del_current_scene(self):
        del self.__current_scene


    def del_screen_width(self):
        del self.__screen_width


    active_team = property(get_active_team, set_active_team, del_active_team, "active_team's docstring")
    current_scene = property(get_current_scene, set_current_scene, del_current_scene, "current_scene's docstring")
    screen_size = property(get_screen_width, set_screen_width, del_screen_width, "screen_width's docstring")
    screen_height = property(get_screen_height, set_screen_height, del_screen_height, "screen_height's docstring")
    current_scene_mode = property(get_current_scene_mode, set_current_scene_mode, del_current_scene_mode, "current_scene_mode's docstring")
    in_fight = property(get_in_fight, set_in_fight, del_in_fight, "in_fight's docstring")
    active_enemies = property(get_active_enemies, set_active_enemies, del_active_enemies, "active_enemies's docstring")
        
    