#system_test.py
import os
import subprocess
import time
import pytest
from app.client.client import PPTXAnalysisClient

CURRENT_DIR = os.getcwd()
DIRECTORY_PATH = os.path.dirname(CURRENT_DIR)
SAMPLE_FILE = os.path.join(DIRECTORY_PATH, 'presentation.pptx')
API_PATH = os.path.join(DIRECTORY_PATH, 'app', 'api_server', 'web_api.py')
EXPLAINER_PATH = os.path.join(DIRECTORY_PATH, 'app', 'explainer_server', 'explainer.py')

BASE_URL = 'http://localhost:5000'

@pytest.fixture(scope='session', autouse=True)
def server():
    # Starting the server
    server = subprocess.Popen(['python', API_PATH])
    time.sleep(5) # Wait for server to start
    yield server
    # Cleanup after test
    server.terminate()

@pytest.fixture(scope='session', autouse=True)
def explainer():
    # Starting the explainer
    explainer = subprocess.Popen(['python', EXPLAINER_PATH])
    yield explainer
    # Cleanup after test
    explainer.terminate()

def test_main():
    client = PPTXAnalysisClient(BASE_URL)

    # Upload a file
    uid = client.upload(SAMPLE_FILE)
    assert uid is not None, "Upload failed - no UID returned."

    # Check the status of the upload
    status = client.status(uid)
    assert status.status == 'pending', f"Expected status 'pending', got {status.status}"

    # Wait for some time to let the explainer process the file
    time.sleep(100)

    # Check the status of the upload
    status = client.status(uid)
    assert status.status == 'done', f"Expected status 'done', got {status.status}"

    # Check if the processing is done
    if status.is_done():
        assert True, "Processing is not done."
