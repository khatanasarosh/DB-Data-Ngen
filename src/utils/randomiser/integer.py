from src.utils.randomiser.randomiser import Randomiser

import random

class IntegerRandomiser(Randomiser):
    def randomise(self, value: int) -> int:
        lower_limit = int('1' + ('0' * (len(str(value)) - 1)))
        upper_limit = int('9' * len(str(value)))

        return random.randint(lower_limit, upper_limit)
