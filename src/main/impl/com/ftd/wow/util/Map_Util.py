import random
from src.main.impl.com.ftd.wow.map.Map_DTO import Cell_DTO, Map_DTO
from enum import Enum, unique
        
        
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
    
    @staticmethod
    def generate_random_map(map_size):
        
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
                    nearby_cell = Map_Util.analysis_nearby_cells(existing_room_cell, generated_cell_group)
                    existing_room_cell.append_nearby_cells(nearby_cell)
                    if len(existing_room_cell.get_nearby_cells()) == 4:
                        temp_room_list.remove(existing_room_cell)
                
                # update the nearby cells
                nearby_cell = Map_Util.analysis_nearby_cells(temp_start_point, generated_cell_group)
                temp_start_point.append_nearby_cells(nearby_cell)
                if len(temp_start_point.get_nearby_cells()) == 4:
                    temp_room_list.remove(temp_start_point)
            else:
                temp_room_list.remove(temp_start_point)
                
            # merge cell group
            map_cell_list = map_cell_list + generated_cell_group
            
            # reduce the map size
            temp_map_size_count = temp_map_size_count - new_group_count
        
        # re-order the map cells
        Map_Util.reorder_cells(map_cell_list)
        # render the map
        Map_Util.render_map(map_cell_list)
        
        mapDTO.set_cell_list(map_cell_list)
        mapDTO.set_entrence(entrance_cell)
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
        '''
        Here we use binary to replace the four directions: NSWE; and 0 means no related cell, 1 means it does.
        For example, 1101 means on North, South and East, the related cells are generated already.
        The variable "temp_existing_directions" is the converted binary value
        The variable "generated_direction" is the representation of for directions: 4:N, 3:S, 2:W, 1:E
        The variable "left_directions" is the directions which do not generated cell
        '''
        temp_existing_directions = 0
        generated_direction = 0
        left_directions = []
        if temp_nearby_cells and len(temp_nearby_cells) > 0:
            for temp_cell in temp_nearby_cells:
                # on Y
                if temp_cell.get_pos_x() == start_cell.get_pos_x():
                    # south existing
                    if temp_cell.get_pos_y() < start_cell.get_pos_y():
                        temp_existing_directions = temp_existing_directions + 4
                    # north existing
                    elif temp_cell.get_pos_y() > start_cell.get_pos_y():
                        temp_existing_directions = temp_existing_directions + 8
                # on X
                elif temp_cell.get_pos_y() == start_cell.get_pos_y():
                    # west existing
                    if temp_cell.get_pos_x() < start_cell.get_pos_x():
                        temp_existing_directions = temp_existing_directions + 2
                    # east existing
                    elif temp_cell.get_pos_x() > start_cell.get_pos_x():
                        temp_existing_directions = temp_existing_directions + 1
                        
        # verify the direction
        tempBinStr = bin(temp_existing_directions)[2:]
        for temp_char in range(4 - len(tempBinStr)):
            tempBinStr = '0' + tempBinStr
            
        if int(tempBinStr[0]) == 0:
            left_directions.append(4)
        if int(tempBinStr[1]) == 0:
            left_directions.append(3)
        if int(tempBinStr[2]) == 0:
            left_directions.append(2)
        if int(tempBinStr[3]) == 0:
            left_directions.append(1)
        
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
    def analysis_nearby_cells(start_cell, cell_group):
        start_x = start_cell.get_pos_x()
        start_y = start_cell.get_pos_y()
        
        for tempCell in cell_group:
            temp_x = tempCell.get_pos_x()
            temp_y = tempCell.get_pos_y()
            
            if start_x == temp_x and start_y == temp_y:
                continue
            elif start_x == temp_x and abs(start_y - temp_y) == 1:
                return tempCell
                
            elif start_y == temp_y and abs(start_x - temp_x) == 1:
                return tempCell
        
        return None 
    
    
    @staticmethod
    def reorder_cells(cell_group):
        '''
        re-order the cells
        '''
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
    def render_map(cell_group):
        '''
        render the map
        '''
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