import random

from attributes import Agile, Sneaky
from characters import Character

class Thief(Sneaky, Agile, Character):
    def pickpocker(self):
        return self.sneaky and bool(random.randing(0,1))
