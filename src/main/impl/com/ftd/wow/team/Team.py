'''
Created on Sep 04, 2019

@author: ftd
'''

import pygame
from src.main.api.com.ftd.wow.character.ICharacter import ICharacter
from src.main.impl.com.ftd.wow.profession.Profession_Enum import Profession_Enum

class Team (object):
    '''
    
    '''
    
    def __init__(self, character01=None, character02=None, character03=None, character04=None):
        
        self._teammember01 = character01
        self._teammember02 = character02
        self._teammember03 = character03
        self._teammember04 = character04
        
        self._team_name = None
        
    
    def set_teammember01(self, character):
        if not isinstance(character, ICharacter):
            return False, 'Incorrect Character'
        self._teammember01 = character
        
        
    def set_teammember02(self, character):
        if not isinstance(character, ICharacter):
            return False, 'Incorrect Character'
        self._teammember02 = character
        
        
    def set_teammember03(self, character):
        if not isinstance(character, ICharacter):
            return False, 'Incorrect Character'
        self._teammember03 = character
        
        
    def set_teammember04(self, character):
        if not isinstance(character, ICharacter):
            return False, 'Incorrect Character'
        self._teammember04 = character
        
    
    def get_teammember01(self):
        return self._teammember01
        
    
    def get_teammember02(self):
        return self._teammember02
    
    
    def get_teammember03(self):
        return self._teammember03
    
    
    def get_teammember04(self):
        return self._teammember04
    
    
    def get_teammembers(self):
        teammembers = []
        teammembers.append(self._teammember01)
        teammembers.append(self._teammember02)
        teammembers.append(self._teammember03)
        teammembers.append(self._teammember04)
            
        return teammembers