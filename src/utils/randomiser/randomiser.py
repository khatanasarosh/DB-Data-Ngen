from abc import ABC, abstractmethod

class Randomiser(ABC):
    @abstractmethod
    def randomise(self, input):
        return input
