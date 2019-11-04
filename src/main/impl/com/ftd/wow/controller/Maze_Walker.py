'''
Created on Oct 16, 2019

@author: ftd
'''

from src.main.impl.com.ftd.wow.util.Map_Util import Map_Util
    
    
class Maze_Walker(object):
    '''
    
    '''
    
    def __init__(self):
        self.__map = None
        
        
    def generate_map(self, map_size):
        self.__map = Map_Util.generate_random_map(map_size)

