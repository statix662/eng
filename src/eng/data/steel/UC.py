from pydantic import BaseModel, Field

class UC_base(BaseModel):
    name: str
    weight: float
    d: float
    bf: float
    tf: float
    tw: float
    r1: float
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


class UC(BaseModel):
    _310UC158: UC_base
    _310UC137: UC_base
    _310UC118: UC_base
    _310UC96: UC_base
    _250UC89: UC_base
    _250UC72: UC_base
    _200UC59: UC_base
    _200UC52: UC_base
    _200UC46: UC_base
    _150UC37: UC_base
    _150UC30: UC_base
    _150UC23: UC_base
    _100UC14: UC_base
 
    def __iter__(self):
        yield from self.__dict__.values()

