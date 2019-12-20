class Map_DTO(object):
    '''
    Map_DTO include the cell_list, format is [[pos_x, pos_y],[....]....]
    '''
    
    def __init__(self, map_size):
        self.__map_size = map_size
        self.__cell_list = []
        self.__entrence = None
        self.__background_img_idx = None
        
        
    def get_map_size(self):
        return self.__map_size
    
    
    def set_map_size(self, value):
        self.__map_size = value
        
        
    def get_cell_list(self):
        return self.__cell_list
    
    
    def set_cell_list(self, value):
        self.__cell_list = value
        
        
    def get_entrence(self):
        return self.__entrence
    
    
    def set_entrence(self, value):
        self.__entrence = value


    def get_background_img_idx(self):
        return self.__background_img_idx
    
    
    def set_background_img_idx(self, value):
        self.__background_img_idx = value
        
        
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
        # cell foreground
        self.__cell_items = []
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
    
    
    def set_cell_items(self, value):
        self.__cell_items = value


    def get_cell_items(self):
        return self.__cell_items
    
    
    def append_cell_item(self, value):
        if isinstance(value, Cell_Item_DTO):
            self.__cell_items.append(value)


    def get_in_combat(self):
        return self.__in_combat
    
    
    def set_in_combat(self, value):
        self.__in_combat = value


class Position_DTO(object):
    '''
    Position DataObject
    NOTE: the default cell size is 100, and cell_position starts from 0 to 100
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
    
    
class Cell_Item_DTO(object):
    '''
    Cell Item DataObject
    '''
    def __init__(self, item_image=None, item_type=None, item_size=None, item_position=None, level_idx=0):
        self.__item_image = item_image
        self.__item_type = item_type
        self.__level_idx = level_idx
        self.__item_size = item_size
        self.__item_position = item_position


    def get_item_position(self):
        return self.__item_position


    def set_item_position(self, value):
        self.__item_position = value


    def del_item_position(self):
        del self.__item_position

        
    def get_item_image(self):
        return self.__item_image


    def get_item_type(self):
        return self.__item_type


    def get_item_size(self):
        return self.__item_size


    def get_level_idx(self):
        return self.__level_idx


    def set_item_image(self, value):
        self.__item_image = value


    def set_item_type(self, value):
        self.__item_type = value


    def set_item_size(self, value):
        self.__item_size = value


    def set_level_idx(self, value):
        self.__level_idx = value


    def del_item_image(self):
        del self.__item_image


    def del_item_type(self):
        del self.__item_type


    def del_level_idx(self):
        del self.__level_idx

    item_image = property(get_item_image, set_item_image, del_item_image, "item_image's docstring")
    item_type = property(get_item_type, set_item_type, del_item_type, "item_type's docstring")
    level_idx = property(get_level_idx, set_level_idx, del_level_idx, "level_idx's docstring")
    item_position = property(get_item_position, set_item_position, del_item_position, "item_position's docstring")
