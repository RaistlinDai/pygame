'''
Created on Aug 27, 2019

@author: ftd
'''
from src.main.impl.com.ftd.wow.scene.base.IFightScene import IFightScene
from src.main.impl.com.ftd.wow.scene.FightScene_Enum import FightScene_Enum

class MC_Boss_Scene(IFightScene):
    '''
    
    '''
    
    def __init__(self, size_w, size_h, active_team, bottom_bar, top_bar):
        # super class constructor
        super().__init__(FightScene_Enum.MC_BOSS_10, size_w, size_h, active_team, bottom_bar, top_bar)
        
        
    def show_background(self):
        return self.__background
    
    
    def show_bottom_bar(self):
        return self.__bottom_bar
        
    
    def render(self, screen_ins, screen_w=None, screen_h=None):
        super().render_scene(screen_ins, screen_w, screen_h)