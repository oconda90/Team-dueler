import random 
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        '''Add ability to abilities list '''
        self.abilities.append(ability)

    def add_armor(self, armor):
        '''Add armor to armors list '''
        self.armors.append(armor)

    def attack(self):
        '''Calculate the total damage from all ability attacks.'''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self, damage_amt):
        ''' Calculate total block amount from all armor'''
        total_block = 0
        for armor in self.armors:
            total_block += armor.block()
        return damage_amt - total_block

    def take_damage(self, damage):
        '''Updates self.current_health to reflect the damage minus the defense.
        '''
        self.current_health -= self.defend(damage)

    def is_alive(self):  
        '''Return True or False depending on whether the hero is alive or not.
        '''
        #seeing if hero is alive method
        if self.current_health <= 0:
            return False
        else: 
            return True

    def fight(self, opponent):  
        #Fight method
        if len(self.abilities) == 0 and len(opponent.abilities) == 0:
            print("Draw!")
            return
        else:
            while self.is_alive() == True and opponent.is_alive() == True:
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
            if self.is_alive() == True:
                print(f"{self.name} won")
            elif opponent.is_alive() == True:
                print(f"{opponent.name} won")
    
    def add_weapon(self, weapon):
        self.abilities.append(weapon)
    
    def add_death(self, num_deaths):
    # ''' Update deaths with num_deaths'''
    
        self.deaths += num_deaths

    def add_kill(self, num_kills):
    # ''' Update self.kills by num_kills amount'''
        self.kills += num_kills

if __name__ == "__main__":
    
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)