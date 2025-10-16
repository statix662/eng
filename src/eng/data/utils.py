import json
from pathlib import Path
from typing import Type, Any
from dataclasses import fields, is_dataclass

def load_data(json_path: Path, wrapper_model: Type[Any]) -> Any:
    """
    Loads data from a JSON file into a dataclass wrapper model.

    This function handles dataclass wrappers where fields may use 'alias'
    in their metadata to map to keys in the JSON file. It also assumes
    that the values in the JSON are dictionaries that can be used to
    instantiate the field types (e.g., a Pydantic model).
    """
    with json_path.open("r", encoding="utf-8") as f:
        raw_data = json.load(f)

    if not is_dataclass(wrapper_model):
        try:
            # Fallback for simple pydantic models or other types
            return wrapper_model(**raw_data)
        except TypeError:
             raise TypeError(f"wrapper_model '{wrapper_model.__name__}' is not a dataclass and could not be instantiated.")

    alias_map = {f.metadata['alias']: f.name for f in fields(wrapper_model) if 'alias' in f.metadata}
    
    init_kwargs = {}
    for json_key, json_value in raw_data.items():
        field_name = alias_map.get(json_key, json_key)
        
        # Get the type annotation for the field
        field_type = wrapper_model.__annotations__.get(field_name)
        
        if field_type:
            # Instantiate the field's type (e.g., a Pydantic model) with the value
            init_kwargs[field_name] = field_type(**json_value)
        else:
            # This path is unlikely if models are generated correctly
            # but as a fallback, just pass the value.
            init_kwargs[field_name] = json_value

    return wrapper_model(**init_kwargs)