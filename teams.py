import random
from hero import Hero

class Team:
    def __init__(self, name):
        ''' Initialize your team with its team name and an empty list of heroes
        '''
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
        #removing the hero
            if hero.name == name:
                self.heroes.remove(hero)
            
                foundHero = True
    
        if not foundHero:
            return 0

    def view_all_heroes(self):

        for hero in self.heroes:
            print(hero)

    def add_hero(self, hero):
        #adding hero to heros
        self.heroes.append(hero)

    def stats(self):
    # team stats
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")

    def revive_heroes(self, health=100):
    # reveiving the heros to full HP
    
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        # To attack the other team 
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:
            hero1 = random.choice(living_heroes)
            hero2 = random.choice(living_opponents)
            hero1.fight(hero2)
            if hero1.is_alive():
                living_opponents.remove(hero2)
            elif hero2.is_alive():
                living_heroes.remove(hero1)
            else:
                living_opponents.remove(hero2)
                living_heroes.remove(hero1)