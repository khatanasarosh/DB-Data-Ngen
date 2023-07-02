from src.utils.randomiser.randomiser import Randomiser

import random

class FloatRandomiser(Randomiser):
    def randomise(self, input):
        if isinstance(input, float):
            return random.uniform(0, input)
        else:
            return type(input)

