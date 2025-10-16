from pydantic import Field
from dataclasses import dataclass, field
from .model.steel import Steel

class UB_base(Steel):
    tw: float
    r1: float
    d1: float
    d1_tw: float = Field(alias='d1/tw')
    bf_tw__2tf: float = Field(alias='_(bf-tw)/2tf')
    Zy: float
    compact_y: str
    Zey: float

@dataclass
class UB:
    _610UB125: UB_base = field(metadata={'alias': '610UB125'})
    _610UB113: UB_base = field(metadata={'alias': '610UB113'})
    _610UB101: UB_base = field(metadata={'alias': '610UB101'})
    _530UB92: UB_base = field(metadata={'alias': '530UB92'})
    _530UB82: UB_base = field(metadata={'alias': '530UB82'})
    _460UB82: UB_base = field(metadata={'alias': '460UB82'})
    _460UB74: UB_base = field(metadata={'alias': '460UB74'})
    _460UB67: UB_base = field(metadata={'alias': '460UB67'})
    _410UB59: UB_base = field(metadata={'alias': '410UB59'})
    _410UB53: UB_base = field(metadata={'alias': '410UB53'})
    _360UB56: UB_base = field(metadata={'alias': '360UB56'})
    _360UB50: UB_base = field(metadata={'alias': '360UB50'})
    _360UB44: UB_base = field(metadata={'alias': '360UB44'})
    _310UB46: UB_base = field(metadata={'alias': '310UB46'})
    _310UB40: UB_base = field(metadata={'alias': '310UB40'})
    _310UB32: UB_base = field(metadata={'alias': '310UB32'})
    _250UB37: UB_base = field(metadata={'alias': '250UB37'})
    _250UB31: UB_base = field(metadata={'alias': '250UB31'})
    _250UB25: UB_base = field(metadata={'alias': '250UB25'})
    _200UB29: UB_base = field(metadata={'alias': '200UB29'})
    _200UB25: UB_base = field(metadata={'alias': '200UB25'})
    _200UB22: UB_base = field(metadata={'alias': '200UB22'})
    _200UB18: UB_base = field(metadata={'alias': '200UB18'})
    _180UB22: UB_base = field(metadata={'alias': '180UB22'})
    _180UB18: UB_base = field(metadata={'alias': '180UB18'})
    _180UB16: UB_base = field(metadata={'alias': '180UB16'})
    _150UB18: UB_base = field(metadata={'alias': '150UB18'})
    _150UB14: UB_base = field(metadata={'alias': '150UB14'})

    def __iter__(self):
        yield from self.__dict__.values()
