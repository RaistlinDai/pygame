'''
Created on Sep 23, 2019

@author: ftd
'''
from src.main.impl.com.ftd.wow.character.CharacterAgainst import CharacterAgainst
from src.main.impl.com.ftd.wow.enemy.mc.Enemy_MC_Enum import Enemy_MC_Enum

class Enemy_Util(object):
    '''
    
    '''
    
    @staticmethod
    def generate_enemy_by_scene(current_scene, resource_DTO):
        '''
        Generate the enemy group by scene
        '''
        enemy_group = []
        
        # create enemy
        idx = 0
        for idx in [0,1,2,3]:
            if idx == 1:
                temp_enemy_character = CharacterAgainst("Enemy" + str(idx), resource_DTO.get_enemy(Enemy_MC_Enum.MC_FIREELEMENTAL.name))
            elif idx == 2:
                temp_enemy_character = CharacterAgainst("Enemy" + str(idx), resource_DTO.get_enemy(Enemy_MC_Enum.MC_FIREELEMENTAL.name))
            else:
                temp_enemy_character = None
            
            enemy_group.append(temp_enemy_character)
        
        return enemy_group
    