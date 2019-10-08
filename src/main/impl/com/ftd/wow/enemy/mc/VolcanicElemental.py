'''
Created on Sep 04, 2019

@author: ftd
'''

import pygame
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant
from src.main.api.com.ftd.wow.enemy.IEnemy import IEnemy

class VolcanicElemental (IEnemy):
    '''
    
    '''
    
    def __init__(self):
        super().__init__(Materials_Constant.enemy_volcanicelemental_image_filename, [20, 7, 6, 5, 2, 2, 1.2])