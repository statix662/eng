
import csv
import json
import os
import argparse

def try_convert_to_float(value):

    try:

        return float(value)

    except (ValueError, TypeError):

        return value





def convert_csv_to_nested_json(csv_path, json_path):

    nested_data = {}



    with open(csv_path, mode='r', newline='', encoding='utf-8') as f:

        reader = csv.DictReader(f)

        for row in reader:

            name_value = row.get('name').strip()

            key_name = name_value.replace(" ", "")

            if name_value and name_value[0].isdigit():

                key_name = '_' + key_name



            cleaned_row = {

                key: try_convert_to_float(value) for key, value in row.items()

            }



            nested_data[key_name] = cleaned_row



    with open(json_path, mode='w', encoding='utf-8') as f:

        json.dump(nested_data, f, indent=4)



    print(f"✅ Converted '{csv_path}' to '{json_path}'")


def infer_type(value):
    if isinstance(try_convert_to_float(value), float):
        return "float"
    return "str"


def sanitize_field_name(name):
    import re
    sanitized = re.sub(r'\W', '_', name)
    sanitized = sanitized.lstrip('_')
    if not sanitized:
        return '_'
    if sanitized and sanitized[0].isdigit():
        sanitized = '_' + sanitized
    return sanitized

def generate_pydantic_model(csv_file, output_dir, json_file_path):
    from collections import OrderedDict
    model_name_upper = os.path.splitext(os.path.basename(csv_file))[0].upper()
    py_filename = model_name_upper + ".py"

    base_model_name = f'{model_name_upper}_base'
    wrapper_model_name = model_name_upper

    with open(csv_file, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        field_names = list(OrderedDict.fromkeys(reader.fieldnames))
        try:
            first_row = next(reader, None)
        except StopIteration:
            first_row = None

    if not field_names or not first_row or "name" not in field_names:
        print(f"⚠️ Skipping '{csv_file}' — missing 'name' column or empty file.")
        return

    fields = []
    for field in field_names:
        if not field: continue
        sanitized = sanitize_field_name(field)
        type_hint = infer_type(first_row[field])
        if sanitized == field:
            fields.append(f"    {field}: {type_hint}")
        else:
            fields.append(f"    {sanitized}: {type_hint} = Field(alias='{field}')")

    model_code = f"""from pydantic import BaseModel, Field

class {base_model_name}(BaseModel):
{chr(10).join(fields)}
"""

    # Generate wrapper model
    with open(json_file_path, 'r') as f:
        json_data = json.load(f)

    wrapper_fields = []
    for key in json_data.keys():
        sanitized_key = sanitize_field_name(key)
        if sanitized_key == key:
            wrapper_fields.append(f"    {key}: {base_model_name}")
        else:
            wrapper_fields.append(f"    {sanitized_key}: {base_model_name} = Field(alias='{key}')")
    
    iter_method = """ 
    def __iter__(self):
        yield from self.__dict__.values()
"""

    wrapper_model_code = f"""
class {wrapper_model_name}(BaseModel):
{chr(10).join(wrapper_fields)}
{iter_method}
"""

    model_code += "\n" + wrapper_model_code

    output_path = os.path.join(output_dir, py_filename)
    with open(output_path, mode="w", encoding="utf-8") as py_file:
        py_file.write(model_code)

    print(f"✅ Generated model: {py_filename}")

def main():
    parser = argparse.ArgumentParser(description="Convert CSV data to JSON and generate Pydantic models.")
    parser.add_argument("data_module_path", help="The path to the data module (e.g., src/eng/data/steel)")
    args = parser.parse_args()

    data_module_path = args.data_module_path
    raw_data_path = os.path.join(data_module_path, "data", "raw")
    json_output_path = os.path.join(data_module_path, "data")
    model_output_path = data_module_path

    if not os.path.isdir(raw_data_path):
        print(f"⚠️ Raw data directory not found at '{raw_data_path}'")
        return

    csv_files = [file for file in os.listdir(raw_data_path) if file.lower().endswith('.csv')]

    if not csv_files:
        print(f"⚠️ No CSV files found in '{raw_data_path}'")
    else:
        for csv_file in csv_files:
            csv_file_path = os.path.join(raw_data_path, csv_file)
            json_file_name = os.path.splitext(csv_file)[0] + '.json'
            json_file_path = os.path.join(json_output_path, json_file_name)

            convert_csv_to_nested_json(csv_file_path, json_file_path)
            generate_pydantic_model(csv_file_path, model_output_path, json_file_path)

if __name__ == "__main__":
    main()
