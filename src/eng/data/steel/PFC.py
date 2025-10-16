from pydantic import Field
from dataclasses import dataclass, field
from .model.steel import Steel

class PFC_base(Steel):
    tw: float
    r1: float
    d1: float
    d1_tw: float = Field(alias='d1/tw')
    bf_tw__2tf: float = Field(alias='_(bf-tw)/2tf')

@dataclass
class PFC:
    _380PFC: PFC_base = field(metadata={'alias': '380PFC'})
    _300PFC: PFC_base = field(metadata={'alias': '300PFC'})
    _250PFC: PFC_base = field(metadata={'alias': '250PFC'})
    _230PFC: PFC_base = field(metadata={'alias': '230PFC'})
    _200PFC: PFC_base = field(metadata={'alias': '200PFC'})
    _180PFC: PFC_base = field(metadata={'alias': '180PFC'})
    _150PFC: PFC_base = field(metadata={'alias': '150PFC'})
    _125PFC: PFC_base = field(metadata={'alias': '125PFC'})
    _100PFC: PFC_base = field(metadata={'alias': '100PFC'})
    _75PFC: PFC_base = field(metadata={'alias': '75PFC'})

    def __iter__(self):
        yield from self.__dict__.values()
