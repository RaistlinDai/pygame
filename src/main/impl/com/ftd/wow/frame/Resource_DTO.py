'''
Created on Sep 17, 2019

@author: ftd
'''
from src.main.impl.com.ftd.wow.scene.base.IMenuScene import IMenuScene
from src.main.impl.com.ftd.wow.scene.MenuScene_Enum import MenuScene_Enum
from src.main.impl.com.ftd.wow.scene.base.IFightScene import IFightScene
from src.main.impl.com.ftd.wow.layout.bar.Top_Bar import Top_Bar
from src.main.impl.com.ftd.wow.layout.bar.Bottom_Bar import Bottom_Bar
from src.main.impl.com.ftd.wow.profession.base.Profession_Enum import Profession_Enum
import pygame
from src.main.impl.com.ftd.wow.const.Materials_Constant import Materials_Constant
from src.main.impl.com.ftd.wow.enemy.mc.Enemy_MC_Enum import Enemy_MC_Enum

from src.main.impl.com.ftd.wow.scene.forrest.ForrestScene_Enum import ForrestScene_Enum
from src.main.impl.com.ftd.wow.scene.forrest.ForrestItem_Enum import ForrestItem_Enum
from src.main.impl.com.ftd.wow.scene.base.IMapItem import IMapItem

class Resource_DTO(object):
    '''
    
    '''
    
    def __init__(self):
        self.__backgrounds = {}       # {"menu_scene": IMenuScene, "combat_scene_corridor: [IFightScene1, IFightScene2]}
        self.__mapitems = {}
        self.__professions = {}
        self.__enemies = {}
        self.__mouse_cursor = None
        
    
    def load_resources(self):
        self._load_backgrounds()
        self._load_map_items()
        self._load_professions()
        self._load_enemies()
        self._load_mouse_cursor()
        
    
    def _load_backgrounds(self):
        '''
        load the backgrounds into dict
        '''
        self.__top_bar = Top_Bar()
        self.__bottom_bar = Bottom_Bar()
        
        for sce in MenuScene_Enum:
            self.__backgrounds[sce.name] = IMenuScene(sce)
        
        for forrest_sce_list in ForrestScene_Enum:
            temp_list = []
            for forrest_sce in forrest_sce_list.value:
                temp_list.append(IFightScene(forrest_sce, self.__bottom_bar, self.__top_bar))
            self.__backgrounds[forrest_sce_list.name] = temp_list
    
    
    def _load_map_items(self):
        '''
        load the map items into dict
        '''
        for map_item_draw_img in ForrestItem_Enum:
            mapItems = IMapItem(map_item_draw_img.value[0])
            self.__mapitems[map_item_draw_img.name] = mapItems.get_item_images()
            
    
    def _load_professions(self):
        '''
        load the professions into dict
        '''
        for pro in Profession_Enum:
            self.__professions[pro.name] = pro.value[0]()
    
    
    def _load_enemies(self):
        '''
        load the enemies into dict
        '''
        for enemy in Enemy_MC_Enum:
            self.__enemies[enemy.name] = enemy.value[0]()
    
    
    def _load_mouse_cursor(self):
        
        '''
        load the mouse image
        '''
        self.__mouse_cursor = pygame.image.load(Materials_Constant.mouse_image_filename).convert_alpha()
        
    
    def get_scene(self, scene_name):
        '''
        get the backgrounds by name
        '''
        return self.__backgrounds[scene_name]
    
    
    def get_maze_scene_by_index(self, maze_scene_type, maze_scene_idx=None):
        '''
        get the backgrounds in maze by type and index
        '''
        scene_list = self.__backgrounds[maze_scene_type]
        return scene_list[maze_scene_idx]
        
    
    def get_maze_scene_list_by_type(self, maze_scene_type):
        '''
        get the backgrounds in maze by type
        '''
        scene_list = self.__backgrounds[maze_scene_type]
        return scene_list
    
    
    def get_map_items_by_type(self, map_item_type):
        '''
        get the map item by map item type and index
        '''
        map_items = self.__mapitems[map_item_type]
        return map_items
    
    
    def get_map_items_by_type_and_index(self, map_item_type, map_item_index):
        '''
        get the map item by map item type and index
        '''
        map_item = self.__mapitems[map_item_type][map_item_index]
        return map_item
        
    
    def get_profession(self, profession_name):
        '''
        get the profession by name
        '''
        return self.__professions[profession_name]
    
    
    def get_enemy(self, enemy_name):
        '''
        get the enemy by name
        '''
        return self.__enemies[enemy_name]
    
    
    def get_mouse_cursor(self):
        
        '''
        get the mouse image
        '''
        return self.__mouse_cursor