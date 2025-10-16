from pydantic import Field
from dataclasses import dataclass, field
from .model.steel import Steel

class CHS_base(Steel):
    Zy: float
    compact_y: str
    Zey: float

@dataclass
class CHS:
    _457_0x12_7_CHS: CHS_base = field(metadata={'alias': '457.0x12.7 CHS'})
    _457_0x9_5_CHS: CHS_base = field(metadata={'alias': '457.0x9.5 CHS'})
    _457_0x6_4_CHS: CHS_base = field(metadata={'alias': '457.0x6.4 CHS'})
    _406_4x12_7_CHS: CHS_base = field(metadata={'alias': '406.4x12.7 CHS'})
    _406_4x9_5_CHS: CHS_base = field(metadata={'alias': '406.4x9.5 CHS'})
    _406_4x_6_4_CHS: CHS_base = field(metadata={'alias': '406.4x 6.4 CHS'})
    _355_6x12_7_CHS: CHS_base = field(metadata={'alias': '355.6x12.7 CHS'})
    _355_6x_9_5_CHS: CHS_base = field(metadata={'alias': '355.6x 9.5 CHS'})
    _355_6x6_4_CHS: CHS_base = field(metadata={'alias': '355.6x6.4 CHS'})
    _323_9x12_7_CHS: CHS_base = field(metadata={'alias': '323.9x12.7 CHS'})
    _323_9x9_5_CHS: CHS_base = field(metadata={'alias': '323.9x9.5 CHS'})
    _323_9x6_4_CHS: CHS_base = field(metadata={'alias': '323.9x6.4 CHS'})
    _273_1x12_7_CHS: CHS_base = field(metadata={'alias': '273.1x12.7 CHS'})
    _273_1x9_3_CHS: CHS_base = field(metadata={'alias': '273.1x9.3 CHS'})
    _273_1x6_4_CHS: CHS_base = field(metadata={'alias': '273.1x6.4 CHS'})
    _273_1x4_8_CHS: CHS_base = field(metadata={'alias': '273.1x4.8 CHS'})
    _219_1x8_2_CHS: CHS_base = field(metadata={'alias': '219.1x8.2 CHS'})
    _219_1x6_4_CHS: CHS_base = field(metadata={'alias': '219.1x6.4 CHS'})
    _219_1x4_8_CHS: CHS_base = field(metadata={'alias': '219.1x4.8 CHS'})
    _168_3x7_1_CHS: CHS_base = field(metadata={'alias': '168.3x7.1 CHS'})
    _168_3x6_4_CHS: CHS_base = field(metadata={'alias': '168.3x6.4 CHS'})
    _168_3x4_8_CHS: CHS_base = field(metadata={'alias': '168.3x4.8 CHS'})
    _165_1x3_5_CHS: CHS_base = field(metadata={'alias': '165.1x3.5 CHS'})
    _139_7x3_5_CHS: CHS_base = field(metadata={'alias': '139.7x3.5 CHS'})
    _139_7x3_0_CHS: CHS_base = field(metadata={'alias': '139.7x3.0 CHS'})
    _114_3x3_6_CHS: CHS_base = field(metadata={'alias': '114.3x3.6 CHS'})
    _114_3x3_2_CHS: CHS_base = field(metadata={'alias': '114.3x3.2 CHS'})
    _101_6x3_2_CHS: CHS_base = field(metadata={'alias': '101.6x3.2 CHS'})
    _101_6x2_6_CHS: CHS_base = field(metadata={'alias': '101.6x2.6 CHS'})
    _88_9x3_2_CHS: CHS_base = field(metadata={'alias': '88.9x3.2 CHS'})
    _88_9x2_6_CHS: CHS_base = field(metadata={'alias': '88.9x2.6 CHS'})
    _76_1x3_2_CHS: CHS_base = field(metadata={'alias': '76.1x3.2 CHS'})
    _76_1x2_3_CHS: CHS_base = field(metadata={'alias': '76.1x2.3 CHS'})
    _60_3x2_9_CHS: CHS_base = field(metadata={'alias': '60.3x2.9 CHS'})
    _60_3x2_3_CHS: CHS_base = field(metadata={'alias': '60.3x2.3 CHS'})
    _48_3x2_9_CHS: CHS_base = field(metadata={'alias': '48.3x2.9 CHS'})
    _48_3x2_3_CHS: CHS_base = field(metadata={'alias': '48.3x2.3 CHS'})
    _42_4x2_6_CHS: CHS_base = field(metadata={'alias': '42.4x2.6 CHS'})
    _42_4x2_0_CHS: CHS_base = field(metadata={'alias': '42.4x2.0 CHS'})
    _33_7x2_6_CHS: CHS_base = field(metadata={'alias': '33.7x2.6 CHS'})
    _33_7x2_0_CHS: CHS_base = field(metadata={'alias': '33.7x2.0 CHS'})
    _26_9x2_3_CHS: CHS_base = field(metadata={'alias': '26.9x2.3 CHS'})
    _26_9x2_0_CHS: CHS_base = field(metadata={'alias': '26.9x2.0 CHS'})

    def __iter__(self):
        yield from self.__dict__.values()
