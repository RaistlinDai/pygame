'''
Created on Oct 09, 2019

@author: ftd
'''

class Combat_Judgment(object):
    '''
    This is the Judgment for Combat round, 
    it will determine the characters' orders, damages, mental stress, body injury and all other affects.
    '''
    
    def __init__(self,):
        '''
        
        '''
        # Judgment is start or not
        self.__is_start_combat = False
        # round count
        self.__round_count = 0
        # all characters in fighting
        self.__all_characters = []
        # character order list
        self.__order_list = []
        # the current active character
        self.__current_active_character = None


    def initialize(self, group1, group2):
        self.__round_count = 0
        temp_list = group1
        
        if group1 and group2 and isinstance(group1, list) and isinstance(group2, list):
            for item in group2:
                temp_list.append(item)
        self.__all_characters = temp_list
        self.__order_list = []
        self.__current_active_character = None
    
    
    def order_combat_characters(self):
        '''
        Once the __order_list is empty, then re-order the whole characters into array list
        '''
        if len(self.__order_list) > 0:
            return
        
        if self.__all_characters and isinstance(self.__all_characters, list):
            '''
            @todo: calculate order list
            '''
            pass


    def set_is_start_combat(self, value):
        self.__is_start_combat = value
        

    def get_is_start_combat(self):
        return self.__is_start_combat


    def get_round_count(self):
        return self.__round_count


    def get_all_characters(self):
        return self.__all_characters


    def get_order_list(self):
        return self.__order_list


    def get_current_active_character(self):
        return self.__current_active_character
        

    def set_round_count(self, value):
        self.__round_count = value


    def set_all_characters(self, value):
        self.__all_characters = value


    def set_order_list(self, value):
        self.__order_list = value


    def set_current_active_character(self, value):
        self.__current_active_character = value


    def del_is_start_combat(self):
        del self.__is_start_combat


    def del_round_count(self):
        del self.__round_count


    def del_all_characters(self):
        del self.__all_characters


    def del_order_list(self):
        del self.__order_list


    def del_current_active_character(self):
        del self.__current_active_character


    is_start = property(get_is_start_combat, None, del_is_start_combat, "is_start's docstring")
    round_count = property(get_round_count, set_round_count, del_round_count, "round_count's docstring")
    all_characters = property(get_all_characters, set_all_characters, del_all_characters, "all_characters's docstring")
    order_list = property(get_order_list, set_order_list, del_order_list, "order_list's docstring")
    current_active_character = property(get_current_active_character, set_current_active_character, del_current_active_character, "current_active_character's docstring")
        
        