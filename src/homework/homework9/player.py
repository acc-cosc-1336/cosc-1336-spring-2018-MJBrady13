#write import statement for Die class
from src.homework.homework9.die import Die

'''
Create a Player class.

'''

class Player:

    def __init__(self):
        '''
        Constructor method creates two Die attributes die1 and die2
        '''
        self.die1 = Die()
        self.die2 = Die()


    def roll_doubles(self):
        '''
        The roll_doubles method that will roll die1 and die2 (attributes from constructor method),
        display rolled values,and continue iterating until a double is rolled.
        '''
        num1 = 0
        num2 = 0
        
        double = False

        while double == False:
            num1 = self.die1.roll()
            num2 = self.die2.roll()
            print("Die 1 = ", num1)
            print("Die 2 = ", num2)
            if num1 == num2:
                double = True
                



