import json
from pathlib import Path
from typing import Type
from pydantic import BaseModel


def load_data(json_path: Path, wrapper_model: Type[BaseModel]) -> BaseModel:
    """
    Loads data from a JSON file into a Pydantic wrapper model.
    """
    with json_path.open("r", encoding="utf-8") as f:
        raw_data = json.load(f)

    return wrapper_model(**raw_data)


### OLD VERSION ###
# def load_data(
#     json_path: Path, entry_model: Type[BaseModel], wrapper_model: Type[BaseModel]
# ) -> BaseModel:
#     """
#     Load JSON data into a statically defined Pydantic wrapper model.
#
#     Args:
#         json_path (Path): Path to the JSON file.
#         entry_model (Type[BaseModel]): Model for individual entries.
#         wrapper_model (Type[BaseModel]): Wrapper model with named fields.
#
#     Returns:
#         BaseModel: An instance of the wrapper model populated with entry models.
#     """
#     with json_path.open("r", encoding="utf-8") as f:
#         raw_data = json.load(f)
#
#     # Validate each entry using the entry model
#     validated_data = {key: entry_model(**value) for key, value in raw_data.items()}
#
#     # Instantiate the wrapper model with validated entries
#     return wrapper_model(**validated_data)
