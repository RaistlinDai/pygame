'''
Created on Oct 16, 2019

@author: ftd
'''

from src.main.impl.com.ftd.wow.util.Map_Util import Map_Util, MoveDirection_Enum,\
    CellType_Enum, CellItemType_Enum, MapType_Enum, CellItemSize_Enum
from src.main.api.com.ftd.wow.controller.IController import IController
from src.main.impl.com.ftd.wow.map.Map_DTO import Position_DTO, Cell_Item_DTO
import time
from src.main.impl.com.ftd.wow.util.Image_Util import Image_Util
import random
from src.main.impl.com.ftd.wow.scene.forrest.ForrestItem_Enum import ForrestItem_Enum
    
    
class Maze_Walker(IController):
    '''
    The controller of Maze, and it's a sub-controller of Abyss_Overlord.
    The main job of Maze_Walker is to maintain the movement of characters in the maze. It could generate the map, calculate the 
      position of character, and also synchronize these information into Context_DTO.ContextDTO_InMap
    '''
    
    
    def __init__(self):
        super().__init__()
    
        
    def wake_up_controller(self, contextDTO=None, resourceDTO=None):
        super().wake_up_controller(contextDTO, resourceDTO)
        # generate map
        temp_map = self.generate_map(contextDTO.get_contextDTO_InMap().get_map_type(), contextDTO.get_contextDTO_InMap().get_map_size())
        # arrange map background and items
        self.arrange_map_background_and_items(temp_map, contextDTO.get_contextDTO_InMap().get_map_type(), resourceDTO)
        
        # backup the map into contextDTO
        contextDTO.get_contextDTO_InMap().set_map(temp_map)
        
        # initial map position
        positionDTO = Position_DTO()
        positionDTO.set_map_cell(temp_map.get_entrence())
        positionDTO.set_cell_position(Map_Util.DEFAULT_CELL_SIZE[0])
        positionDTO.set_move_direction(MoveDirection_Enum.DIRECTION_EAST)
        contextDTO.get_contextDTO_InMap().set_map_position(positionDTO)
        
        # resize character image
        calc_h = Image_Util.calculate_character_move_height_by_screen_size(contextDTO.get_screen_height())
        for temp_char in contextDTO.get_active_team().get_teammembers():
            if temp_char:
                temp_char.resize_character_images_by_height(calc_h, 1)
    
    
    def generate_map(self, map_type, map_size):
        return Map_Util.generate_random_map(map_type, map_size)
        
    
    def arrange_map_background_and_items(self, temp_map, map_type, resourceDTO):
        '''
        Arrange the background image index to each cell in map
        @todo: to retrieve the maze deepth
        '''
        # set general map background
        general_background_list = map_type.value[0].value
        idx = random.randint(0, len(general_background_list)-1)
        
        " set corridor background "
        temp_map.set_background_img_idx(idx)
        
        for map_cell in temp_map.get_cell_list():
            
            if map_cell.get_type() == CellType_Enum.TYPE_CORRIDOR:
                " cell items "
                obj_list_range = 0
                item_type = None
                item_list = []
                
                " forest map - "
                if map_type == MapType_Enum.FORREST:
                    item_type = ForrestItem_Enum.Forrest_Foreground_Trees
                    item_list = resourceDTO.get_map_items_by_type(item_type.name)
                    item_count_range = item_type.value[1].value
                    obj_list_range = len(item_list)
                
                    " random total items count "
                    random_item_count = random.randint(0, item_count_range)
                    while (random_item_count > 0):
                        " random item "
                        obj_idx = random.randint(0, obj_list_range-1)
                        temp_item_image = item_list[obj_idx]
                        # random the item position
                        random_item_posx = random.randint(1,100)
                        temp_cell_item = Cell_Item_DTO(temp_item_image, CellItemType_Enum.TYPE_FOREGROUND, \
                                                       CellItemSize_Enum.SIZE_BIG, random_item_posx, random_item_count) 
                        map_cell.append_cell_item(temp_cell_item)
                        
                        random_item_count = random_item_count - 1
                    
            elif map_cell.get_type() == CellType_Enum.TYPE_ROOM or map_cell.get_type() == CellType_Enum.TYPE_ENTRANCE:
                " set room background "
                room_list = map_type.value[1].value
                room_list_range = len(room_list)
                idx = random.randint(0, room_list_range-1)
                map_cell.set_background_img_idx(idx)
    
    
    def manage_characters_move_in_map(self, move_a, move_d, move_w, move_s, contextDTO):
        '''
        The most important function of Maze_Walker, it will maintain the characters' movement in the map. 
        Normally, the screen takes 30 size of a cell (cell's whole size is 100).
        
        |=======|                 -> the screen (40 cell size)
        |--------------------|    -> the cell in map (100 cell size)
        
        @return: scene_changing_timer
        @return: character_moving_timer
        @return: error message
        '''
        scene_changing_timer = 0
        character_moving_timer = 0
        
        # get the current map
        if not contextDTO.get_contextDTO_InMap() or not contextDTO.get_contextDTO_InMap().get_map():
            '''
            @todo: error
            '''
            return scene_changing_timer, character_moving_timer, "There's no map available!"
        
        current_map = contextDTO.get_contextDTO_InMap().get_map()
        positionDTO = contextDTO.get_contextDTO_InMap().get_map_position()
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
                    contextDTO.get_contextDTO_InMap().set_map_next_room(next_cell)
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
                    contextDTO.get_contextDTO_InMap().set_map_next_room(next_cell)
                    character_moving_timer = 0
            
            # enter the room
            next_room_cell = contextDTO.get_contextDTO_InMap().get_map_next_room()
            if move_w != 0 and next_room_cell and \
               (next_room_cell.get_type() == CellType_Enum.TYPE_ENTRANCE or next_room_cell.get_type() == CellType_Enum.TYPE_ROOM):
                if current_cell_position == Map_Util.DEFAULT_CELL_SIZE[1]:
                    current_cell_position = Map_Util.DEFAULT_CELL_SIZE[0]
                    current_cell = next_room_cell
                    contextDTO.get_contextDTO_InMap().set_map_next_room(None)
                elif current_cell_position == Map_Util.DEFAULT_CELL_SIZE[0]:
                    current_cell_position = Map_Util.DEFAULT_CELL_SIZE[1]
                    current_cell = next_room_cell
                    contextDTO.get_contextDTO_InMap().set_map_next_room(None)
                
                scene_changing_timer = time.time()*1000.0
            
            # update cell position DTO
            positionDTO.set_cell_position(current_cell_position)
            positionDTO.set_move_direction(current_direction)
            positionDTO.set_map_cell(current_cell)
            
            # synchronize contextDTO
            contextDTO.get_contextDTO_InMap().set_map_position(positionDTO)
        
        '''
        if move_a != 0 or move_d != 0 or move_w != 0:
            print('position:', current_cell.get_type(), (current_cell.get_pos_x(), current_cell.get_pos_y()), current_cell_position, scene_changing_timer)
        '''
        return scene_changing_timer, character_moving_timer, None
    