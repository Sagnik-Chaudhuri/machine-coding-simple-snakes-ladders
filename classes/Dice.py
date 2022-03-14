import math
from random import randint, random


class Dice():
    def __init__(self, number_of_dice) -> None:
        self.number_of_dice = number_of_dice

    def roll_dice(self):
        return randint(1, 6)*self.number_of_dice
