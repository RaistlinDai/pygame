import random
from enum import Enum, unique


class Map_DTO(object):
    '''
    Map_DTO include the cell_list, format is [[pos_x, pos_y],[....]....]
    '''
    
    def __init__(self, map_size):
        self.__map_size = map_size
        self.__cell_list = []
        self.__current_cell = 0
    

class Cell_DTO(object):
    '''
    
    '''
    
    def __init__(self, pos_x=0, pox_y=0, cell_type=None):
        self.__pos_x = pos_x
        self.__pos_y = pox_y
        self.__size = 10
        
        self.__type = cell_type
        
        self.__has_enemy = False
        self.__enemy_team = None
        
        self.__special_event = None
        
        self.__nearby_cells = []
    
    
    def get_pos_x(self):
        return self.__pos_x
    
    
    def set_pos_x(self, value):
        self.__pos_x = value
        
    
    def get_pos_y(self):
        return self.__pos_y
    
    
    def set_pos_y(self, value):
        self.__pos_y = value
        
        
    def get_type(self):
        return self.__type
    
    
    def set_type(self, value):
        self.__type = value
        

    def get_nearby_cells(self):
        return self.__nearby_cells
    
    
    def set_nearby_cells(self, value):
        self.__nearby_cells = value
        
    
    def append_nearby_cells(self, value):
        self.__nearby_cells.append(value)