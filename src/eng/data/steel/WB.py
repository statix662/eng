from pydantic import Field
from dataclasses import dataclass, field
from .model.steel import Steel

class WB_base(Steel):
    tw: float
    r1: str
    d1: float
    d1_tw: float = Field(alias='d1/tw')
    bf_tw__2tf: float = Field(alias='_(bf-tw)/2tf')
    Zy: float
    compact_y: str
    Zey: float

@dataclass
class WB:
    _1200WB455: WB_base = field(metadata={'alias': '1200WB455'})
    _1200WB423: WB_base = field(metadata={'alias': '1200WB423'})
    _1200WB392: WB_base = field(metadata={'alias': '1200WB392'})
    _1200WB342: WB_base = field(metadata={'alias': '1200WB342'})
    _1200WB317: WB_base = field(metadata={'alias': '1200WB317'})
    _1200WB278: WB_base = field(metadata={'alias': '1200WB278'})
    _1200WB249: WB_base = field(metadata={'alias': '1200WB249'})
    _1000WB322: WB_base = field(metadata={'alias': '1000WB322'})
    _1000WB296: WB_base = field(metadata={'alias': '1000WB296'})
    _1000WB258: WB_base = field(metadata={'alias': '1000WB258'})
    _1000WB215: WB_base = field(metadata={'alias': '1000WB215'})
    _900WB282: WB_base = field(metadata={'alias': '900WB282'})
    _900WB257: WB_base = field(metadata={'alias': '900WB257'})
    _900WB218: WB_base = field(metadata={'alias': '900WB218'})
    _900WB175: WB_base = field(metadata={'alias': '900WB175'})
    _800WB192: WB_base = field(metadata={'alias': '800WB192'})
    _800WB168: WB_base = field(metadata={'alias': '800WB168'})
    _800WB146: WB_base = field(metadata={'alias': '800WB146'})
    _800WB122: WB_base = field(metadata={'alias': '800WB122'})
    _700WB173: WB_base = field(metadata={'alias': '700WB173'})
    _700WB150: WB_base = field(metadata={'alias': '700WB150'})
    _700WB130: WB_base = field(metadata={'alias': '700WB130'})
    _700WB115: WB_base = field(metadata={'alias': '700WB115'})

    def __iter__(self):
        yield from self.__dict__.values()
