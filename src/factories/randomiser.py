from src.utils.randomiser.randomiser import Randomiser
from src.utils.randomiser.string import StringRandomiser
from src.utils.randomiser.integer import IntegerRandomiser
from src.utils.randomiser.float import FloatRandomiser
from src.utils.randomiser.bool import BoolRandomiser
from src.utils.randomiser.datetime import DateTimeRandomiser
from src.utils.randomiser.default import DefaultRandomiser

import datetime


class RandomiserFactory():

    def get_randomiser(self, data) -> Randomiser:
        if isinstance(data, str):
            return StringRandomiser()
        elif isinstance(data, int):
            return IntegerRandomiser()
        elif isinstance(data, float):
            return FloatRandomiser()
        elif isinstance(data, bool):
            return BoolRandomiser()
        elif isinstance(data, datetime.datetime):
            return DateTimeRandomiser()
        else:
            return DefaultRandomiser()
