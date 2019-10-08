'''
Created on Sep 04, 2019

@author: ftd
'''

import pygame
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant
from src.main.api.com.ftd.wow.enemy.IEnemy import IEnemy

class FireElemental (IEnemy):
    '''
    
    '''
    
    def __init__(self):
        super().__init__(Materials_Constant.enemy_fireelemental_image_filename, \
                         [16, 12, 6, 11, 30, 15, 1.2])
    