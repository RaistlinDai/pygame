'''
Created on Sep 11, 2019

@author: ftd
'''
from src.main.impl.com.ftd.wow.util.Map_Util import CellItemSize_Enum
from src.main.impl.com.ftd.wow.const.Scene_Constant import Scene_Constant

class Image_Util(object):
    '''
    
    '''
    
    @staticmethod
    def calculate_backround_image_size(img, screen_w, screen_h):
        '''
        The background images might not be in 4:3 rate, so it has to be calculated before transform
        '''
        pass
        
    
    @staticmethod
    def calculate_bottom_bar_height_by_screen_size(screen_h):
        '''
        Calculate the standard bottom bar height according to the screen's height
        The default value is 250 in 1280*720
        @param screen_h: the height of screen
        @return: the standard height of bottom bar 
        '''
        standard_h = 250 * screen_h / 720
        return round(standard_h)
    
    
    @staticmethod
    def calculate_bottom_bar_positionY_by_screen_size(screen_h):
        '''
        Calculate the standard bottom bar position according to the screen's height
        The default value is 470 in 1280*720
        @param screen_h: the height of screen
        @return: the standard positionY of bottom bar 
        '''
        standard_y = 470 * screen_h / 720
        return round(standard_y)
    
    
    @staticmethod
    def calculate_top_bar_height_by_screen_size(screen_h):
        '''
        Calculate the standard top bar height according to the screen's height
        The default value is 96 in 1280*720
        @param screen_h: the height of screen
        @return: the standard height of top bar 
        '''
        standard_h = 96 * screen_h / 720
        return round(standard_h)

    
    @staticmethod
    def calculate_character_move_height_by_screen_size(screen_h):
        '''
        Calculate the standard character height according to the screen's height
        The default value is 100 in 1280*720
        @param character_h: the height of screen
        @return: the standard height of character 
        '''
        standard_h = 180 * screen_h / 720
        return round(standard_h)
    
    
    @staticmethod
    def calculate_character_move_width_by_height(character_image, character_h):
        '''
        @param character_image: the height of character
        @param: character_h: the standard height of character 
        '''
        w, h = character_image.get_size()
        character_w = w * character_h / h
        return round(character_w)
    
    
    @staticmethod
    def calculate_character_combat_height_by_screen_size(character_h):
        '''
        Calculate the standard character height according to the screen's height
        The default value is 100 in 1280*720
        @param character_h: the height of screen
        @return: the standard height of character 
        '''
        standard_h = 100 * character_h / 720
        return round(standard_h)
    
    
    @staticmethod
    def calculate_character_combat_width_by_height(character_image, character_h):
        '''
        @param character_image: the image of character
        @param: character_h: the standard height of character 
        '''
        w, h = character_image.get_size()
        character_w = w * character_h / h
        return round(character_w)
    
    
    @staticmethod
    def calculate_character_move_position_by_screen_size(screen_w, screen_y, team_position, profession_image_rate):
        '''
        Calculate the standard character position according to the screen's size
        The default value is 1:50-450, 2:150-450, 3:250-450, 4:350-450 in 1280*720
        @param screen_h: the height of screen
        @return: the standard position of character 
        '''
        standard_x = (200 + 150 * (team_position - 1)) * screen_w / 1280
        standard_y = (550 - 180 * profession_image_rate) * screen_y / 720
        return (int(standard_x), round(standard_y))
    
    
    @staticmethod
    def calculate_character_combat_position_by_screen_size(screen_w, screen_y, team_position, profession_image_rate):
        '''
        Calculate the standard character position according to the screen's size
        The default value is 1:50-450, 2:150-450, 3:250-450, 4:350-450 in 1280*720
        @param screen_h: the height of screen
        @return: the standard position of character 
        '''
        standard_x = (50 + 100 * (team_position - 1)) * screen_w / 1280
        standard_y = (550 - 100 * profession_image_rate) * screen_y / 720
        return (int(standard_x), round(standard_y))
    
    
    @staticmethod
    def calculate_enemy_position_by_screen_size(screen_w, screen_y, team_position, profession_image_rate):
        '''
        Calculate the standard enemy position according to the screen's size
        The default value is 1:750-450, 2:830-450, 3:960-450, 4:1090-450 in 1280*720
        @param screen_h: the height of screen
        @return: the standard position of character 
        '''
        standard_x = (750 + 130 * (team_position - 1)) * screen_w / 1280
        standard_y = (550 - 100 * profession_image_rate) * screen_y / 720
        return (int(standard_x), round(standard_y))
    
    
    @staticmethod
    def calculate_character_in_fight_height_by_screen_size(screen_h):
        '''
        Calculate the fighting character height according to the screen's height
        The default value is 100 in 1280*720
        @param screen_h: the height of screen
        @return: the standard height of character 
        '''
        standard_h = 200 * screen_h / 720
        return round(standard_h)
    
    
    @staticmethod
    def calculate_character_in_fight_position_by_screen_size(screen_w, screen_y, team_position, profession_image_rate):
        '''
        Calculate the standard character position according to the screen's size
        The default value is 1:50-450, 2:150-450, 3:250-450, 4:350-450 in 1280*720
        @param screen_h: the height of screen
        @return: the standard position of character 
        '''
        standard_x = (50 + 50 * (team_position - 1)) * screen_w / 1280
        standard_y = (380 - 100 * profession_image_rate) * screen_y / 720
        return (int(standard_x), round(standard_y))


    
    @staticmethod
    def calculate_enemy_in_fight_position_by_screen_size(screen_w, screen_y, team_position, profession_image_rate):
        '''
        Calculate the standard character position according to the screen's size
        The default value is 1:50-450, 2:150-450, 3:250-450, 4:350-450 in 1280*720
        @param screen_h: the height of screen
        @return: the standard position of character 
        '''
        standard_x = (750 + 50 * (team_position - 1)) * screen_w / 1280
        standard_y = (380 - 100 * profession_image_rate) * screen_y / 720
        return (int(standard_x), round(standard_y))
    
    
    @staticmethod
    def calculate_skill_in_fight_height_by_screen_size(screen_h):
        '''
        Calculate the skill label height according to the screen's height
        The default value is 50 in 1280*720
        @param skill_image: the height of skill label
        @return: standard_h: the standard height of skill 
        '''
        standard_h = 60 * screen_h / 720
        return round(standard_h)
    
    
    @staticmethod
    def calculate_skill_in_fight_positionX_by_screen_size(screen_w, label_idx):
        '''
        Calculate the skill label position X according to the screen's width
        The default value is (400 + label_idx * 80) in 1280*720
        @param screen_w: the width of screen
        @param label_idx: the label index
        @return: standard_X: the standard position X of skill 
        '''
        standard_X = 200 * screen_w / 1280 + label_idx * (60 * screen_w / 1280)
        return round(standard_X)
    
     
    @staticmethod
    def calculate_skill_in_fight_positionY_by_screen_size(screen_h):
        '''
        Calculate the skill label position Y according to the screen's height
        The default value is 600 in 1280*720
        @param screen_h: the height of screen
        @return: standard_Y: the standard position Y of skill 
        '''
        standard_Y = 570 * screen_h / 720
        return round(standard_Y)
    
    
    @staticmethod
    def calculate_skill_in_fight_size_by_screen_size(screen_h):
        '''
        Calculate the skill label size according to the screen's height
        The default value is 70 in 1280*720
        @param screen_h: the height of screen
        @return: standard_size: the standard size of skill 
        '''
        standard_size = 50 * screen_h / 720
        return round(standard_size)
    
    
    @staticmethod
    def calculate_skill_effect_size_by_screen_size(screen_w, screen_h):
        '''
        Calculate the skill effect size according to the screen's size
        The default value is 500,300 in 1280*720
        @param screen_w: the width of screen
        @param screen_h: the height of screen
        @return: standard_w, standard_h: the standard size of skill 
        '''
        standard_w = 500 * screen_w / 1280
        standard_h = 300 * screen_h / 720
        return (int(standard_w), round(standard_h))
    
    
    @staticmethod
    def calculate_map_item_size_by_screen_size(item_image, item_size_type, screen_h):
        '''
        Calculate the map item's size according to the screen's size
        The default screen is 1280*720, and the default height of each size are B:600,M:300,S:150
        @param item_image: the item image
        @param item_size_type: the item type (big,mid,small)
        @param screen_h: the height of screen
        '''
        w, h = item_image.get_size()
        cal_h = h
        if item_size_type == CellItemSize_Enum.SIZE_BIG:
            cal_h = 600 * screen_h / 720
        elif item_size_type == CellItemSize_Enum.SIZE_MIDDLE:
            cal_h = 300 * screen_h / 720
        else:
            cal_h = 150 * screen_h / 720
            
        cal_w = w * cal_h / h
        return round(cal_w), round(cal_h)
    
    
    @staticmethod
    def calculate_map_item_position(item_position_in_cell, item_image_w, cell_position, screen_w):
        '''
        
        '''
        screen_start_pos_x = cell_position * screen_w / Scene_Constant.SCENE_CELL_WIDTH
        item_cal_pos_x = item_position_in_cell * screen_w / Scene_Constant.SCENE_CELL_WIDTH
        
        if item_cal_pos_x + item_image_w < screen_start_pos_x:
            return False, 0
        else:
            return True, item_cal_pos_x - screen_start_pos_x
        
        