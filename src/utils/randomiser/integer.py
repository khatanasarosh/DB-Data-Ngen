from src.utils.randomiser.randomiser import Randomiser

import random

class IntegerRandomiser(Randomiser):
    def randomise(self, input):
        if isinstance(input, int):
            return random.randint(0, input)
        else:
            return type(input)
