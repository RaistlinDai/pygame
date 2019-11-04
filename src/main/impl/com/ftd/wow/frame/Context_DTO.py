'''
Created on Sep 17, 2019

@author: ftd
'''

class Context_DTO(object):
    '''
    
    '''
    
    def __init__(self):
        self.__screen_width = 1280
        self.__screen_height = 720
        
        self.__contextDto_InMap = Context_DTO_InMap()
        self.__contextDto_InCombat = Context_DTO_InCombat()


    def get_screen_height(self):
        return self.__screen_height


    def set_screen_height(self, value):
        self.__screen_height = value


    def del_screen_height(self):
        del self.__screen_height


    def get_screen_width(self):
        return self.__screen_width


    def set_screen_width(self, value):
        self.__screen_width = value


    def del_screen_width(self):
        del self.__screen_width


    def get_ContextDto_InCombat(self):
        return self.__contextDto_InCombat


    def set_ContextDto_InCombat(self, value):
        self.__contextDto_InCombat = value


    def get_ContextDto_InMap(self):
        return self.__contextDto_InMap


    def set_ContextDto_InMap(self, value):
        self.__contextDto_InMap = value
        

    screen_size = property(get_screen_width, set_screen_width, del_screen_width, "screen_width's docstring")
    screen_height = property(get_screen_height, set_screen_height, del_screen_height, "screen_height's docstring")



class Context_DTO_InMap(object):
    
    def __init__(self):
        self.__map_size = None
    
    def get_map_size(self):
        return self.__map_size


    def set_map_size(self, value):
        self.__map_size = value
    
    
    
class Context_DTO_InCombat(object):
    
    def __init__(self):
        self.__active_team = None
        self.__active_enemies = None
        self.__in_fight = False

        self.__current_selection = None
        self.__current_target = None
        self.__current_target_extension = []
        
        # cover skill
        self.__current_cover_skill = None
        # select skill
        self.__current_select_skill = None
        
        # is fight in round
        self.__is_fight_in_round = False
        self.__fighting_timer = 0
        self.__is_fight_calculate = False
        
    
    def get_active_enemies(self):
        return self.__active_enemies


    def set_active_enemies(self, value):
        self.__active_enemies = value


    def get_active_team(self):
        return self.__active_team


    def set_active_team(self, value):
        self.__active_team = value


    def get_in_fight(self):
        return self.__in_fight


    def set_in_fight(self, value):
        self.__in_fight = value
    
    
    def get_current_selection(self):
        return self.__current_selection


    def set_current_selection(self, value):
        self.__current_selection = value
    
    
    def get_current_target(self):
        return self.__current_target


    def set_current_target(self, value):
        self.__current_target = value
    
    
    def get_current_target_extension(self):
        return self.__current_target_extension


    def set_current_target_extension(self, value):
        self.__current_target_extension = value
    
    
    def get_current_cover_skill(self):
        return self.__current_cover_skill


    def set_current_select_skill(self, value):
        self.__current_select_skill = value
    
    
    def get_current_select_skill(self):
        return self.__current_select_skill


    def set_current_cover_skill(self, value):
        self.__current_cover_skill = value
    
    
    def get_is_fight_in_round(self):
        return self.__is_fight_in_round


    def set_is_fight_in_round(self, value):
        self.__is_fight_in_round = value
    
    
    def get_fighting_timer(self):
        return self.__fighting_timer


    def set_fighting_timer(self, value):
        self.__fighting_timer = value
    
    
    def get_is_fight_calculate(self):
        return self.__is_fight_calculate


    def set_is_fight_calculate(self, value):
        self.__is_fight_calculate = value