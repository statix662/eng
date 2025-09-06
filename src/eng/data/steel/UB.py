from pydantic import BaseModel
from pathlib import Path
from eng.data.utils import load_data
from eng.data.modela import SteelSection

from .data.models import SteelSection
from .data.utils import load_data

json_path = Path(__file__).parent / "data" / "UB.json"

class UBSections(BaseModel):
    _250UB25: SteelSection
    _310UB32: SteelSection

    
UB = load_data(json_path, SteelSection, UBSections)
