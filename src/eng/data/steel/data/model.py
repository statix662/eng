import os
import csv


def infer_type(value):
    try:
        float(value)
        return "float"
    except ValueError:
        return "str"


def generate_pydantic_model(csv_file, output_dir="."):
    model_name = os.path.splitext(os.path.basename(csv_file))[0].capitalize() + "Model"
    py_filename = os.path.splitext(os.path.basename(csv_file))[0] + ".py"

    with open(csv_file, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        field_names = reader.fieldnames
        first_row = next(reader, None)

    if not field_names or not first_row or "Designation" not in field_names:
        print(f"⚠️ Skipping '{csv_file}' — missing 'Designation' column or empty file.")
        return

    # Infer types from first row
    fields = []
    for field in field_names:
        if field == "Designation":
            fields.append(f"    {field}: str")
        else:
            inferred_type = infer_type(first_row[field])
            fields.append(f"    {field}: {inferred_type}")

    # Create model code
    model_code = f"""from pydantic import BaseModel

class {model_name}(BaseModel):
{chr(10).join(fields)}
"""

    # Write to .py file
    output_path = os.path.join(output_dir, py_filename)
    with open(output_path, mode="w", encoding="utf-8") as py_file:
        py_file.write(model_code)

    print(f"✅ Generated model: {py_filename}")


def find_csv_files_in_directory(directory="."):
    return [file for file in os.listdir(directory) if file.lower().endswith(".csv")]


if __name__ == "__main__":
    csv_files = find_csv_files_in_directory()
    if not csv_files:
        print("⚠️ No CSV files found in the current directory.")
    else:
        for csv_file in csv_files:
            generate_pydantic_model(csv_file)
