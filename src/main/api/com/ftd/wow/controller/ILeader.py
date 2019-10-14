'''
Created on Oct 11, 2019

@author: ftd
'''

class ILeader(object):
    '''
    
    '''
    
    def __init__(self):
        self.__is_going_hibernate = False
        self.__in_hibernation = True
    
    
    def wake_up_leader(self):
        self.__in_hibernation = False
    
    
    def fall_asleep_leader(self):
        self.__in_hibernation = True
        
    
    def get_in_hibernation(self):
        return self.__in_hibernation
        
    
    def set_in_hibernation(self, value):
        self.__in_hibernation = value
        
        
    def get_is_going_hibernate(self):
        return self.__is_going_hibernate
    
    
    def set_is_going_hibernate(self, value):
        self.__is_going_hibernate = value