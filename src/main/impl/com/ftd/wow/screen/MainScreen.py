'''
Created on Aug 27, 2019

@author: ftd
'''
import pygame
from pygame.locals import *
from src.main.impl.com.ftd.wow.scene.menu.Scene_Login import Scene_Login
from src.main.impl.com.ftd.wow.team.Team import Team
from src.main.impl.com.ftd.wow.frame.Resource_DTO import Resource_DTO
from src.main.impl.com.ftd.wow.frame.Context_DTO import Context_DTO
from src.main.impl.com.ftd.wow.scene.base.SceneMode_Enum import SceneMode_Enum
from src.main.impl.com.ftd.wow.savedata.Savedata_Analysis import Savedata_Analsis
from src.main.impl.com.ftd.wow.util.Enemy_Util import Enemy_Util
from src.main.impl.com.ftd.wow.controller.Big_Boss import Big_Boss

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
        
        # big boss manager
        self.__manager = Big_Boss(self.__resource_DTO)
        
    
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
        
        # update manager
        self.__manager.update_leader(SceneMode_Enum.MENU_SCENE)
                
        move_x, move_y = 0, 0
        
        # main loop
        while True:
            # mouse cursor position
            cursor_x, cursor_y = pygame.mouse.get_pos()
            
            #==========================================#
            #         Controller maintain              #
            #==========================================#
            self.__manager.wakeup_next_leader()
            
            #==========================================#
            #               Scene render               #
            #==========================================#
            # render the background
            self.__manager.render_scene(self._screen, self.__context_DTO)
            
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
                self.__manager.event_mouse_click(pressed_mouse)
            
            # render cursor
            self.render_cursor(cursor_x, cursor_y)
                
            # render the screen
            pygame.display.update()
        
    
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
