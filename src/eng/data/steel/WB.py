from pydantic import BaseModel, Field

class WB_base(BaseModel):
    name: str
    weight: float
    d: float
    bf: float
    tf: float
    tw: float
    r1: str
    d1: float
    d1_tw: float = Field(alias='d1/tw')
    bf_tw__2tf: float = Field(alias='_(bf-tw)/2tf')
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


class WB(BaseModel):
    _1200WB455: WB_base
    _1200WB423: WB_base
    _1200WB392: WB_base
    _1200WB342: WB_base
    _1200WB317: WB_base
    _1200WB278: WB_base
    _1200WB249: WB_base
    _1000WB322: WB_base
    _1000WB296: WB_base
    _1000WB258: WB_base
    _1000WB215: WB_base
    _900WB282: WB_base
    _900WB257: WB_base
    _900WB218: WB_base
    _900WB175: WB_base
    _800WB192: WB_base
    _800WB168: WB_base
    _800WB146: WB_base
    _800WB122: WB_base
    _700WB173: WB_base
    _700WB150: WB_base
    _700WB130: WB_base
    _700WB115: WB_base
 
    def __iter__(self):
        yield from self.__dict__.values()

