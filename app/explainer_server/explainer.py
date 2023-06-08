import os
import time
import subprocess

# File path
CURRENT_DIR = os.getcwd()
UPLOAD_FOLDER = os.path.abspath(os.path.join(CURRENT_DIR,'app', 'uploads'))
OUTPUT_FOLDER = os.path.abspath(os.path.join(CURRENT_DIR,'app', 'outputs'))
SCRIPT_PATH = os.path.abspath(os.path.join(CURRENT_DIR, 'app', 'explainer_server', 'pptx_analysis', 'pptx_gpt_analysis.py'))

def get_processed_files():
    """Get a list of UIDs of the files that have been processed."""
    files = os.listdir(OUTPUT_FOLDER)
    # Remove the .json extension
    return [os.path.splitext(file)[0] for file in files]

def get_unprocessed_files(processed_files):
    """Get a list of UIDs of the files that have not yet been processed."""
    files = os.listdir(UPLOAD_FOLDER)
    # Remove the .pptx extension and check if the file has been processed
    return [file for file in files if os.path.splitext(file)[0] not in processed_files]

def explainer():
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    while True:
        processed_files = get_processed_files()
        unprocessed_files = get_unprocessed_files(processed_files)

        for file in unprocessed_files:
            print(f"Processing file: {file}")
            try:
                subprocess.run(['python', SCRIPT_PATH, os.path.join(UPLOAD_FOLDER, file), OUTPUT_FOLDER], check=True)
                print(f"Finished processing file: {file}")
            except subprocess.CalledProcessError as e:
                print(f"An error occurred while processing the file: {e}")

        time.sleep(10)  # Sleep for 10 seconds between iterations

if __name__ == '__main__':
    explainer()
