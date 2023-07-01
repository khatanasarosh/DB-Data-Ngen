from app.src.utils.randomiser.randomiser import Randomiser

import random
import string

class StringRandomiser(Randomiser):
    def randomise(self, input):
        if isinstance(input, str):
            return ''.join(self.randomise_char(char) for char in input)
        else:
            return type(input)
    
    def randomise_char(self, char):
        if char.isalpha():
            if char.isupper():
                return random.SystemRandom().choice(string.ascii_uppercase)
            return random.SystemRandom().choice(string.ascii_lowercase)
        elif char.isdigit():
            return random.SystemRandom().choice(string.digits)
        else:
            return char
