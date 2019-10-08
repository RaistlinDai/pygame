'''
Created on Sep 04, 2019

@author: ftd
'''

import pygame
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant
from src.main.api.com.ftd.wow.enemy.IEnemy import IEnemy

class Ragnaros (IEnemy):
    '''
    
    '''
    
    def __init__(self):
        super().__init__(Materials_Constant.boss_ragnaros_image_filename, [100, 12, 8, 10, 5, 5])