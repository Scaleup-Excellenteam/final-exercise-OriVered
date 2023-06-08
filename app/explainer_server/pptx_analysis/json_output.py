import json
import os


def output_to_json(file_name,output_path, data):
    try:
        file_name = os.path.basename(file_name) # Extract only the file name without the path
        json_file_name = file_name.replace('.pptx', '.json') # Replace the file suffix
        json_file_path = os.path.join(output_path, json_file_name)  # Connect output_path with the new file name

        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file)

        print(f"Output written to {json_file_path}")

    except Exception as e:
        print(f"An error occurred while writing to the JSON file: {e}")
