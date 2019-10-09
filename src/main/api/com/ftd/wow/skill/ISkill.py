'''
Created on Sep 10, 2019

@author: ftd
'''

class ISkill(object):
    '''
    
    '''
    
    # skill damage range
    LOW_DAMAGE = 1
    MIDDLE_DAMAGE = 2
    HIGH_DAMAGE = 3
    
    def __init__(self, name, skill_images, skill_properties=None):
        '''
        @param skill_images: 0: skill_normal_image
                             1: skill_selected_image
                             2: skill_inactive_image
                             3: skill_effect_image
        @param skill_properties: 0: skill_damage_range;
                                 1: skill_damage_rate;
                                 2: skill_hit_rate;
                                 3: skill_setup;
                                 4: skill_boot;
                                 5: skill_range;
                                 6: skill_extention_value;
                                 7: skill_target;  0-self;1-target
                                 8: skill_special_effects[];
                                 
        '''
        
        # set default values
        self.__damage_range = 0
        self.__damage_rate = 1
        self.__hit_rate = 0
        self.__setup = 0
        self.__boot = 0
        self.__range = 1
        self.__extension_value = 0
        self.__target = 1
        self.__speical_effects = []
        self.__image = None
        self.__image_select = None
        self.__image_inactive = None
        self.__effect_image = None
        
        # give a name
        self.__name = name
        
        # images
        if skill_images and len(skill_images) > 0:
            self.__image = skill_images[0]
            self.__image_select = skill_images[1]
            self.__image_inactive = skill_images[2]
            self.__effect_image = skill_images[3]
        
        # properties
        if skill_properties and len(skill_properties) >= 9:
            self.__damage_range = skill_properties[0]
            self.__damage_rate = skill_properties[1]
            self.__hit_rate = skill_properties[2]
            self.__setup = skill_properties[3]
            self.__boot = skill_properties[4]
            self.__range = skill_properties[5]
            self.__extention_value = skill_properties[6]
            self.__target = skill_properties[7]
            self.__speical_effects = skill_properties[8]
    
    
    def get_skill_name(self):
        return self.__name
    
    
    def get_skill_image(self):
        return self.__image


    def get_skill_image_select(self):
        return self.__image_select
    
    
    def get_skill_image_inactive(self):
        return self.__image_inactive
    
    
    def get_effect_image(self):
        return self.__effect_image
    
    
    def get_damage_range(self):
        return self.__damage_range
    
    
    def get_damage_rate(self):
        return self.__damage_rate
    
    
    def get_hit_rate(self):
        return self.__hit_rate
    
    
    def get_setup(self):
        return self.__setup
    
    
    def get_boot(self):
        return self.__boot
    
    
    def get_range(self):
        return self.__range
    
    
    def get_target(self):
        return self.__target
    
    
    def get_extension_value(self):
        return self.__extension_value
    
    
    def get_speical_effects(self):
        return self.__speical_effects