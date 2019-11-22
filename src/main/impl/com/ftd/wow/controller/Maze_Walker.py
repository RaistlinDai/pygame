'''
Created on Oct 16, 2019

@author: ftd
'''

from src.main.impl.com.ftd.wow.util.Map_Util import Map_Util, MoveDirection_Enum,\
    CellType_Enum
from src.main.api.com.ftd.wow.controller.IController import IController
from src.main.impl.com.ftd.wow.map.Map_DTO import Position_DTO
import time
    
    
class Maze_Walker(IController):
    '''
    
    '''
    
    CELL_SIZE = 10
    
    def __init__(self):
        super().__init__()
        self.__map = None
        
        
    def wake_up_controller(self, contextDto=None):
        super().wake_up_controller(contextDto)
        # generate map
        self.generate_map(contextDto.get_ContextDto_InMap().get_map_size())
        # backup the map into contextDTO
        contextDto.get_ContextDto_InMap().set_map(self.__map)
        
        positionDTO = Position_DTO()
        positionDTO.set_map_cell(self.__map.get_entrence())
        positionDTO.set_cell_position(Map_Util.DEFAULT_CELL_SIZE[0])
        positionDTO.set_move_direction(MoveDirection_Enum.DIRECTION_EAST)
        contextDto.get_ContextDto_InMap().set_map_position(positionDTO)
        
        
    def generate_map(self, map_size):
        self.__map = Map_Util.generate_random_map(map_size)

        
    def get_map(self):
        return self.__map
    
        
    def set_current_position(self, value):
        self._current_position = value
        
        
    def get_current_position(self):
        return self._current_position
    
    
    def manage_characters_move_in_map(self, move_a, move_d, move_w, move_s, contextDTO):
        '''
        The most important function of Maze_Walker, it will maintain the characters' movement in the map. 
        @return: scene_changing_timer
        @return: character_moving_timer
        @return: error message
        '''
        scene_changing_timer = 0
        character_moving_timer = 0
        
        # get the current map
        current_map = self.get_map()
        if not current_map:
            '''
            @todo: error
            '''
            return scene_changing_timer, character_moving_timer, "There's no map available!"
        
        positionDTO = contextDTO.get_ContextDto_InMap().get_map_position()
        current_cell = positionDTO.get_map_cell()
        current_cell_position = positionDTO.get_cell_position()
        current_direction = positionDTO.get_move_direction()
            
        if not current_cell:
            current_cell = current_map.get_entrence()
            
        if not current_cell_position:
            current_cell_position = Map_Util.DEFAULT_CELL_SIZE[0]
            
        if not current_direction:
            current_direction = MoveDirection_Enum.DIRECTION_EAST
        
        if current_cell.get_type() == CellType_Enum.TYPE_ENTRANCE or \
           current_cell.get_type() == CellType_Enum.TYPE_ROOM:
            # In room or entrance
            nearby_cells = current_cell.get_nearby_cells()
            if len(nearby_cells) == 0:
                '''
                @todo: error
                '''
                return scene_changing_timer, character_moving_timer, "These's no nearby cell available!"
            else:
                existing_directions, temp_list = Map_Util.get_cell_directions(current_cell, nearby_cells)
                
                if move_w != 0 and 4 in existing_directions.keys():
                    current_cell = existing_directions[4]
                    current_direction = MoveDirection_Enum.DIRECTION_NORTH
                    scene_changing_timer = time.time()*1000.0
                elif move_s != 0 and 3 in existing_directions.keys():
                    current_cell = existing_directions[3]
                    current_direction = MoveDirection_Enum.DIRECTION_SOUTH
                    scene_changing_timer = time.time()*1000.0
                elif move_a != 0 and 2 in existing_directions.keys():
                    current_cell = existing_directions[2]
                    current_direction = MoveDirection_Enum.DIRECTION_WEST
                    scene_changing_timer = time.time()*1000.0
                elif move_d != 0 and 1 in existing_directions.keys():
                    current_cell = existing_directions[1]
                    current_direction = MoveDirection_Enum.DIRECTION_EAST
                    scene_changing_timer = time.time()*1000.0
                
                positionDTO.set_map_cell(current_cell)
                positionDTO.set_move_direction(current_direction)
                positionDTO.set_cell_position(0)
                    
        elif current_cell.get_type() == CellType_Enum.TYPE_CORRIDOR:
            # In corridor
            current_opposite_direction = None
            
            if current_direction == MoveDirection_Enum.DIRECTION_EAST:
                current_opposite_direction = MoveDirection_Enum.DIRECTION_WEST
            elif current_direction == MoveDirection_Enum.DIRECTION_WEST:
                current_opposite_direction = MoveDirection_Enum.DIRECTION_EAST
            elif current_direction == MoveDirection_Enum.DIRECTION_NORTH:
                current_opposite_direction = MoveDirection_Enum.DIRECTION_SOUTH
            elif current_direction == MoveDirection_Enum.DIRECTION_SOUTH:
                current_opposite_direction = MoveDirection_Enum.DIRECTION_NORTH
            
            # character movement offset
            current_cell_position = current_cell_position + move_d - move_a
            
            # calculate map cells
            if move_d - move_a != 0:
                character_moving_timer = time.time()*1000.0
                
            if current_cell_position > Map_Util.DEFAULT_CELL_SIZE[1]:
                next_cell = Map_Util.get_next_cell_in_map_by_direction(current_cell, current_direction, current_map)
                if next_cell.get_type() == CellType_Enum.TYPE_CORRIDOR:
                    current_cell_position = Map_Util.DEFAULT_CELL_SIZE[0]
                    current_cell = next_cell
                elif next_cell.get_type() == CellType_Enum.TYPE_ENTRANCE or\
                     next_cell.get_type() == CellType_Enum.TYPE_ROOM:
                    # waiting at the door of room
                    current_cell_position = Map_Util.DEFAULT_CELL_SIZE[1]
                    contextDTO.get_ContextDto_InMap().set_map_next_room(next_cell)
                    character_moving_timer = 0
                
            elif current_cell_position < Map_Util.DEFAULT_CELL_SIZE[0]:
                next_cell = Map_Util.get_next_cell_in_map_by_direction(current_cell, current_opposite_direction, current_map)
                if next_cell.get_type() == CellType_Enum.TYPE_CORRIDOR:
                    current_cell_position = Map_Util.DEFAULT_CELL_SIZE[1]
                    current_cell = next_cell
                elif next_cell.get_type() == CellType_Enum.TYPE_ENTRANCE or\
                     next_cell.get_type() == CellType_Enum.TYPE_ROOM:
                    # waiting at the door of room
                    current_cell_position = Map_Util.DEFAULT_CELL_SIZE[0]
                    contextDTO.get_ContextDto_InMap().set_map_next_room(next_cell)
                    character_moving_timer = 0
            
            # enter the room
            next_room_cell = contextDTO.get_ContextDto_InMap().get_map_next_room()
            if move_w != 0 and next_room_cell and \
               (next_room_cell.get_type() == CellType_Enum.TYPE_ENTRANCE or next_room_cell.get_type() == CellType_Enum.TYPE_ROOM):
                if current_cell_position == Map_Util.DEFAULT_CELL_SIZE[1]:
                    current_cell_position = Map_Util.DEFAULT_CELL_SIZE[0]
                    current_cell = next_room_cell
                    contextDTO.get_ContextDto_InMap().set_map_next_room(None)
                elif current_cell_position == Map_Util.DEFAULT_CELL_SIZE[0]:
                    current_cell_position = Map_Util.DEFAULT_CELL_SIZE[1]
                    current_cell = next_room_cell
                    contextDTO.get_ContextDto_InMap().set_map_next_room(None)
                
                scene_changing_timer = time.time()*1000.0
            
            # update cell position DTO
            positionDTO.set_cell_position(current_cell_position)
            positionDTO.set_move_direction(current_direction)
            positionDTO.set_map_cell(current_cell)
            
            # synchronize ContextDTO
            contextDTO.get_ContextDto_InMap().set_map_position(positionDTO)
        
        '''
        if move_a != 0 or move_d != 0 or move_w != 0:
            print('position:', current_cell.get_type(), (current_cell.get_pos_x(), current_cell.get_pos_y()), current_cell_position, scene_changing_timer)
        '''
        return scene_changing_timer, character_moving_timer, None
    