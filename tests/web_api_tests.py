import pytest
import os
import time
from app.web_api import app, UPLOAD_FOLDER, OUTPUT_FOLDER, STATUS_DONE, STATUS_PENDING, STATUS_NOT_FOUND

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATH = os.path.join(PROJECT_DIR, 'pptx_analysis', 'poster.pptx')
UPLOAD_ENDPOINT = '/upload'
STATUS_ENDPOINT = '/status/'

NON_EXISTING_UID = 'non_existing_uid'
EMPTY_STRING = ''

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def cleanup(uid):
    """
    Cleanup function to remove files after testing.
    """
    files = os.listdir(UPLOAD_FOLDER) + os.listdir(OUTPUT_FOLDER)
    for file in files:
        if uid in file:
            if file in os.listdir(UPLOAD_FOLDER):
                os.remove(os.path.join(UPLOAD_FOLDER, file))
            if file in os.listdir(OUTPUT_FOLDER):
                os.remove(os.path.join(OUTPUT_FOLDER, file))

def test_upload_endpoint(client):
    # Test that the upload endpoint returns a 400 when no file part is provided
    response = client.post(UPLOAD_ENDPOINT, data={})
    assert response.status_code == 400

    # Test that the upload endpoint returns a 400 when no file is selected
    response = client.post(UPLOAD_ENDPOINT, data={'file': (None, None)})
    assert response.status_code == 400

    # Test that the upload endpoint returns a UID
    response = client.post(UPLOAD_ENDPOINT, data={'file': (open(FILE_PATH, 'rb'), os.path.basename(FILE_PATH))})
    assert 'uid' in response.get_json()

    # Test that the upload creates a file in the uploads folder
    uid = response.get_json()['uid']
    assert any(uid in file for file in os.listdir(UPLOAD_FOLDER))
    cleanup(uid)

def test_status_endpoint(client):
    # Test that the status endpoint returns a 'pending' status right after uploading a file
    response = client.post(UPLOAD_ENDPOINT, data={'file': (open(FILE_PATH, 'rb'), os.path.basename(FILE_PATH))})
    uid = response.get_json()['uid']
    response = client.get(STATUS_ENDPOINT + uid)
    assert response.get_json()['status'] == STATUS_PENDING

    # Test that the status endpoint returns a 'not found' status for a non-existing UID
    response = client.get(STATUS_ENDPOINT + NON_EXISTING_UID)
    assert response.get_json()['status'] == STATUS_NOT_FOUND
    cleanup(uid)