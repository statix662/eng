from pydantic import BaseModel, Field

class PFC_base(BaseModel):
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
    Sy: float
    ry: float
    J: float
    Iw: float
    fy: float
    kf: float
    compact_x: str
    Zex: float


class PFC(BaseModel):
    _380PFC: PFC_base
    _300PFC: PFC_base
    _250PFC: PFC_base
    _230PFC: PFC_base
    _200PFC: PFC_base
    _180PFC: PFC_base
    _150PFC: PFC_base
    _125PFC: PFC_base
    _100PFC: PFC_base
    _75PFC: PFC_base
 
    def __iter__(self):
        yield from self.__dict__.values()

