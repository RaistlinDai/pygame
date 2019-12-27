import random
from src.main.impl.com.ftd.wow.map.Map_DTO import Cell_DTO, Map_DTO
from enum import Enum, unique
from src.main.impl.com.ftd.wow.scene.forrest.ForrestScene_Enum import ForrestScene_Enum
        
        
@unique
class MapType_Enum(Enum):
    '''
    classdocs
    @attention: the value structure: [Corridor list, Room list, Foreground list]
    '''
    
    FORREST = [ForrestScene_Enum.Forrest_Background_Generals, ForrestScene_Enum.Forrest_Background_Rooms]
    MOUNTAIN = []
    
        
@unique
class MapSize_Enum(Enum):
    '''
    classdocs
    @attention: the value structure: scene constructor
    '''
    
    SIZE_BIG = (100,110)
    SIZE_MIDDLE = (70,80)
    SIZE_SMALL = (40,50)
    

@unique
class CellType_Enum(Enum):
    '''
    classdocs
    @attention: the value structure: scene constructor
    '''
    
    TYPE_ENTRANCE = "Entrance"
    TYPE_CORRIDOR = "Corridor"
    TYPE_ROOM = "Room"
    TYPE_SECRET = "Secret"
    
    
@unique
class CellItemType_Enum(Enum):
    '''
    classdocs
    @attention: the value structure: scene constructor
    '''
    
    TYPE_FOREGROUND = "Foreground"
    TYPE_ITEM = "Item"

    
@unique
class CellItemSize_Enum(Enum):
    '''
    classdocs
    @attention: the value is a contrary value in 1280*720
    '''
    
    SIZE_BIG = 800
    SIZE_MIDDLE = 500
    SIZE_SMALL = 300
    
    
@unique
class CellItemsCount_Enum(Enum):
    '''
    classdocs
    @attention: the count of items in one map cell
    '''
    
    COUNT_SERRIED = 5
    COUNT_THICK = 3
    COUNT_THIN = 1
    COUNT_DESERTED = 0
    

@unique
class MoveDirection_Enum(Enum):
    '''
    classdocs
    @attention: the move direction
    '''
    
    DIRECTION_NORTH = "North"
    DIRECTION_SOUTH = "South"
    DIRECTION_WEST = "West"
    DIRECTION_EAST = "East"
    
    
