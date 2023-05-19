from pptx_processor import extract_text_from_presentation
from prompt_composer import prompt_composer

file_path = 'End of course exercise - kickof - upload.pptx'
slides_data = extract_text_from_presentation(file_path)
prompt = prompt_composer(slides_data)
