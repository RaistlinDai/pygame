'''
Created on Sep 27, 2019

@author: ftd
'''
import math
import random
from src.main.api.com.ftd.wow.character.ICharacter import ICharacter
from src.main.api.com.ftd.wow.skill.ISkill import ISkill
from src.main.impl.com.ftd.wow.skill.SkillEffect import SkillEffect

class Fight_Util(object):
    '''
    @summary: The flow of a fighting round:
                1. calculate all the characters' orders by speed
                2. disturb the orders by default rate (15%)
                3. invert the orders by default rate (20%)
                4. focus on on the attack character's turn
                   4.1. calculate the HOT/DOT on attack character
                   4.2. calculate the HOT/DOT/buff/debuff durations
                   4.3. calculate fighting                                       --- calculate_fighting
                        4.3.1. calculate basic attack of attack character        --- calculate_basic_attack
                        4.3.2. calculate basic defense of defense character      --- calculate_basic_defense
                        4.3.3. separate skill special effects into two groups    --- separate_skill_special_effect
                        4.3.4. calculate skill of attack character               --- calculate_skill
                        4.3.5. calculate buffs/debuffs effects                   --- 
                        4.3.6. calculate skill hit rate                          --- calculate_skill_hit_rate
                               if missing then return
                        4.3.7. calculate skill critical attack                   --- calculate_skill_critical
                        4.3.8. calculate the final damage                        --- calculate_skill_critical
                        4.3.9. arrange skill special effects to characters       --- arrange_skill_special_effect_to_character
    '''
    
    
    @staticmethod
    def calculate_characters_orders():
        orders = []
        
        return orders
        
    
    @staticmethod
    def calculate_before_fighting(attack_character):
        '''
        In this method it will calculate the DOT/HOT and character status before the coming fighting round
        @param attack_character: the attack character
        '''
        pass
    
    
    @staticmethod
    def calculate_fighting(attack_character, defense_character, skill):
        final_damage = 0
        is_critical = False
        
        # calculate character basic attack
        calculated_attack, calculated_critical, calculated_critical_damage = Fight_Util.calculate_basic_attack(attack_character)
        
        # calculate character basic defense
        calculated_defense, calculated_dodge = Fight_Util.calculate_basic_defense(defense_character)
            
        # calculate character skill attack
        calculated_hit_rate, calculated_attack = Fight_Util.calculate_skill(skill, calculated_dodge, calculated_attack)
            
        # separate the skill special effects
        skill_special_effects_on_self, skill_special_effects_on_target = Fight_Util.separate_skill_special_effect(skill)
        
        # calculate existing buffs/debuffs
        
            
        # calculate skill hit rate
        is_hit = Fight_Util.calculate_skill_hit_rate(calculated_hit_rate)
        
        if is_hit:
            # calculate critical attack
            is_critical, calculated_attack = \
                Fight_Util.calculate_skill_critical(calculated_attack, calculated_critical, calculated_critical_damage)
            
            # calculate the final damage by calculated attack and calculated defense
            final_damage = Fight_Util.calculate_final_damage(calculated_attack, calculated_defense)
                
            # arrange skill special effect
            Fight_Util.arrange_skill_special_effect_to_character(attack_character, \
                                                                 defense_character, \
                                                                 skill_special_effects_on_self, \
                                                                 skill_special_effects_on_target)
            
            print('debuffs:', defense_character.get_debuffs())
        
        print(is_hit, is_critical, final_damage)
        return is_hit, is_critical, final_damage
    
    
    @staticmethod
    def separate_skill_special_effect(skill):
        
        '''
        separate the skill effect onto self-character or target-character
        '''
        skill_special_effects_on_self = {}
        skill_special_effects_on_target = {}
        
        if skill and isinstance(skill, ISkill):
            temp_effects = skill.get_speical_effects()
            if temp_effects and len(temp_effects) > 0:
                for temp_skill_effect in temp_effects:
                    if skill.get_target() == 0:
                        skill_special_effects_on_self[skill.get_skill_name()] = temp_skill_effect
                    else:
                        skill_special_effects_on_target[skill.get_skill_name()] = temp_skill_effect
        
        return skill_special_effects_on_self, skill_special_effects_on_target
                
                
    @staticmethod
    def arrange_skill_special_effect_to_character(attack_character, \
                                                  defense_character, \
                                                  skill_special_effects_on_self, \
                                                  skill_special_effects_on_target):
        
        # arrange on self character
        if attack_character and isinstance(attack_character, ICharacter) and \
            skill_special_effects_on_self and len(skill_special_effects_on_self) > 0:
            
            existing_skill_debuffs = attack_character.get_debuffs()
            existing_skill_buffs = attack_character.get_buffs()
            
            for temp_skill in skill_special_effects_on_self.items():
                if temp_skill[1].get_skill_effect_type() == SkillEffect.REDUCE_ATTACK:
                    print(temp_skill[0])
                elif temp_skill[1].get_skill_effect_type() == SkillEffect.REDUCE_DEFENSE:
                    print(temp_skill[0])
                elif temp_skill[1].get_skill_effect_type() == SkillEffect.REDUCE_SPEED:
                    print(temp_skill[0])
        
        # arrange on target character
        if defense_character and isinstance(defense_character, ICharacter) and \
            skill_special_effects_on_target and len(skill_special_effects_on_target) > 0:
            
            existing_skill_debuffs = defense_character.get_debuffs()
            existing_skill_magic_dots = defense_character.get_magic_dots()
            existing_skill_physical_dots = defense_character.get_physical_dots()
            
            for temp_skill in skill_special_effects_on_target.items():
                # stackable skill effect
                if temp_skill[0] in existing_skill_debuffs and temp_skill[1].get_skill_is_stackable():
                    last_idx = len(existing_skill_debuffs[temp_skill[0]])
                    existing_skill_debuffs[temp_skill[0]][last_idx + 1] = temp_skill[1]
                
                elif temp_skill[0] in existing_skill_magic_dots and temp_skill[1].get_skill_is_stackable():
                    last_idx = len(existing_skill_magic_dots[temp_skill[0]])
                    existing_skill_magic_dots[temp_skill[0]][last_idx + 1] = temp_skill[1]
                
                elif temp_skill[0] in existing_skill_physical_dots and temp_skill[1].get_skill_is_stackable():
                    last_idx = len(existing_skill_physical_dots[temp_skill[0]])
                    existing_skill_physical_dots[temp_skill[0]][last_idx + 1] = temp_skill[1]        
                    
                elif temp_skill[1].get_skill_effect_type() == SkillEffect.REDUCE_ATTACK or \
                     temp_skill[1].get_skill_effect_type() == SkillEffect.REDUCE_DEFENSE or \
                     temp_skill[1].get_skill_effect_type() == SkillEffect.REDUCE_SPEED:
                    existing_skill_debuffs[temp_skill[0]] = {1:temp_skill[1]}
                    
                elif temp_skill[1].get_skill_effect_type() == SkillEffect.DOT_MAGIC:
                    existing_skill_magic_dots[temp_skill[0]] = {1:temp_skill[1]}
                    
                elif temp_skill[1].get_skill_effect_type() == SkillEffect.DOT_PHYSICAL:
                    existing_skill_physical_dots[temp_skill[0]] = {1:temp_skill[1]}
            
    
    @staticmethod
    def calculate_basic_attack(attack_character):
        if attack_character and isinstance(attack_character, ICharacter):
            character_level = attack_character.get_level()
            character_weapon = attack_character.get_weapon()
            prof = attack_character.get_profession()
            prof_basic_attack = prof.get_basic_attack()
            prof_basic_rate = prof.get_basic_rate()
            
            calculated_critical = prof.get_basic_critical()
            calculated_critical_damage = prof.get_basic_critical_damage()
            
            # calculate character basic attack
            calculated_attack = prof_basic_attack * math.pow(prof_basic_rate, (character_level - 1)) + character_weapon
            
            return calculated_attack, calculated_critical, calculated_critical_damage
    
    
    @staticmethod
    def calculate_basic_defense(defense_character):
        if defense_character and isinstance(defense_character, ICharacter):
            character_level = defense_character.get_level()
            character_amour = defense_character.get_amour()
            prof = defense_character.get_profession()
            prof_basic_defense = prof.get_basic_defense()
            prof_basic_rate = prof.get_basic_rate()
            calculated_dodge = prof.get_basic_dodge()
            
            # calculate character basic defense
            calculated_defense = prof_basic_defense * math.pow(prof_basic_rate, (character_level - 1)) + character_amour
            
            return calculated_defense, calculated_dodge
    
    
    @staticmethod
    def calculate_skill(skill, calculated_dodge, calculated_attack):
        calculated_hit_rate = 0
        if skill and isinstance(skill, ISkill):
            skill_damage_range = skill.get_damage_range()
            skill_damage_rate = skill.get_damage_rate()
            
            calculated_hit_rate = skill.get_hit_rate() - calculated_dodge
            random_skill_damage = random.randint(0,skill_damage_range)
            calculated_attack = (calculated_attack + random_skill_damage) * skill_damage_rate / 100
            
        return calculated_hit_rate, calculated_attack
    
    
    @staticmethod
    def calculate_skill_hit_rate(calculated_hit_rate):
        is_hit = False
        random_hit_rate = random.randint(0,100)
        if 0 < random_hit_rate < calculated_hit_rate:
            is_hit = True
    
        return is_hit
    
    
    @staticmethod
    def calculate_skill_critical(calculated_attack, calculated_critical, calculated_critical_damage):
        is_critical = False
        random_critical_rate = random.randint(0,100)
        if 0 < random_critical_rate < calculated_critical:
            calculated_attack = calculated_attack * calculated_critical_damage / 100
            is_critical = True
        
        return is_critical, calculated_attack
    
    
    @staticmethod
    def calculate_final_damage(calculated_attack, calculated_defense):
        final_damage = round(calculated_attack - calculated_defense)
        if final_damage < 0:
            final_damage = 0
            
        return final_damage