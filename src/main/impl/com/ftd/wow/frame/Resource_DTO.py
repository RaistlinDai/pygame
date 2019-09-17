'''
Created on Sep 17, 2019

@author: ftd
'''
from src.main.impl.com.ftd.wow.scene.base.IMenuScene import IMenuScene
from src.main.impl.com.ftd.wow.scene.MenuScene_Enum import MenuScene_Enum
from src.main.impl.com.ftd.wow.scene.FightScene_Enum import FightScene_Enum
from src.main.impl.com.ftd.wow.scene.base.IFightScene import IFightScene
from src.main.impl.com.ftd.wow.layout.bar.Top_Bar import Top_Bar
from src.main.impl.com.ftd.wow.layout.bar.Bottom_Bar import Bottom_Bar

class Resource_DTO(object):
    '''
    
    '''
    
    def __init__(self):
        self.__backgrounds = {}
    
    
    def load_resources(self):
        self._load_backgrounds()
        print(self.__backgrounds)
        
    
    def _load_backgrounds(self):
        '''
        hardcode loading the backgrounds
        '''
        
        self.__top_bar = Top_Bar()
        self.__bottom_bar = Bottom_Bar()
        
        for sce in MenuScene_Enum:
            self.__backgrounds[sce.name] = IMenuScene(sce)
        
        for fightsce in FightScene_Enum:
            self.__backgrounds[fightsce.name] = IFightScene(fightsce)
            
        
        