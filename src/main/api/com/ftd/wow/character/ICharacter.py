'''
Created on Jul 14, 2019

@author: ftd
'''

class ICharacter(object):
    '''
    
    '''
    
    def __init__(self):
        # character status
        self.__resist_physical_dizzy_rate = 0
        self.__is_physical_dizzy = False
        self.__physical_dizzy_duration = 0
        self.__physical_dizzy_immune_duration = 0
        
        self.__resist_magic_transform_rate = 0
        self.__is_magic_transform = False
        self.__magic_transform_duration = 0
        self.__magic_transform_duration_duration = 0
        
        self.__physical_dots = {} # {SkillName: {1:SkillEffect, 2:SkillEffect}}
        self.__magic_dots = {}    # {SkillName: {1:SkillEffect, 2:SkillEffect}}
        
        self.__physical_hots = {} # {SkillName: {1:SkillEffect, 2:SkillEffect}}
        self.__magic_hots = {}    # {SkillName: {1:SkillEffect, 2:SkillEffect}}
        
        self.__debuffs = {}       # {SkillName: {1:SkillEffect, 2:SkillEffect}}
        self.__buffs = {}         # {SkillName: {1:SkillEffect, 2:SkillEffect}}


    def get_physical_hots(self):
        return self.__physical_hots


    def get_magic_hots(self):
        return self.__magic_hots


    def set_physical_hots(self, value):
        self.__physical_hots = value


    def set_magic_hots(self, value):
        self.__magic_hots = value


    def del_physical_hots(self):
        del self.__physical_hots


    def del_magic_hots(self):
        del self.__magic_hots


    def get_resist_physical_dizzy_rate(self):
        return self.__resist_physical_dizzy_rate


    def get_is_physical_dizzy(self):
        return self.__is_physical_dizzy


    def get_physical_dizzy_duration(self):
        return self.__physical_dizzy_duration


    def get_physical_dizzy_immune_duration(self):
        return self.__physical_dizzy_immune_duration


    def get_resist_magic_transform_rate(self):
        return self.__resist_magic_transform_rate


    def get_is_magic_transform(self):
        return self.__is_magic_transform


    def get_magic_transform_duration(self):
        return self.__magic_transform_duration


    def get_magic_transform_duration_duration(self):
        return self.__magic_transform_duration_duration


    def get_physical_dots(self):
        return self.__physical_dots


    def get_magic_dots(self):
        return self.__magic_dots


    def get_debuffs(self):
        return self.__debuffs


    def get_buffs(self):
        return self.__buffs


    def set_resist_physical_dizzy_rate(self, value):
        self.__resist_physical_dizzy_rate = value


    def set_is_physical_dizzy(self, value):
        self.__is_physical_dizzy = value


    def set_physical_dizzy_duration(self, value):
        self.__physical_dizzy_duration = value


    def set_physical_dizzy_immune_duration(self, value):
        self.__physical_dizzy_immune_duration = value


    def set_resist_magic_transform_rate(self, value):
        self.__resist_magic_transform_rate = value


    def set_is_magic_transform(self, value):
        self.__is_magic_transform = value


    def set_magic_transform_duration(self, value):
        self.__magic_transform_duration = value


    def set_magic_transform_duration_duration(self, value):
        self.__magic_transform_duration_duration = value


    def set_physical_dots(self, value):
        self.__physical_dots = value


    def add_physical_dot(self, key, value):
        self.__physical_dots[key] = value


    def set_magic_dots(self, value):
        self.__magic_dots = value


    def add_magic_dot(self, key, value):
        self.__magic_dots[key] = value


    def set_debuffs(self, value):
        self.__debuffs = value


    def add_debuff(self, key, value):
        self.__debuffs[key] = value


    def set_buffs(self, value):
        self.__buffs = value


    def add_buff(self, key, value):
        self.__buffs[key] = value


    def del_resist_physical_dizzy_rate(self):
        del self.__resist_physical_dizzy_rate


    def del_is_physical_dizzy(self):
        del self.__is_physical_dizzy


    def del_physical_dizzy_duration(self):
        del self.__physical_dizzy_duration


    def del_physical_dizzy_immune_duration(self):
        del self.__physical_dizzy_immune_duration


    def del_resist_magic_transform_rate(self):
        del self.__resist_magic_transform_rate


    def del_is_magic_transform(self):
        del self.__is_magic_transform


    def del_magic_transform_duration(self):
        del self.__magic_transform_duration


    def del_magic_transform_duration_duration(self):
        del self.__magic_transform_duration_duration


    def del_physical_dots(self):
        del self.__physical_dots


    def del_magic_dots(self):
        del self.__magic_dots


    def del_debuffs(self):
        del self.__debuffs


    def del_buffs(self):
        del self.__buffs

    
    def get_stand_image(self):
        pass
    
    
    resist_physical_dizzy_rate = property(get_resist_physical_dizzy_rate, set_resist_physical_dizzy_rate, del_resist_physical_dizzy_rate, "resist_physical_dizzy_rate's docstring")
    is_physical_dizzy = property(get_is_physical_dizzy, set_is_physical_dizzy, del_is_physical_dizzy, "is_physical_dizzy's docstring")
    physical_dizzy_duration = property(get_physical_dizzy_duration, set_physical_dizzy_duration, del_physical_dizzy_duration, "physical_dizzy_duration's docstring")
    physical_dizzy_immune_duration = property(get_physical_dizzy_immune_duration, set_physical_dizzy_immune_duration, del_physical_dizzy_immune_duration, "physical_dizzy_immune_duration's docstring")
    resist_magic_transform_rate = property(get_resist_magic_transform_rate, set_resist_magic_transform_rate, del_resist_magic_transform_rate, "resist_magic_transform_rate's docstring")
    is_magic_transform = property(get_is_magic_transform, set_is_magic_transform, del_is_magic_transform, "is_magic_transform's docstring")
    magic_transform_duration = property(get_magic_transform_duration, set_magic_transform_duration, del_magic_transform_duration, "magic_transform_duration's docstring")
    magic_transform_duration_duration = property(get_magic_transform_duration_duration, set_magic_transform_duration_duration, del_magic_transform_duration_duration, "magic_transform_duration_duration's docstring")
    physical_dots = property(get_physical_dots, set_physical_dots, del_physical_dots, "physical_dots's docstring")
    magic_dots = property(get_magic_dots, set_magic_dots, del_magic_dots, "magic_dots's docstring")
    debuffs = property(get_debuffs, set_debuffs, del_debuffs, "debuffs's docstring")
    buffs = property(get_buffs, set_buffs, del_buffs, "buffs's docstring")
    physical_hots = property(get_physical_hots, set_physical_hots, del_physical_hots, "physical_hots's docstring")
    magic_hots = property(get_magic_hots, set_magic_hots, del_magic_hots, "magic_hots's docstring")
    
    
    