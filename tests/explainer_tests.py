import os
import pytest
import unittest.mock
from app.explainer import os, explainer_loop, UPLOAD_FOLDER, SCRIPT_PATH

@pytest.fixture
def mock_listdir_and_run():
    with unittest.mock.patch('os.listdir') as mock_listdir, \
         unittest.mock.patch('subprocess.run') as mock_run:
        yield mock_listdir, mock_run

def test_explainer(mock_listdir_and_run):
    mock_listdir, mock_run = mock_listdir_and_run

    mock_listdir.side_effect = [
        ['file1_uid1', 'file2_uid2'],
        ['file1_uid1']
    ]

    mock_run.return_value = None

    explainer_loop()

    mock_run.assert_called_once_with(['python', SCRIPT_PATH, os.path.join(UPLOAD_FOLDER, 'file2_uid2')], check=True)
