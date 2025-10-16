from pydantic import BaseModel, Field


class Steel(BaseModel):
    Ag: float
    Iw: float
    Ix: float
    Iy: float
    J: float
    Sx: float
    Sy: float
    Zex: float
    Zx: float
    bf: float
    compact_x: str
    d: float
    fy: float
    kf: float
    name: str
    rx: float
    ry: float
    tf: float
    weight: float