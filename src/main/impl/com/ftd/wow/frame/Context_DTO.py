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
        self.__active_team = None


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


    def get_active_team(self):
        return self.__active_team


    def set_active_team(self, value):
        self.__active_team = value



class Context_DTO_InMap(object):
    
    def __init__(self):
        self.__map_size = None
        self.__map = None
        self.__map_position = None
        self.__map_next_room = None
        " the characters pace index list "
        self.__characters_move = None
        
    
    def get_map_size(self):
        return self.__map_size


    def set_map_size(self, value):
        self.__map_size = value
    
    
    def get_map(self):
        return self.__map


    def set_map(self, value):
        self.__map = value
        
    
    def get_map_position(self):
        return self.__map_position


    def set_map_position(self, value):
        self.__map_position = value
        
    
    def get_map_next_room(self):
        return self.__map_next_room


    def set_map_next_room(self, value):
        self.__map_next_room = value
    
    
    def get_characters_move(self):
        return self.__characters_move


    def set_characters_move(self, value):
        self.__characters_move = value
        
    
    def clear_map(self):
        self.__map_size = None
        self.__map = None
        self.__map_position = None
        self.__map_next_room = None
        self.__character_pace_idx = None
    
    
class Context_DTO_InCombat(object):
    
    def __init__(self):
        self.__active_enemies = None
        self.__combat = False

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


    def get_combat(self):
        return self.__combat


    def set_combat(self, value):
        self.__combat = value
    
    
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