from random import randint

class Die():
    """ a class representing a die"""
    def __init__(self,num_sides = 6):
        self.num_sides = num_sides

    def roll(self):
        ''' return a random number between 1 and number of sides'''
        return randint(1, self.num_sides)
