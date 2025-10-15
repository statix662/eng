import importlib
from pathlib import Path
from eng.data.utils import load_data

steel_path = Path(__file__).parent
# Find all python files (models) in this directory that are all uppercase
model_files = [f for f in steel_path.glob('*.py') if f.name != '__init__.py' and f.stem == f.stem.upper()]
__all__ = []

for model_file in model_files:
    model_name_upper = model_file.stem
    
    try:
        module = importlib.import_module(f'.{model_name_upper}', __package__)
        wrapper_model_class = getattr(module, model_name_upper)
    except (ImportError, AttributeError) as e:
        print(f"Could not load wrapper model for {model_name_upper}: {e}")
        continue

    json_path = steel_path / 'data' / f'{model_name_upper}.json'
    
    if json_path.exists():
        var_name = model_name_upper
        try:
            data_wrapper_object = load_data(json_path, wrapper_model_class)
            globals()[var_name] = data_wrapper_object
            __all__.append(var_name)
        except Exception as e:
            print(f"Could not load data for {model_name_upper}: {e}")