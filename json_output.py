import json

def output_to_json(file_path, data):
    try:
        json_file_path = file_path.replace('.pptx', '.json')

        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file)

        print(f"Output written to {json_file_path}")

    except Exception as e:
        print(f"An error occurred while writing to the JSON file: {e}")
