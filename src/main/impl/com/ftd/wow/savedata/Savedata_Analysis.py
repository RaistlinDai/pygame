'''
Created on Sep 17, 2019

@author: ftd
'''
import json


class Savedata_Analsis (object):
    '''
    
    '''
    
    @staticmethod
    def load_savedata():
        with open('savedata01.json', 'r') as f:
            distros_dict = json.load(f)
        
        for distro in distros_dict:
            print(distro['Name'])