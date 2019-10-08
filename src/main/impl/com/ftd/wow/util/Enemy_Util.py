'''
Created on Sep 23, 2019

@author: ftd
'''
from src.main.impl.com.ftd.wow.character.CharacterAgainst import CharacterAgainst

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
            if idx == 0:
                temp_enemy_character = CharacterAgainst("Enemy" + str(idx), resource_DTO.get_enemy('MC_VALCANICELEMENTAL'))
            elif idx == 1:
                temp_enemy_character = CharacterAgainst("Enemy" + str(idx), resource_DTO.get_enemy('MC_LAVAELEMENTAL'))
            elif idx == 2:
                temp_enemy_character = CharacterAgainst("Enemy" + str(idx), resource_DTO.get_enemy('MC_FIREELEMENTAL'))
                
            enemy_group.append(temp_enemy_character)
        
        return enemy_group
    