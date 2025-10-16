from pydantic import Field
from dataclasses import dataclass, field
from .model.steel import Steel

class WC_base(Steel):
    tw: float
    r1: str
    d1: float
    d1_tw: float = Field(alias='d1/tw')
    bf_tw__2tf: float = Field(alias='_(bf-tw)/2tf')
    Zy: float
    compact_y: str
    Zey: float

@dataclass
class WC:
    _500WC440: WC_base = field(metadata={'alias': '500WC440'})
    _500WC414: WC_base = field(metadata={'alias': '500WC414'})
    _500WC383: WC_base = field(metadata={'alias': '500WC383'})
    _500WC340: WC_base = field(metadata={'alias': '500WC340'})
    _500WC290: WC_base = field(metadata={'alias': '500WC290'})
    _500WC267: WC_base = field(metadata={'alias': '500WC267'})
    _500WC228: WC_base = field(metadata={'alias': '500WC228'})
    _400WC361: WC_base = field(metadata={'alias': '400WC361'})
    _400WC328: WC_base = field(metadata={'alias': '400WC328'})
    _400WC303: WC_base = field(metadata={'alias': '400WC303'})
    _400WC270: WC_base = field(metadata={'alias': '400WC270'})
    _400WC212: WC_base = field(metadata={'alias': '400WC212'})
    _400WC181: WC_base = field(metadata={'alias': '400WC181'})
    _400WC144: WC_base = field(metadata={'alias': '400WC144'})
    _350WC280: WC_base = field(metadata={'alias': '350WC280'})
    _350WC258: WC_base = field(metadata={'alias': '350WC258'})
    _350WC230: WC_base = field(metadata={'alias': '350WC230'})
    _350WC197: WC_base = field(metadata={'alias': '350WC197'})

    def __iter__(self):
        yield from self.__dict__.values()
