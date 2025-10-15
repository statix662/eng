import json
from pathlib import Path
from typing import Type
from pydantic import BaseModel

def load_data(
    json_path: Path,
    wrapper_model: Type[BaseModel]
) -> BaseModel:
    """
    Loads data from a JSON file into a Pydantic wrapper model.
    """
    with json_path.open("r", encoding="utf-8") as f:
        raw_data = json.load(f)
    
    return wrapper_model(**raw_data)
