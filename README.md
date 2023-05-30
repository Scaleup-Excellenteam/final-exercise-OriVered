# Project Overview

This project is a Python-based solution for analyzing PowerPoint presentations. The script reads the content from a PowerPoint file (`.pptx`), sends the slide information to an AI model for generating insights, and saves the AI responses into a JSON file.

This repository contains:

- `pptx_gpt_analysis.py`: The main script that calls the `engine.py` module for processing the PowerPoint file.
- `engine.py`: This module includes the `process_pptx` function for orchestrating the extraction of text from the PowerPoint slides, generating AI prompts, making calls to the AI model, and saving the responses to a JSON file.
- `pptx_processor.py`: This module provides classes and functions for extracting text, tables, and SmartArt from the PowerPoint slides.
- `prompt_composer.py`: This module provides functions for formatting the extracted slide data and generating prompts to send to the AI model.
- `gpt_api_calls.py`: This module (not included in the code provided) makes asynchronous calls to the AI model and gets responses for the generated prompts.
- `json_output.py`: This module provides a function for outputting the AI responses to a JSON file.

## Installation

To install the required packages, it is recommended to set up a new virtual environment to avoid conflicts with your existing Python packages. You can follow these steps to set up a virtual environment and install the required packages:

1. Create a new virtual environment:

```
python -m venv pptx-analysis-env
```

2. Activate the virtual environment:
- For Windows:
  ```
  pptx-analysis-env\Scripts\activate
  ```
- For macOS/Linux:
  ```
  source pptx-analysis-env/bin/activate
  ```

3. Install the required packages using pip:
```
pip install -r requirements.txt
```

These steps will create a new virtual environment named
  ```
  pptx-analysis-env
  ```
and install all the necessary packages specified in the `requirements.txt` file.

## Running the Script

Once you have set up the virtual environment and installed the required packages, you can run the script to analyze your PowerPoint presentation.

1. Activate the virtual environment (if not already activated):
- For Windows:
  ```
  pptx-analysis-env\Scripts\activate
  ```
- For macOS/Linux:
  ```
  source pptx-analysis-env/bin/activate
  ```

2. Run the script with the PowerPoint file path as an argument:
```
python pptx_gpt_analysis.py <file-path>
```

Replace `<file-path>` with the path to your `.pptx` file. For example:

```
python pptx_gpt_analysis.py presentation.pptx
```


The script will check if the file exists. If the file exists, it will process the presentation and generate AI insights. The AI responses will be saved in a JSON file in the same directory as the PowerPoint file.

If an error occurs during processing, an error message will be printed to the console.

Please note that due to the asynchronous nature of the AI API calls, Python 3.7 or higher is required.

## Output

The output of this program is a JSON file with the same name as the input PowerPoint file, located in the same directory. The JSON file contains the AI responses for each slide in the presentation.
