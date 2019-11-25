class Map_DTO(object):
    '''
    Map_DTO include the cell_list, format is [[pos_x, pos_y],[....]....]
    '''
    
    def __init__(self, map_size):
        self.__map_size = map_size
        self.__cell_list = []
        self.__entrence = None
    
    
    def get_cell_list(self):
        return self.__cell_list
    
    
    def set_cell_list(self, value):
        self.__cell_list = value
        
        
    def get_entrence(self):
        return self.__entrence
    
    
    def set_entrence(self, value):
        self.__entrence = value
        
        

class Cell_DTO(object):
    '''
    
    '''
    
    def __init__(self, pos_x=0, pox_y=0, cell_type=None):
        self.__pos_x = pos_x
        self.__pos_y = pox_y
        # cell type
        self.__type = cell_type
        # nearby cells
        self.__nearby_cells = []
        # cell background
        self.__background_img_idx = None
        '''
        @todo: in future
        '''
        self.__in_combat = False
        self.__enemy_team = None
        self.__special_event = None
    
    
    def get_pos_x(self):
        return self.__pos_x
    
    
    def set_pos_x(self, value):
        self.__pos_x = value
        
    
    def get_pos_y(self):
        return self.__pos_y
    
    
    def set_pos_y(self, value):
        self.__pos_y = value
        
        
    def get_type(self):
        return self.__type
    
    
    def set_type(self, value):
        self.__type = value
        

    def get_nearby_cells(self):
        return self.__nearby_cells
    
    
    def set_nearby_cells(self, value):
        self.__nearby_cells = value
        
    
    def append_nearby_cells(self, value):
        self.__nearby_cells.append(value)


    def get_background_img_idx(self):
        return self.__background_img_idx
    
    
    def set_background_img_idx(self, value):
        self.__background_img_idx = value


    def get_in_combat(self):
        return self.__in_combat
    
    
    def set_in_combat(self, value):
        self.__in_combat = value


class Position_DTO(object):
    '''
    Position DataObject
    NOTE: the default cell size is 100
    '''
    def __init__(self, map_cell=None, cell_position=0, move_direction=None):
        self.__map_cell = map_cell
        self.__cell_position = cell_position
        self.__move_direction = move_direction


    def get_map_cell(self):
        return self.__map_cell


    def get_cell_position(self):
        return self.__cell_position


    def get_move_direction(self):
        return self.__move_direction


    def set_map_cell(self, value):
        self.__map_cell = value


    def set_cell_position(self, value):
        self.__cell_position = value


    def set_move_direction(self, value):
        self.__move_direction = value


    map_cell = property(get_map_cell, set_map_cell, None, None)
    cell_position = property(get_cell_position, set_cell_position, None, None)
    move_direction = property(get_move_direction, set_move_direction, None, None)
    
    
    