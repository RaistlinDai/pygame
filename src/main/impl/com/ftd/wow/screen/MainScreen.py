'''
Created on Aug 27, 2019

@author: ftd
'''
import pygame
from pygame.locals import *
from src.main.impl.com.ftd.wow.button.Horde_Button import Horde_Button
import time; 
from src.main.impl.com.ftd.wow.scene.menu.Scene_Login import Scene_Login
from src.main.impl.com.ftd.wow.team.Team import Team
from src.main.impl.com.ftd.wow.frame.Resource_DTO import Resource_DTO
from src.main.impl.com.ftd.wow.scene.MenuScene_Enum import MenuScene_Enum
from src.main.impl.com.ftd.wow.scene.FightScene_Enum import FightScene_Enum
from src.main.impl.com.ftd.wow.frame.Context_DTO import Context_DTO
from src.main.impl.com.ftd.wow.scene.base.SceneMode_Enum import SceneMode_Enum
from src.main.impl.com.ftd.wow.savedata.Savedata_Analysis import Savedata_Analsis
from src.main.impl.com.ftd.wow.util.Enemy_Util import Enemy_Util

class MainScreen(object):
    '''
    
    '''
    
    def __init__(self, width, height):
        # initialize context
        self.__context_DTO = Context_DTO()
        self.__context_DTO.set_screen_width(width)
        self.__context_DTO.set_screen_height(height)
        
        # initialize pygame for hardware
        pygame.init()
        # create a window
        self._screen = pygame.display.set_mode((self.__context_DTO.get_screen_width(), self.__context_DTO.get_screen_height()), 0, 32)
        # set window title
        pygame.display.set_caption("Hello, World!")
        
        # screen background
        self._background = Scene_Login(self.__context_DTO.get_screen_width(), self.__context_DTO.get_screen_height())
        self._background_prop = (0, 0, self.__context_DTO.get_screen_width(), self.__context_DTO.get_screen_height())
        
        # source loading
        # the range of loading: all scene backgrounds and framework images, all profession images, all skill images
        self.__resource_DTO = Resource_DTO()
        self.__resource_DTO.load_resources()
        
    
    def execute(self):
        '''
        @todo: add login and load scene - consider to add a "Scene Controller" to handle the scene changing
        '''
        # load savedata
        load_characters = Savedata_Analsis.load_savedata(self.__resource_DTO)
        
        '''
        @todo: 
        '''
        
        self.__context_DTO.set_active_team(Team(None, None, load_characters[0], load_characters[1]))
        # generate enemy
        generated_enemies = self.generate_enemy(self.__resource_DTO)
        self.__context_DTO.set_active_enemies(Team(generated_enemies[0], generated_enemies[1], generated_enemies[2], generated_enemies[3]))
        
        # setup current scene
        self.__context_DTO.get_scene_manager().set_current_scene_mode(SceneMode_Enum.MENU_SCENE)
        self.__context_DTO.get_scene_manager().set_current_scene(self.__resource_DTO.get_scene(MenuScene_Enum.HORDE_LOGIN.name))
        
        # horde button
        horde_start_button = Horde_Button(585, 270, 100, 100)
        horde_button_click_timer = 0
                
        move_x, move_y = 0, 0
        
        # main loop
        while True:
            # clocker
            current_timer = time.time()*1000.0
            # mouse cursor position
            cursor_x, cursor_y = pygame.mouse.get_pos()
            
            #==========================================#
            #               Scene maintain             #
            #==========================================#
            # render the background
            self.render_scene(self.__context_DTO.get_scene_manager().get_current_scene())
            
            # render the button & determine the background
            if (self.__context_DTO.get_scene_manager().get_current_scene_mode() == SceneMode_Enum.MENU_SCENE):
                if (not horde_start_button.is_over()):
                    self._screen.blit(horde_start_button.show_button(), horde_start_button.get_position())
                else:
                    self._screen.blit(horde_start_button.show_button_cover(), horde_start_button.get_position())
                    
            elif (self.__context_DTO.get_scene_manager().get_current_scene_mode() == SceneMode_Enum.LOAD_SCENE):
                if (current_timer - horde_button_click_timer < 2000):
                    self._screen.blit(horde_start_button.show_button_click(), horde_start_button.get_position())
                elif (current_timer - horde_button_click_timer >= 2000):
                    self.__context_DTO.get_scene_manager().set_current_scene_mode(SceneMode_Enum.FIGHT_SCENE)
                    
            elif (self.__context_DTO.get_scene_manager().get_current_scene_mode() == SceneMode_Enum.FIGHT_SCENE):
                # re-load the background
                self.__context_DTO.get_scene_manager().set_current_scene_mode(SceneMode_Enum.FIGHT_SCENE)
                self.__context_DTO.get_scene_manager().set_current_scene(self.__resource_DTO.get_scene(FightScene_Enum.MC_BOSS_10.name))
                self.__context_DTO.get_scene_manager().get_current_scene().add_active_team(self.__context_DTO.get_active_team())
                self.__context_DTO.get_scene_manager().get_current_scene().set_current_character(load_characters[1])
                
                self.__context_DTO.set_in_fight(True)
                if self.__context_DTO.get_in_fight() == True:
                    self.__context_DTO.get_scene_manager().get_current_scene().add_active_enemies(self.__context_DTO.get_active_enemies())
                
                # Mouse cursor event
                self.__context_DTO.get_scene_manager().get_current_scene().cursor_event(cursor_x, cursor_y)
            
            #==========================================#
            #               Event handler              #
            #==========================================#
            for event in pygame.event.get():
                # leave event
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                    
                # keyboard event
                if event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        move_x = -1
                    elif event.key == K_RIGHT:
                        move_x = 1
                    elif event.key == K_UP:
                        move_y = -1
                    elif event.key == K_DOWN:
                        move_y = 1
                elif event.type == KEYUP:
                    move_x = 0
                    move_y = 0
            
            # get the keyboard and mouse click
            pressed_mouse = pygame.mouse.get_pressed()
        
            # mouse click event
            if pressed_mouse[0] or pressed_mouse[2]:
                '''
                @todo: move into Scene_Manager?
                '''
                # menu scene
                if (self.__context_DTO.get_scene_manager().get_current_scene_mode() == SceneMode_Enum.MENU_SCENE):
                    # horde button click
                    if (horde_start_button.is_over()):
                        self.__context_DTO.get_scene_manager().set_current_scene_mode(SceneMode_Enum.LOAD_SCENE)
                        horde_button_click_timer = time.time()*1000.0
                
                elif (self.__context_DTO.get_scene_manager().get_current_scene_mode() == SceneMode_Enum.FIGHT_SCENE):
                    self.__context_DTO.get_scene_manager().get_current_scene().mouse_click_event(pressed_mouse)
            
            # render cursor
            self.render_cursor(cursor_x, cursor_y)
            
            # clipping in middle
            #screen.set_clip(0, 50, 770, 380)
                
            # render the screen
            pygame.display.update()
            
    
    def render_scene(self, scene):
        if not scene.render_scene:
            return False, 'Scene renderer is not valid!'
        
        renderer = self._screen
        scene.render_scene(renderer, self.__context_DTO.get_screen_width(), self.__context_DTO.get_screen_height())
        
    
    def render_cursor(self, cursor_x, cursor_y):
        # calculate the cursor left-top position
        cursor_x-= self.__resource_DTO.get_mouse_cursor().get_width() / 2
        cursor_y-= self.__resource_DTO.get_mouse_cursor().get_height() / 2
        # render the cursor
        self._screen.blit(self.__resource_DTO.get_mouse_cursor(), (cursor_x, cursor_y))
    
    
    '''
    TODO: move to other place
    '''
    def generate_enemy(self, resource_DTO):
        return Enemy_Util.generate_enemy_by_scene(self, resource_DTO)
