from pydantic import BaseModel, Field

class WC_base(BaseModel):
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


class WC(BaseModel):
    _500WC440: WC_base
    _500WC414: WC_base
    _500WC383: WC_base
    _500WC340: WC_base
    _500WC290: WC_base
    _500WC267: WC_base
    _500WC228: WC_base
    _400WC361: WC_base
    _400WC328: WC_base
    _400WC303: WC_base
    _400WC270: WC_base
    _400WC212: WC_base
    _400WC181: WC_base
    _400WC144: WC_base
    _350WC280: WC_base
    _350WC258: WC_base
    _350WC230: WC_base
    _350WC197: WC_base
 
    def __iter__(self):
        yield from self.__dict__.values()

