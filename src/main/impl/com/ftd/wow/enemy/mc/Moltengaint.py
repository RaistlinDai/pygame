'''
Created on Sep 04, 2019

@author: ftd
'''

import pygame
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant
from src.main.api.com.ftd.wow.enemy.IEnemy import IEnemy

class Moltengaint (IEnemy):
    '''
    
    '''
    
    
    def __init__(self):
        super().__init__(Materials_Constant.enemy_moltengaint_image_filename, [50, 10, 10, 1, 4, 3, 1.2])