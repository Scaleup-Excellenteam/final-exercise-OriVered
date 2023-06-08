# PPTX-Analysis-Project

### Project Overview

This project is designed to automate the analysis of PowerPoint (PPTX) presentations using an AI model. It consists of three main components: the server, the explainer script, and the client.

The **server** (`web_api.py`) is a Flask web application that provides an interface for clients to upload their PPTX files. Once a file is uploaded, the application assigns it a unique identifier (uid) and stores it in the 'uploads' folder. This uid is returned to the client and can be used to check the status of the file processing.

The **explainer script** (`explainer.py`) is a background service that continuously checks the 'uploads' folder for new files. Once it finds an unprocessed file, it initiates the process of analysis. The analysis process includes extracting text from the slides, composing prompts based on the text, and sending these prompts to the GPT API for analysis. The responses from the GPT API are then compiled and stored in the 'outputs' folder.

The **client** (`client.py`) is a Python script that you can use to interact with the API. It includes the `PPTXAnalysisClient` class, which abstracts the HTTP calls to the API. This makes it easy to upload files and check their status.

The analysis results can be fetched using the status endpoint of the Flask application by providing the uid of the upload. The results include the status of processing, the filename, the timestamp of upload, and the AI's explanations (if available).

Through these three components, the project provides a seamless and automated way to analyze PowerPoint presentations and extract meaningful insights from them.

## Table of contents

- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installing](#installing)
- [API Documentation](#api-documentation)
- [Usage Example](#usage-Example)

### Project Structure

The main files in this project are:

- **web_api.py**: This script is the main entry point for our Flask web application. It handles file uploads and provides an endpoint to check the status of a file.

- **explainer.py**: This script continuously checks for unprocessed files, processes them with gpt analysis script, and outputs the results to the 'outputs' folder.

- **client.py**: This script is a client that can communicate with our web API, it handles file upload and status checking.

- **pptx_analysis.py**: This script is responsible for calling the functions in engine.py module to process PPTX files.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or above
- pip (Python package installer)

### Installing

Firstly, clone the repository to your local machine:

```bash
git clone https://github.com/your_repository/final-exercise-OriVered.git
```
Change into the cloned directory:
```bash
cd final-exercise-OriVered
```

Install the necessary Python packages:
```bash
pip install -r requirements.txt
```

###Running the Application
You can run the application with the following command:
```bash
python app/api_server/web_api.py
```

This will start the Flask application on your localhost.

To process the PPTX files, run:
```bash
python app/explainer_server/explainer.py
```

### API Documentation

**Upload endpoint**

- **URL**: `/upload`
- **Method**: `POST`
- **Data Params**: `{'file': <file data>}`
- **Success Response**: `{'uid': <uid>}`

**Status endpoint**

- **URL**: `/status/:uid`
- **Method**: `GET`
- **Success Response**: `{'status': <status>, 'filename': <filename>, 'timestamp': <timestamp>, 'explanation': <explanation>}`

### Usage Example

You can interact with the API using any HTTP client like curl, Postman or a browser. Here's an example of how to use this API with Python's `requests` library:

**Uploading a file**

```python
import requests

url = "http://localhost:5000/upload"
file_path = "/path/to/your/pptx/file.pptx"

with open(file_path, 'rb') as f:
    files = {'file': f}
    r = requests.post(url, files=files)
    r.raise_for_status()  # raise exception if error
    print(r.json()['uid'])
```

This will print the unique ID (uid) of the uploaded file.

**Checking the status of a file**

```python
import requests

url = "http://localhost:5000/upload"
file_path = "/path/to/your/pptx/file.pptx"

with open(file_path, 'rb') as f:
    files = {'file': f}
    r = requests.post(url, files=files)
    r.raise_for_status()  # raise exception if error
    print(r.json()['uid'])
```

This will print the status, filename, timestamp, and explanation (if available) of the upload.