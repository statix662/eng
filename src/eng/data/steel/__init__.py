from pathlib import Path
from ..utils import load_data

from .CHS import CHS as CHS_wrapper
from .PFC import PFC as PFC_wrapper
from .SHS import SHS as SHS_wrapper
from .UB import UB as UB_wrapper
from .UC import UC as UC_wrapper
from .WB import WB as WB_wrapper
from .WC import WC as WC_wrapper

_data_path = Path(__file__).parent / "data"

CHS: CHS_wrapper = load_data(_data_path / "CHS.json", CHS_wrapper)
PFC: PFC_wrapper = load_data(_data_path / "PFC.json", PFC_wrapper)
SHS: SHS_wrapper = load_data(_data_path / "SHS.json", SHS_wrapper)
UB: UB_wrapper = load_data(_data_path / "UB.json", UB_wrapper)
UC: UC_wrapper = load_data(_data_path / "UC.json", UC_wrapper)
WB: WB_wrapper = load_data(_data_path / "WB.json", WB_wrapper)
WC: WC_wrapper = load_data(_data_path / "WC.json", WC_wrapper)

__all__ = ['CHS', 'PFC', 'SHS', 'UB', 'UC', 'WB', 'WC']