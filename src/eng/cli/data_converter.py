import csv
import json
import os
import re
from collections import OrderedDict
from pathlib import Path

# --- Utility Functions ---

def try_convert_to_float(value):
    """Tries to convert a value to a float, otherwise returns it as is."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return value

def infer_type(value):
    """Infers if a value should be a float or a string."""
    if isinstance(try_convert_to_float(value), float):
        return "float"
    return "str"

def sanitize_name(name):
    """Sanitizes a string to be a valid Python attribute name."""
    sanitized = re.sub(r'\W', '_', name)
    sanitized = sanitized.lstrip('_')
    if not sanitized:
        return '_'
    if sanitized and sanitized[0].isdigit():
        sanitized = '_' + sanitized
    return sanitized

# --- Data Loading and Structuring ---

def load_csv_data(csv_path):
    """Loads data from a CSV file into a list of dictionaries."""
    if not os.path.exists(csv_path):
        print(f"⚠️  CSV file not found at '{csv_path}'")
        return []
    with open(csv_path, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        return [row for row in reader if row.get('name', '').strip()]

def create_nested_dictionary(data):
    """Structures a list of dictionaries into a nested dictionary."""
    nested_data = {}
    for row in data:
        name_value = row.get('name').strip()
        nested_data[name_value] = {key: try_convert_to_float(value) for key, value in row.items()}
    return nested_data

def write_json_file(data, json_path):
    """Writes a dictionary to a JSON file."""
    with open(json_path, mode='w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print(f"  ✅ Created JSON file: '{os.path.basename(json_path)}'")

# --- Model Generation ---

def get_csv_headers(csv_path):
    """Reads the header from a CSV file, handling duplicates."""
    with open(csv_path, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        try:
            headers = next(reader)
            return list(OrderedDict.fromkeys(h.strip() for h in headers if h.strip()))
        except StopIteration:
            return []

def generate_base_model(data_module_path, module_name, csv_files):
    """Generates and writes a base Pydantic model from common fields."""
    raw_data_path = os.path.join(data_module_path, "data", "raw")
    
    header_sets = [set(get_csv_headers(os.path.join(raw_data_path, f))) for f in csv_files]
    if not header_sets:
        return None, set()

    common_headers = set.intersection(*header_sets)
    
    model_dir = os.path.join(data_module_path, "model")
    os.makedirs(model_dir, exist_ok=True)
    with open(os.path.join(model_dir, "__init__.py"), "w") as f:
        pass

    base_model_name = module_name.capitalize()
    base_model_fields_code = []
    
    first_csv_path = os.path.join(raw_data_path, csv_files[0])
    with open(first_csv_path, 'r', newline='', encoding='utf-8') as f:
        first_row = next(csv.DictReader(f), {})

    common_sanitized_fields = set()
    for field in sorted(list(common_headers)):
        type_hint = infer_type(first_row.get(field))
        sanitized = sanitize_name(field)
        common_sanitized_fields.add(sanitized)
        if sanitized == field:
            base_model_fields_code.append(f"    {field}: {type_hint}")
        else:
            base_model_fields_code.append(f"    {sanitized}: {type_hint} = Field(alias='{field}')")

    base_model_code = f"from pydantic import BaseModel, Field\n\n\nclass {base_model_name}(BaseModel):\n"
    base_model_code += "\n".join(base_model_fields_code) if base_model_fields_code else "    pass"

    base_model_file_path = os.path.join(model_dir, f"{module_name}.py")
    write_model_file(base_model_code, base_model_file_path, is_base_model=True)
    
    return base_model_name, common_sanitized_fields

def generate_section_model_code(csv_path, json_data, module_name, base_model_name, common_fields):
    """Generates code for a section-specific model and its wrapper."""
    model_name_upper = os.path.splitext(os.path.basename(csv_path))[0].upper()
    datapoint_model_name = f'{model_name_upper}_base'
    wrapper_model_name = model_name_upper

    with open(csv_path, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        field_names = list(OrderedDict.fromkeys(reader.fieldnames))
        first_row = next(reader, {})

    pydantic_fields = []
    for field in field_names:
        if not field: continue
        sanitized = sanitize_name(field)
        if sanitized in common_fields:
            continue
        
        type_hint = infer_type(first_row.get(field))
        if sanitized == field:
            pydantic_fields.append(f"    {field}: {type_hint}")
        else:
            pydantic_fields.append(f"    {sanitized}: {type_hint} = Field(alias='{field}')")

    imports = f"from pydantic import Field\nfrom dataclasses import dataclass, field\nfrom .model.{module_name} import {base_model_name}\n"
    inheritance = f"({base_model_name})"

    pydantic_model_code = f"""{imports}
