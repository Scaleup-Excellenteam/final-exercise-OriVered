import asyncio
from pptx_processor import extract_text_from_presentation
from prompt_composer import prompt_composer
from gpt_api_calls import gpt_api_calls
from json_output import output_to_json

def process_pptx(file_path, output_path):
    try:
        slides_data = extract_text_from_presentation(file_path)
        prompts = prompt_composer(slides_data)
        AI_responses = asyncio.run(gpt_api_calls(prompts))

        # Output AI_responses to a JSON file
        output_to_json(file_path,output_path, AI_responses)

    except Exception as e:
        print(f"An error occurred during processing: {e}")
