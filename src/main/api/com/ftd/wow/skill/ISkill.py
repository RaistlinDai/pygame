'''
Created on Sep 10, 2019

@author: ftd
'''

class ISkill(object):
    '''
    
    '''
    
    def __init__(self, name=None, img=None, img_sel=None, img_inac=None, img_eff=None):
        # give a name
        self.__name = name
        # images
        self.__image = img
        self.__image_select = img_sel
        self.__image_inactive = img_inac
        self.__effect_image = img_eff
    
    
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