class {datapoint_model_name}{inheritance}:
{chr(10).join(pydantic_fields) if pydantic_fields else '    pass'}
"""

    wrapper_fields = []
    for key in json_data.keys():
        sanitized_key = sanitize_name(key)
        if sanitized_key == key:
            wrapper_fields.append(f"    {key}: {datapoint_model_name}")
        else:
            wrapper_fields.append(f"    {sanitized_key}: {datapoint_model_name} = field(metadata={{'alias': '{key}'}})")
    
    iter_method = """\n    def __iter__(self):
        yield from self.__dict__.values()"""

    wrapper_model_code = f"""\n@dataclass
class {wrapper_model_name}:
{chr(10).join(wrapper_fields)}
{iter_method}
"""
    
    return pydantic_model_code + wrapper_model_code

def write_model_file(code, output_path, is_base_model=False):
    """Writes the generated model code to a Python file."""
    with open(output_path, mode="w", encoding="utf-8") as py_file:
        py_file.write(code)
    
    if is_base_model:
        print(f"  ✅ Generated base model: {os.path.basename(output_path)}")
    else:
        print(f"  ✅ Generated section model: {os.path.basename(output_path)}")

def generate_module_init(module_path, section_names):
    """Generates the __init__.py file for a data module with explicit imports."""
    init_path = os.path.join(module_path, "__init__.py")
    
    sorted_names = sorted(section_names)
    
    lines = [
        "from pathlib import Path",
        "from ..utils import load_data",
        ""
    ]
    
    for name in sorted_names:
        lines.append(f"from .{name} import {name} as {name}_wrapper")
    
    lines.append("\n_data_path = Path(__file__).parent / \"data\"\n")
    
    for name in sorted_names:
        lines.append(f"{name} = load_data(_data_path / \"{name}.json\", {name}_wrapper)")
        
    lines.append(f"\n__all__ = {repr(sorted_names)}")

    with open(init_path, "w") as f:
        f.write("\n".join(lines))
    
    print(f"  ✅ Generated __init__.py for module.")

# --- Main Execution ---

def process_module(data_module_path):
    """Processes a single data module end-to-end."""
    module_name = os.path.basename(data_module_path)
    print(f"--- Processing data module: {module_name} ---")

    raw_data_path = os.path.join(data_module_path, "data", "raw")
    json_output_path = os.path.join(data_module_path, "data")
    model_output_path = data_module_path

    if not os.path.isdir(raw_data_path):
        print(f"⚠️  Skipping '{module_name}': 'data/raw' directory not found.")
        return

    csv_files = [f for f in os.listdir(raw_data_path) if f.lower().endswith('.csv')]
    if not csv_files:
        print(f"⚠️  Skipping '{module_name}': No CSV files found in 'data/raw'.")
        return

    base_model_name, common_fields = generate_base_model(data_module_path, module_name, csv_files)
    if not base_model_name:
        print(f"⚠️  Skipping model generation for '{module_name}': Could not determine common fields.")
        return

    section_module_names = []
    for csv_file in csv_files:
        print(f"  Processing '{csv_file}'...")
        csv_file_path = os.path.join(raw_data_path, csv_file)
        
        csv_data = load_csv_data(csv_file_path)
        if not csv_data:
            print(f"  - Skipping '{csv_file}': empty or missing 'name' column.")
            continue

        nested_dict = create_nested_dictionary(csv_data)
        json_file_name = os.path.splitext(csv_file)[0] + '.json'
        json_file_path = os.path.join(json_output_path, json_file_name)
        write_json_file(nested_dict, json_file_path)

        model_code = generate_section_model_code(csv_file_path, nested_dict, module_name, base_model_name, common_fields)
        
        if model_code:
            section_name = os.path.splitext(csv_file)[0].upper()
            section_module_names.append(section_name)
            model_filename = f"{section_name}.py"
            model_file_path = os.path.join(model_output_path, model_filename)
            write_model_file(model_code, model_file_path)
        else:
            print(f"  - ⚠️  Could not generate model for '{csv_file}'")

    if section_module_names:
        generate_module_init(data_module_path, section_module_names)

def main():
    """
    Finds all data modules and processes them to refresh JSON and model files.
    This script can be run via the 'refresh-data' command.
    """
    print("--- Starting data refresh process ---")
    script_path = os.path.dirname(os.path.abspath(__file__))
    data_root_path = os.path.abspath(os.path.join(script_path, '..', 'data'))

    if not os.path.isdir(data_root_path):
        print(f"❌ Critical Error: Data root directory not found at '{data_root_path}'")
        return

    for module_name in sorted(os.listdir(data_root_path)):
        module_path = os.path.join(data_root_path, module_name)
        if os.path.isdir(module_path) and not module_name.startswith('__'):
            process_module(module_path)
    
    print("--- Data refresh process finished ---")

if __name__ == "__main__":
    main()