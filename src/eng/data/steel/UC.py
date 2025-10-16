from pydantic import Field
from dataclasses import dataclass, field
from .model.steel import Steel

class UC_base(Steel):
    tw: float
    r1: float
    d1: float
    d1_tw: float = Field(alias='d1/tw')
    bf_tw__2tf: float = Field(alias='_(bf-tw)/2tf')
    Zy: float
    compact_y: str
    Zey: float

@dataclass
class UC:
    _310UC158: UC_base = field(metadata={'alias': '310UC158'})
    _310UC137: UC_base = field(metadata={'alias': '310UC137'})
    _310UC118: UC_base = field(metadata={'alias': '310UC118'})
    _310UC96: UC_base = field(metadata={'alias': '310UC96'})
    _250UC89: UC_base = field(metadata={'alias': '250UC89'})
    _250UC72: UC_base = field(metadata={'alias': '250UC72'})
    _200UC59: UC_base = field(metadata={'alias': '200UC59'})
    _200UC52: UC_base = field(metadata={'alias': '200UC52'})
    _200UC46: UC_base = field(metadata={'alias': '200UC46'})
    _150UC37: UC_base = field(metadata={'alias': '150UC37'})
    _150UC30: UC_base = field(metadata={'alias': '150UC30'})
    _150UC23: UC_base = field(metadata={'alias': '150UC23'})
    _100UC14: UC_base = field(metadata={'alias': '100UC14'})

    def __iter__(self):
        yield from self.__dict__.values()
