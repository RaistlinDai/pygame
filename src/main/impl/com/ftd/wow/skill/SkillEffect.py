'''
Created on Sep 30, 2019

@author: ftd
'''
class SkillEffect(object):
    '''
    classdocs
    @attention: the value structure: skills constructor
    '''
    
        
    # debuff
    REDUCE_ATTACK = 1
    REDUCE_DEFENSE = 2
    REDUCE_SPEED = 3
    # buff
    ADD_ATTACK = 11
    ADD_DEFENSE = 12
    ADD_SPEED = 13
    # physical control
    CONTROL_DIZZY = 21
    CONTROL_TRANSFORM = 22
    # movement
    MOVE_FRIENDLY = 31
    MOVE_ENEMY = 32
    # dot
    DOT_PHYSICAL = 41
    DOT_MAGIC = 42
    DOT_CURSE = 43
    DOT_PLAGUE = 44
    

    def __init__(self, skill_effect_type=None, skill_effect_value=0, skill_effect_rate=0, skill_effect_duration=0, skill_is_stackable=False):
        '''
        @param skill_effect_type: effect type, e.g. CONTROL_DIZZY
        @param skill_effect_value: effect value, e.g. reduce speed 5
        @param skill_effect_rate: effect rate, e.g. reduce attack 10%
        @param skill_effect_duration: effect duration, e.g. duration 2 round
        @param skill_is_stackable: is effect stackable
        '''
        self.__skill_effect_type = skill_effect_type
        self.__skill_effect_value = skill_effect_value
        self.__skill_effect_rate = skill_effect_rate
        self.__skill_effect_duration = skill_effect_duration
        self.__skill_is_stackable = skill_is_stackable


    def get_skill_is_stackable(self):
        return self.__skill_is_stackable


    def set_skill_is_stackable(self, value):
        self.__skill_is_stackable = value


    def del_skill_is_stackable(self):
        del self.__skill_is_stackable


    def get_skill_effect_type(self):
        return self.__skill_effect_type


    def get_skill_effect_value(self):
        return self.__skill_effect_value


    def get_skill_effect_rate(self):
        return self.__skill_effect_rate


    def get_skill_effect_duration(self):
        return self.__skill_effect_duration


    def set_skill_effect_type(self, value):
        self.__skill_effect_type = value


    def set_skill_effect_value(self, value):
        self.__skill_effect_value = value


    def set_skill_effect_rate(self, value):
        self.__skill_effect_rate = value


    def set_skill_effect_duration(self, value):
        self.__skill_effect_duration = value


    def del_skill_effect_type(self):
        del self.__skill_effect_type


    def del_skill_effect_value(self):
        del self.__skill_effect_value


    def del_skill_effect_rate(self):
        del self.__skill_effect_rate


    def del_skill_effect_duration(self):
        del self.__skill_effect_duration

    skill_effect_type = property(get_skill_effect_type, set_skill_effect_type, del_skill_effect_type, "skill_effect_type's docstring")
    skill_effect_value = property(get_skill_effect_value, set_skill_effect_value, del_skill_effect_value, "skill_effect_value's docstring")
    skill_effect_rate = property(get_skill_effect_rate, set_skill_effect_rate, del_skill_effect_rate, "skill_effect_rate's docstring")
    skill_effect_duration = property(get_skill_effect_duration, set_skill_effect_duration, del_skill_effect_duration, "skill_effect_duration's docstring")
    skill_is_stackable = property(get_skill_is_stackable, set_skill_is_stackable, del_skill_is_stackable, "skill_is_stackable's docstring")

    