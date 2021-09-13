import random as rd

class Die(object):
    """description of class"""

    def __init__(self,num_sides=6):
        """assumed 6 sided die"""
        self.num_sides = num_sides

    def roll(self):
        """random number between 1 and number of sides"""

        return rd.randint(1,self.num_sides)

