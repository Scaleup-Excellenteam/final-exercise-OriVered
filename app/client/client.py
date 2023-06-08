import requests
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Status:
    status: str
    filename: str
    timestamp: datetime
    explanation: str

    def is_done(self):
        return self.status == 'done'

class PPTXAnalysisClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def upload(self, filepath):
        url = f"{self.base_url}/upload"
        with open(filepath, 'rb') as f:
            files = {'file': f}
            r = requests.post(url, files=files)
            r.raise_for_status()  # raise exception if error
            return r.json()['uid']

    def status(self, uid):
        url = f"{self.base_url}/status/{uid}"
        r = requests.get(url)
        r.raise_for_status()  # raise exception if error
        data = r.json()
        timestamp = datetime.strptime(data['timestamp'], "%Y%m%d%H%M%S")
        return Status(data['status'], data['filename'], timestamp, data['explanation'])
