import random


class Weapon():
    def __init__(self, name, hitDie):
        self.name = name
        self.hitDie = hitDie
    
    def getName(self):
        return self.name

    def rollAttack(self):
        return self.hitDie.roll()


class Dice():
    def __init__(self, diceType):
        self.diceType = diceType

    def roll(self):
        return random.randint(1, self.diceType)
