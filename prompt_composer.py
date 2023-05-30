from typing import List, Dict


def format_slide_text(slide_data: Dict[str, str]) -> str:
    """Formats the text extracted from a slide for inclusion in the prompt."""
    formatted_text = ""

    if slide_data.get('title'):
        formatted_text += f"Title: {slide_data['title']}\n"

    if slide_data.get('subtitle'):
        formatted_text += f"Subtitle: {slide_data['subtitle']}\n"

    if slide_data.get('body'):
        formatted_text += f"Body:\n{slide_data['body']}\n"

    for j, table in enumerate(slide_data.get('tables', [])):
        formatted_text += f"Table {j + 1}:\n"
        for cell_text in table:
            formatted_text += f"{cell_text}\n"

    for j, smartart_text in enumerate(slide_data.get('smartart', [])):
        formatted_text += f"SmartArt {j + 1}:\n{smartart_text}\n"

    return formatted_text


def single_slide_prompt(slide_data: Dict[str, str], slide_number: int) -> str:
    """
    Composes a prompt for a single slide in the presentation, including detailed analysis points.

    Args:
        slide_data (dict): A dictionary representing a slide in the presentation.
        slide_number (int): The number of the slide in the presentation.

    Returns:
        str: The composed prompt for the slide.
    """
    prompt = f"Slide {slide_number} Analysis:\n"
    prompt += format_slide_text(slide_data)
    prompt += "\n"
    prompt += "Please analyze this slide and provide detailed insights on the following aspects:\n\n"
    prompt += "1. Key Message: What is the main message or purpose of this slide?\n"
    prompt += "2. Structure: How is the content on this slide organized? Are there any notable sections or transitions?\n"
    prompt += "3. Supporting Data: What data, statistics, or evidence are provided to support the information on this slide?\n"
    prompt += "4. Visual Aids: What visual aids or graphs are used on this slide to convey information? How effective are they?\n"
    prompt += "5. Engagement: How well does this slide engage the audience? Are there any interactive elements?\n"
    prompt += "6. Strengths: What are the strengths or standout elements of this slide?\n"
    prompt += "7. Weaknesses: Are there any weaknesses or areas for improvement in this slide?\n"
    prompt += "8. Recommendations: Based on your analysis, what recommendations can you provide to enhance this slide?\n\n"
    prompt += "Please provide detailed and well-structured answers to each aspect, supported by specific examples and explanations.\n"
    prompt += "Your analysis should demonstrate a deep understanding of the slide content and its effectiveness in conveying the intended message to the audience.\n\n"
    return prompt


def prompt_composer(slides_data: List[Dict[str, str]]) -> List[str]:
    """
    Compose a list of slides and returns a list of prompts for each slide.

    Args:
        slides_data (list): A list of dictionaries representing the slides in the presentation.

    Returns:
        list: A list of prompts, one for each slide in the presentation.
    """
    prompts = []

    for i, slide_data in enumerate(slides_data):
        slide_number = i + 1
        prompts.append(single_slide_prompt(slide_data, slide_number))

    return prompts


