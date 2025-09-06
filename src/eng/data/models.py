from pydantic import BaseModel 

class SteelSection(BaseModel):
    name: str
    weight: float
    Ix: float
    #TODO: Add other properties
