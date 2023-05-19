from pptx_processor import extract_text_from_presentation



file_path = 'End of course exercise - kickof - upload.pptx'
slides_data = extract_text_from_presentation(file_path)
print(slides_data)