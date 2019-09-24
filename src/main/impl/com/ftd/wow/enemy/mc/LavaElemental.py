'''
Created on Sep 04, 2019

@author: ftd
'''

import pygame
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant
from src.main.api.com.ftd.wow.enemy.IEnemy import IEnemy

class LavaElemental (IEnemy):
    '''
    
    '''
    
    def __init__(self):
        super().__init__(Materials_Constant.enemy_lavaelemental_image_filename)

