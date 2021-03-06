import random


class Armor():
    def __init__(self, name, max_block):
        '''Instantiate instance properties. 
        name: string
        max_block: int
        '''
        self.name = name
        self.max_block = max_block
    
    def block(self):
        ''' 
        Return a random value between 0 and the initialized
        max_block strength.
        '''
        random_value = random.randint(0, int(self.max_block))
        return random_value
    
if __name__ == "__main__":
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())