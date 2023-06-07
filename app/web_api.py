from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import uuid
import json
from datetime import datetime

# Constants
CURRENT_DIR = os.getcwd()
UPLOAD_FOLDER = os.path.abspath(os.path.join(CURRENT_DIR, 'uploads'))
OUTPUT_FOLDER = os.path.abspath(os.path.join(CURRENT_DIR, 'outputs'))
STATUS_DONE = 'done'
STATUS_PENDING = 'pending'
STATUS_NOT_FOUND = 'not found'
ALLOWED_EXTENSIONS = {'pptx'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Upload endpoint:
    - Receives a POST request with an attached file.
    - Generates a UID for the uploaded file.
    - Saves the file in the `uploads` folder with the original filename, a timestamp, and the UID.
    - Returns a JSON object with the UID of the upload.
    """
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    if 'file' not in request.files:
        return jsonify(error='No file part'), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify(error='No selected file'), 400
    if file and allowed_file(file.filename):
        try:
            uid = str(uuid.uuid4())
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            filename = secure_filename(file.filename)
            new_filename = f"{filename.rsplit('.', 1)[0]}_{timestamp}_{uid}.{filename.rsplit('.', 1)[1]}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], new_filename))
            return jsonify(uid=uid), 200
        except Exception as e:
            return jsonify(error=str(e)), 500
    else:
        return jsonify(error='Invalid file type'), 400

@app.route('/status/<uid>', methods=['GET'])
def check_status(uid):
    """
    Status endpoint:
    - Receives a GET request with a UID as a URL parameter.
    - Returns a JSON object with the status, original filename, timestamp, and explanation of the upload.
    """
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    files = os.listdir(OUTPUT_FOLDER)
    for file in files:
        if uid in file:
            with open(os.path.join(OUTPUT_FOLDER, file), 'r') as f:
                data = json.load(f)
            original_filename, timestamp, _ = file.rsplit('_', 2)
            return jsonify(status=STATUS_DONE, filename=original_filename, timestamp=timestamp, explanation=data), 200
    files = os.listdir(UPLOAD_FOLDER)
    for file in files:
        if uid in file:
            original_filename, timestamp, _ = file.rsplit('_', 2)
            return jsonify(status=STATUS_PENDING, filename=original_filename, timestamp=timestamp, explanation=None), 200
    return jsonify(status=STATUS_NOT_FOUND, filename=None, timestamp=None, explanation=None), 404

if __name__ == '__main__':
    app.run(debug=True)
