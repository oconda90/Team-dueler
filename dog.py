
# dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        print("dog initialized!")

    def bark(self):
        print("Woof!")

    def Roll(self):
        print(f'{self.name} has rolled over!')
        
    def Sit(self):
        print(f'{self.name} has Sat!')