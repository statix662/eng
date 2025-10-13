import csv
import json
import os

def convert_csv_to_nested_json(csv_path, json_path):
    nested_data = {}

    with open(csv_path, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            name_value = row.get('name').strip()
            key_name = '_' + name_value.replace(" ", "")

            cleaned_row = {}
            for key, value in row.items():
                try:
                    cleaned_row[key] = float(value)
                except ValueError:
                    cleaned_row[key] = value  # Keep as string if not a float

            nested_data[key_name] = cleaned_row

    with open(json_path, mode='w', encoding='utf-8') as f:
        json.dump(nested_data, f, indent=4)

    print(f"✅ Converted '{csv_path}' to '{json_path}'")

def find_csv_files_in_directory(directory='.'):
    return [file for file in os.listdir(directory) if file.lower().endswith('.csv')]

if __name__ == "__main__":
    csv_files = find_csv_files_in_directory()
    if not csv_files:
        print("⚠️ No CSV files found in the current directory.")
    else:
        for csv_file in csv_files:
            json_file = os.path.splitext(csv_file)[0] + '.json'
            convert_csv_to_nested_json(csv_file, json_file)

