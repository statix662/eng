from pydantic import BaseModel, Field

class UB_base(BaseModel):
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


class UB(BaseModel):
    _610UB125: UB_base
    _610UB113: UB_base
    _610UB101: UB_base
    _530UB92: UB_base
    _530UB82: UB_base
    _460UB82: UB_base
    _460UB74: UB_base
    _460UB67: UB_base
    _410UB59: UB_base
    _410UB53: UB_base
    _360UB56: UB_base
    _360UB50: UB_base
    _360UB44: UB_base
    _310UB46: UB_base
    _310UB40: UB_base
    _310UB32: UB_base
    _250UB37: UB_base
    _250UB31: UB_base
    _250UB25: UB_base
    _200UB29: UB_base
    _200UB25: UB_base
    _200UB22: UB_base
    _200UB18: UB_base
    _180UB22: UB_base
    _180UB18: UB_base
    _180UB16: UB_base
    _150UB18: UB_base
    _150UB14: UB_base
 
    def __iter__(self):
        yield from self.__dict__.values()

