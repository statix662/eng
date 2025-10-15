from pydantic import BaseModel, Field

class CHS_base(BaseModel):
    name: str
    weight: float
    d: float
    bf: float
    tf: float
    Ag: float
    Ix: float
    Zx: float
    Sx: float
    rx: float
    Iy: float
    Zy: float
    Sy: float
    ry: float
    J: float
    Iw: float
    fy: float
    kf: float
    compact_x: str
    Zex: float
    compact_y: str
    Zey: float


class CHS(BaseModel):
    _457_0x12_7CHS: CHS_base = Field(alias='_457.0x12.7CHS')
    _457_0x9_5CHS: CHS_base = Field(alias='_457.0x9.5CHS')
    _457_0x6_4CHS: CHS_base = Field(alias='_457.0x6.4CHS')
    _406_4x12_7CHS: CHS_base = Field(alias='_406.4x12.7CHS')
    _406_4x9_5CHS: CHS_base = Field(alias='_406.4x9.5CHS')
    _406_4x6_4CHS: CHS_base = Field(alias='_406.4x6.4CHS')
    _355_6x12_7CHS: CHS_base = Field(alias='_355.6x12.7CHS')
    _355_6x9_5CHS: CHS_base = Field(alias='_355.6x9.5CHS')
    _355_6x6_4CHS: CHS_base = Field(alias='_355.6x6.4CHS')
    _323_9x12_7CHS: CHS_base = Field(alias='_323.9x12.7CHS')
    _323_9x9_5CHS: CHS_base = Field(alias='_323.9x9.5CHS')
    _323_9x6_4CHS: CHS_base = Field(alias='_323.9x6.4CHS')
    _273_1x12_7CHS: CHS_base = Field(alias='_273.1x12.7CHS')
    _273_1x9_3CHS: CHS_base = Field(alias='_273.1x9.3CHS')
    _273_1x6_4CHS: CHS_base = Field(alias='_273.1x6.4CHS')
    _273_1x4_8CHS: CHS_base = Field(alias='_273.1x4.8CHS')
    _219_1x8_2CHS: CHS_base = Field(alias='_219.1x8.2CHS')
    _219_1x6_4CHS: CHS_base = Field(alias='_219.1x6.4CHS')
    _219_1x4_8CHS: CHS_base = Field(alias='_219.1x4.8CHS')
    _168_3x7_1CHS: CHS_base = Field(alias='_168.3x7.1CHS')
    _168_3x6_4CHS: CHS_base = Field(alias='_168.3x6.4CHS')
    _168_3x4_8CHS: CHS_base = Field(alias='_168.3x4.8CHS')
    _165_1x3_5CHS: CHS_base = Field(alias='_165.1x3.5CHS')
    _139_7x3_5CHS: CHS_base = Field(alias='_139.7x3.5CHS')
    _139_7x3_0CHS: CHS_base = Field(alias='_139.7x3.0CHS')
    _114_3x3_6CHS: CHS_base = Field(alias='_114.3x3.6CHS')
    _114_3x3_2CHS: CHS_base = Field(alias='_114.3x3.2CHS')
    _101_6x3_2CHS: CHS_base = Field(alias='_101.6x3.2CHS')
    _101_6x2_6CHS: CHS_base = Field(alias='_101.6x2.6CHS')
    _88_9x3_2CHS: CHS_base = Field(alias='_88.9x3.2CHS')
    _88_9x2_6CHS: CHS_base = Field(alias='_88.9x2.6CHS')
    _76_1x3_2CHS: CHS_base = Field(alias='_76.1x3.2CHS')
    _76_1x2_3CHS: CHS_base = Field(alias='_76.1x2.3CHS')
    _60_3x2_9CHS: CHS_base = Field(alias='_60.3x2.9CHS')
    _60_3x2_3CHS: CHS_base = Field(alias='_60.3x2.3CHS')
    _48_3x2_9CHS: CHS_base = Field(alias='_48.3x2.9CHS')
    _48_3x2_3CHS: CHS_base = Field(alias='_48.3x2.3CHS')
    _42_4x2_6CHS: CHS_base = Field(alias='_42.4x2.6CHS')
    _42_4x2_0CHS: CHS_base = Field(alias='_42.4x2.0CHS')
    _33_7x2_6CHS: CHS_base = Field(alias='_33.7x2.6CHS')
    _33_7x2_0CHS: CHS_base = Field(alias='_33.7x2.0CHS')
    _26_9x2_3CHS: CHS_base = Field(alias='_26.9x2.3CHS')
    _26_9x2_0CHS: CHS_base = Field(alias='_26.9x2.0CHS')
 
    def __iter__(self):
        yield from self.__dict__.values()

