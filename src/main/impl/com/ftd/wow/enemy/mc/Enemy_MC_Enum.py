'''
Created on Sep 13, 2019

@author: ftd
'''
from enum import Enum, unique
from src.main.impl.com.ftd.wow.enemy.mc.FireElemental import FireElemental
from src.main.impl.com.ftd.wow.enemy.mc.LavaElemental import LavaElemental
from src.main.impl.com.ftd.wow.enemy.mc.Moltengaint import Moltengaint
from src.main.impl.com.ftd.wow.enemy.mc.boss.Ragnaros import Ragnaros
from src.main.impl.com.ftd.wow.enemy.mc.VolcanicElemental import VolcanicElemental


@unique
class Enemy_MC_Enum(Enum):
    '''
    classdocs
    @attention: the value structure: scene constructor
    '''
    
    MC_FIREELEMENTAL = [FireElemental, 1.8]
    MC_LAVAELEMENTAL = [LavaElemental, 1.8]
    MC_VALCANICELEMENTAL = [VolcanicElemental, 1.8]
    MC_MOLTENGAINT = [Moltengaint, 3]
    
    MC_BOSS_10 = [Ragnaros, 5]