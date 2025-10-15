from pydantic import BaseModel, Field

class SHS_base(BaseModel):
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


class SHS(BaseModel):
    _250x9SHS: SHS_base
    _250x6SHS: SHS_base
    _200x9SHS: SHS_base
    _200x6SHS: SHS_base
    _200x5SHS: SHS_base
    _150x9SHS: SHS_base
    _150x6SHS: SHS_base
    _150x5SHS: SHS_base
    _125x9SHS: SHS_base
    _125x6SHS: SHS_base
    _125x5SHS: SHS_base
    _125x4SHS: SHS_base
    _100x9SHS: SHS_base
    _100x6SHS: SHS_base
    _100x5SHS: SHS_base
    _100x4SHS: SHS_base
    _100x3SHS: SHS_base
    _100x2_5SHS: SHS_base = Field(alias='_100x2.5SHS')
    _100x2SHS: SHS_base
    _89x6SHS: SHS_base
    _89x5SHS: SHS_base
    _89x3_5SHS: SHS_base = Field(alias='_89x3.5SHS')
    _75x6SHS: SHS_base
    _75x5SHS: SHS_base
    _75x4SHS: SHS_base
    _75x3_5SHS: SHS_base = Field(alias='_75x3.5SHS')
    _75x3SHS: SHS_base
    _75x2_5SHS: SHS_base = Field(alias='_75x2.5SHS')
    _75x2SHS: SHS_base
    _65x6SHS: SHS_base
    _65x5SHS: SHS_base
    _65x4SHS: SHS_base
    _65x3SHS: SHS_base
    _65x2_5SHS: SHS_base = Field(alias='_65x2.5SHS')
    _65x2SHS: SHS_base
    _65x1_6SHS: SHS_base = Field(alias='_65x1.6SHS')
    _50x5SHS: SHS_base
    _50x4SHS: SHS_base
    _50x3SHS: SHS_base
    _50x2_5SHS: SHS_base = Field(alias='_50x2.5SHS')
    _50x2SHS: SHS_base
    _50x1_6SHS: SHS_base = Field(alias='_50x1.6SHS')
    _40x4SHS: SHS_base
    _40x3SHS: SHS_base
    _40x2_5SHS: SHS_base = Field(alias='_40x2.5SHS')
    _40x2SHS: SHS_base
    _40x1_6SHS: SHS_base = Field(alias='_40x1.6SHS')
    _35x3SHS: SHS_base
    _35x2_5SHS: SHS_base = Field(alias='_35x2.5SHS')
    _35x2SHS: SHS_base
    _35x1_6SHS: SHS_base = Field(alias='_35x1.6SHS')
    _30x2SHS: SHS_base
    _30x1_6SHS: SHS_base = Field(alias='_30x1.6SHS')
    _25x3SHS: SHS_base
    _25x2_5SHS: SHS_base = Field(alias='_25x2.5SHS')
    _25x2SHS: SHS_base
    _25x1_6SHS: SHS_base = Field(alias='_25x1.6SHS')
    _20x1_6SHS: SHS_base = Field(alias='_20x1.6SHS')
 
    def __iter__(self):
        yield from self.__dict__.values()