class Map_Util(object):
    '''
    The map is consist by cells with PosX and PosY
    Example:
                      [0,-1]     
    [-3,0][-2,0][-1,0][0,0][1,0][2,0]
                [-1,1]
                [-1,2]
    PosX is the horizontal position, PosY is the vertical position
    
    The direction: north:1, south:2, west:3, east:4
    
    '''
    
    DEFAULT_CELL_COUNT_IN_SINGLE_GROUP = (4,8)
    DEFAULT_CELL_SIZE = (1, 100)
    
    @staticmethod
    def generate_random_map(map_type, map_size):
        '''
        Generate a random map
        @param map_size: the size of the random map
        '''
        mapDTO = Map_DTO(map_size)
        
        if not isinstance(map_size, MapSize_Enum):
            return mapDTO
        
        # map cell list
        map_cell_list = []
        
        # generate the cells count by map_size
        temp_map_size_count = random.randint(map_size.value[0], map_size.value[1])
        
        # the start cell is [0,0]
        entrance_cell = Cell_DTO(0, 0, CellType_Enum.TYPE_ENTRANCE)
        map_cell_list.append(entrance_cell)
        
        # the room list
        temp_room_list = []
        temp_room_list.append(entrance_cell)
        
        while (temp_map_size_count > 2 or len(temp_room_list) == 0):
            # pick up one Room cell as start point
            room_number = random.randint(0, len(temp_room_list)-1)
            temp_start_point = temp_room_list[room_number]
            
            # generate new cell group
            generated_cell_group, new_group_count, new_room_cell, existing_room_cell = \
                Map_Util.generate_single_cell_group(temp_start_point, temp_map_size_count, map_cell_list)
                
            # update start point
            if new_group_count > 0:
                # add room cell
                if new_room_cell:
                    temp_room_list.append(new_room_cell)
                elif existing_room_cell:
                    # update the nearby cells
                    nearby_cells = Map_Util.get_nearby_cells_in_cell_group(existing_room_cell, generated_cell_group)
                    if len(nearby_cells) == 1:
                        existing_room_cell.append_nearby_cells(nearby_cells[0])
                    if len(existing_room_cell.get_nearby_cells()) == 4:
                        temp_room_list.remove(existing_room_cell)
                
                # update the nearby cells
                nearby_cells = Map_Util.get_nearby_cells_in_cell_group(temp_start_point, generated_cell_group)
                if len(nearby_cells) == 1:
                    temp_start_point.append_nearby_cells(nearby_cells[0])
                if len(temp_start_point.get_nearby_cells()) == 4:
                    temp_room_list.remove(temp_start_point)
            else:
                temp_room_list.remove(temp_start_point)
                
            # merge cell group
            map_cell_list = map_cell_list + generated_cell_group
            
            # reduce the map size
            temp_map_size_count = temp_map_size_count - new_group_count
        
        # update mapDTO
        mapDTO.set_cell_list(map_cell_list)
        mapDTO.set_entrence(entrance_cell)
        
        # re-order the map cells
        Map_Util.reorder_cells(mapDTO)
        
        # render the map
        Map_Util.render_map(mapDTO)
        return mapDTO
        
        
    @staticmethod
    def generate_single_cell_group(start_cell, count_limit, cell_group):
        '''
        @param start_cell: the start cell of this cell group
        @param count_limit: the max cell count
        @param cell_group: the generated cell groups
        @return: new generated cell group, new cell group count, new Room cell
        '''
        
        temp_cell_list = []
        if not isinstance(start_cell, Cell_DTO):
            return temp_cell_list, 0, None, None
        
        # verify if the related cells are existing, and the exactly direction
        temp_nearby_cells = start_cell.get_nearby_cells()
        
        # get the left directions
        generated_direction = 0
        temp_list, left_directions = Map_Util.get_cell_directions(start_cell, temp_nearby_cells)
        
        if len(left_directions) > 1:
            generated_direction = random.choice(left_directions)
        elif len(left_directions) == 1:
            generated_direction = left_directions[0]
        else:
            return temp_cell_list, 0, None, None
        
        # calculate the cell group size
        temp_size_in_group = random.randint(Map_Util.DEFAULT_CELL_COUNT_IN_SINGLE_GROUP[0], \
                                            Map_Util.DEFAULT_CELL_COUNT_IN_SINGLE_GROUP[1])
        startX = start_cell.get_pos_x()
        startY = start_cell.get_pos_y()
        is_generate_room = True
        
        if temp_size_in_group >= count_limit:
            temp_size_in_group = count_limit
            
        # verify if there's cell existing in this direction
        cell_distance = 999
        cell_far_end = None
        for temp_cell in cell_group:
            if generated_direction == 4 and startX == temp_cell.get_pos_x() and startY < temp_cell.get_pos_y():
                if cell_distance > abs(startY - temp_cell.get_pos_y()):
                    cell_far_end = temp_cell
                    cell_distance = abs(startY - temp_cell.get_pos_y())
            elif generated_direction == 3 and startX == temp_cell.get_pos_x() and startY > temp_cell.get_pos_y():
                if cell_distance > abs(startY - temp_cell.get_pos_y()):
                    cell_far_end = temp_cell
                    cell_distance = abs(startY - temp_cell.get_pos_y())
            elif generated_direction == 2 and startY == temp_cell.get_pos_y() and startX > temp_cell.get_pos_x():
                if cell_distance > abs(startX - temp_cell.get_pos_x()):
                    cell_far_end = temp_cell
                    cell_distance = abs(startX - temp_cell.get_pos_x())
            elif generated_direction == 1 and startY == temp_cell.get_pos_y() and startX < temp_cell.get_pos_x():
                if cell_distance > abs(startX - temp_cell.get_pos_x()):
                    cell_far_end = temp_cell
                    cell_distance = abs(startX - temp_cell.get_pos_x())
            
        # if the far-end cell is a Room, then link it
        existing_room_cell = None
        if cell_far_end:
            # link the generated room to the new cell group
            if cell_far_end.get_type() == CellType_Enum.TYPE_ROOM or cell_far_end.get_type() == CellType_Enum.TYPE_ENTRANCE:
                temp_size_in_group = cell_distance - 1
                is_generate_room = False
                existing_room_cell = cell_far_end
            elif cell_distance <= temp_size_in_group:
                if cell_distance <= 3:
                    return temp_cell_list, 0, None, None
                else:
                    temp_size_in_group = cell_distance - 1
        
        # generate the map cells
        i = 0
        new_room_cell = None
        while (i < temp_size_in_group):
            if generated_direction == 4:
                tempCell = Cell_DTO(startX, startY + i + 1, CellType_Enum.TYPE_CORRIDOR)
            elif generated_direction == 3:
                tempCell = Cell_DTO(startX, startY - i - 1, CellType_Enum.TYPE_CORRIDOR)
            elif generated_direction == 2:
                tempCell = Cell_DTO(startX - i - 1, startY, CellType_Enum.TYPE_CORRIDOR)
            elif generated_direction == 1:
                tempCell = Cell_DTO(startX + i + 1, startY, CellType_Enum.TYPE_CORRIDOR)
            
            if i + 1 == temp_size_in_group and is_generate_room:
                tempCell.set_type(CellType_Enum.TYPE_ROOM)
                new_room_cell = tempCell
            
            temp_cell_list.append(tempCell)
            
            i = i + 1
        
        # apply nearby cells
        i = 0
        for temp_cell in temp_cell_list:
            if i - 1 >= 0:
                temp_cell.append_nearby_cells(temp_cell_list[i - 1])
            else:
                temp_cell.append_nearby_cells(start_cell)
                
            if i + 1 < len(temp_cell_list):
                temp_cell.append_nearby_cells(temp_cell_list[i + 1])
            elif existing_room_cell:
                temp_cell.append_nearby_cells(existing_room_cell)
                
            i += 1
                
        return temp_cell_list, temp_size_in_group, new_room_cell, existing_room_cell
    
    
    @staticmethod
    def get_cell_directions(start_cell, nearby_cells):
        '''
        Here we use binary to replace the four directions: NSWE; and 0 means no related cell, 1 means it does.
        For example, 1101 means on North, South and East, the related cells are generated already.
        The variable "temp_existing_directions" is the converted binary value
        The variable "generated_direction" is the representation of for directions: 4:N, 3:S, 2:W, 1:E
        The variable "left_directions" is the directions which do not generated cell
        
        @return: existing_directions - Format - {1:Cell, 2:Cell, 3:Cell, 4:Cell}
        @return: left_directions     - Format - [4,3,2,1]
        '''
        temp_existing_directions = 0
        existing_directions = {}
        left_directions = []
        cell_on_south = None
        cell_on_north = None
        cell_on_west = None
        cell_on_east = None
        if nearby_cells and len(nearby_cells) > 0:
            for temp_cell in nearby_cells:
                # on Y
                if temp_cell.get_pos_x() == start_cell.get_pos_x():
                    # south existing
                    if temp_cell.get_pos_y() < start_cell.get_pos_y():
                        temp_existing_directions = temp_existing_directions + 4
                        cell_on_south = temp_cell
                    # north existing
                    elif temp_cell.get_pos_y() > start_cell.get_pos_y():
                        temp_existing_directions = temp_existing_directions + 8
                        cell_on_north = temp_cell
                # on X
                elif temp_cell.get_pos_y() == start_cell.get_pos_y():
                    # west existing
                    if temp_cell.get_pos_x() < start_cell.get_pos_x():
                        temp_existing_directions = temp_existing_directions + 2
                        cell_on_west = temp_cell
                    # east existing
                    elif temp_cell.get_pos_x() > start_cell.get_pos_x():
                        temp_existing_directions = temp_existing_directions + 1
                        cell_on_east = temp_cell
                        
        # verify the direction
        tempBinStr = bin(temp_existing_directions)[2:]
        for temp_char in range(4 - len(tempBinStr)):
            tempBinStr = '0' + tempBinStr
            
        if int(tempBinStr[0]) == 0:
            left_directions.append(4)
        else:
            existing_directions[4] = cell_on_north
            
        if int(tempBinStr[1]) == 0:
            left_directions.append(3)
        else:
            existing_directions[3] = cell_on_south
            
        if int(tempBinStr[2]) == 0:
            left_directions.append(2)
        else:
            existing_directions[2] = cell_on_west
            
        if int(tempBinStr[3]) == 0:
            left_directions.append(1)
        else:
            existing_directions[1] = cell_on_east
        
        return existing_directions, left_directions
    
    
    @staticmethod
    def get_nearby_cells_in_cell_group(start_cell, cell_group):
        '''
        Retrieve the nearby cell in cell group
        '''
        start_x = start_cell.get_pos_x()
        start_y = start_cell.get_pos_y()
        nearby_cells = []
        
        for tempCell in cell_group:
            temp_x = tempCell.get_pos_x()
            temp_y = tempCell.get_pos_y()
            
            if start_x == temp_x and start_y == temp_y:
                continue
            elif start_x == temp_x and abs(start_y - temp_y) == 1:
                nearby_cells.append(tempCell)
            elif start_y == temp_y and abs(start_x - temp_x) == 1:
                nearby_cells.append(tempCell)
        
        return nearby_cells 
    
    
    @staticmethod
    def get_next_cell_in_map_by_direction(current_cell, direction, mapDTO):
        '''
        Retrieve the next cell according to the move direction
        '''
        if not mapDTO or not isinstance(mapDTO, Map_DTO):
            return None
        
        if not current_cell or not isinstance(current_cell, Cell_DTO):
            return None
        
        if not direction or not isinstance(direction, MoveDirection_Enum):
            return None
        
        cell_group = mapDTO.get_cell_list()
        
        pos_x = current_cell.get_pos_x()
        pos_y = current_cell.get_pos_y()
        
        for tempCell in cell_group:
            temp_x = tempCell.get_pos_x()
            temp_y = tempCell.get_pos_y()
            
            if pos_y == temp_y and pos_x - temp_x == 1 and \
               direction == MoveDirection_Enum.DIRECTION_WEST:
                return tempCell
            elif pos_y == temp_y and temp_x - pos_x == 1 and \
               direction == MoveDirection_Enum.DIRECTION_EAST:
                return tempCell
            elif pos_x == temp_x and pos_y - temp_y == 1 and \
               direction == MoveDirection_Enum.DIRECTION_SOUTH:
                return tempCell
            elif pos_x == temp_x and temp_y - pos_y == 1 and \
               direction == MoveDirection_Enum.DIRECTION_NORTH:
                return tempCell
            
        return None
    
    
    @staticmethod
    def get_prev_cell_in_map_by_direction(current_cell, direction, mapDTO):
        '''
        Retrieve the previous cell according to the move direction
        '''
        if not mapDTO or not isinstance(mapDTO, Map_DTO):
            return None
        
        if not current_cell or not isinstance(current_cell, Cell_DTO):
            return None
        
        if not direction or not isinstance(direction, MoveDirection_Enum):
            return None
        
        cell_group = mapDTO.get_cell_list()
        
        pos_x = current_cell.get_pos_x()
        pos_y = current_cell.get_pos_y()
        
        for tempCell in cell_group:
            temp_x = tempCell.get_pos_x()
            temp_y = tempCell.get_pos_y()
            
            if pos_y == temp_y and pos_x - temp_x == 1 and \
               direction == MoveDirection_Enum.DIRECTION_EAST:
                return tempCell
            elif pos_y == temp_y and temp_x - pos_x == 1 and \
               direction == MoveDirection_Enum.DIRECTION_WEST:
                return tempCell
            elif pos_x == temp_x and pos_y - temp_y == 1 and \
               direction == MoveDirection_Enum.DIRECTION_NORTH:
                return tempCell
            elif pos_x == temp_x and temp_y - pos_y == 1 and \
               direction == MoveDirection_Enum.DIRECTION_SOUTH:
                return tempCell
            
        return None
        
    
    @staticmethod
    def reorder_cells(mapDTO):
        '''
        re-order the cells
        '''
        if not isinstance(mapDTO, Map_DTO):
            return None
        
        cell_group = mapDTO.get_cell_list()
        
        group_length = len(cell_group)
        for i in range(group_length):
            temp_cell = cell_group[i]
            j = i
            for j in range(group_length):
                if temp_cell.get_pos_x() < cell_group[j].get_pos_x():
                    temp_cell = cell_group[j]
                    cell_group[j] = cell_group[i]
                    cell_group[i] = temp_cell
                    
                if temp_cell.get_pos_y() > cell_group[j].get_pos_y():
                    temp_cell = cell_group[j]
                    cell_group[j] = cell_group[i]
                    cell_group[i] = temp_cell
        
        return cell_group    
    
    
    @staticmethod
    def render_map(mapDTO):
        '''
        render the map
        '''
        if not isinstance(mapDTO, Map_DTO):
            return None
        
        cell_group = mapDTO.get_cell_list()
        
        max_x = 0
        max_y = 0
        for temp_cell in cell_group:
            if max_x > temp_cell.get_pos_x():
                max_x = temp_cell.get_pos_x()
            if max_y < temp_cell.get_pos_y():
                max_y = temp_cell.get_pos_y()
        
        current_posY_nbr = -9999
        current_line_txt = ''
        for temp_cell in cell_group:
            abs_x = temp_cell.get_pos_x()
            abs_y = temp_cell.get_pos_y()
            
            if current_posY_nbr != abs_y:
                print(current_line_txt)
                current_line_txt = ''
            
            line_nbr = len(current_line_txt)
            space_nbr = abs(abs_x - max_x) - line_nbr
            for space_x in range(space_nbr):
                current_line_txt += ' '
            if temp_cell.get_type() == CellType_Enum.TYPE_CORRIDOR:
                current_line_txt += '+'
            elif temp_cell.get_type() == CellType_Enum.TYPE_ENTRANCE:
                current_line_txt += 'O'
            elif temp_cell.get_type() == CellType_Enum.TYPE_ROOM:
                current_line_txt += 'X'
                
            current_posY_nbr = abs_y
        
        print(current_line_txt)
        
    
    @staticmethod
    def calculate_movement(move_x):
        pass