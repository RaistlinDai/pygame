'''
Created on Oct 16, 2019

@author: ftd
'''

from src.main.impl.com.ftd.wow.util.Map_Util import Map_Util
    
    
class Maze_Walker(object):
    '''
    
    '''
    
    CELL_SIZE = 10
    
    def __init__(self):
        self.__map = None
        self._current_position = (None, 0, 0)     # MapCell, cell_position: 0-10, direction: 4/N,3/S,2/W,1/E
        
        
    def generate_map(self, map_size):
        self.__map = Map_Util.generate_random_map(map_size)

        
    def get_map(self):
        return self.__map
    
        
    def set_current_position(self, value):
        self._current_position = value
        
        
    def get_current_position(self):
        return self._current_position