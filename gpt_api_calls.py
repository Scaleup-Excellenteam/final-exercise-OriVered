import os
import asyncio
import openai

# Define constants
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL = "gpt-3.5-turbo"
TIMEOUT = 500
SYSTEM_PROMPT = "You are an expert at evaluating and providing critical analysis of .pptx presentations."
OPENAI_URL = "https://api.openai.com/v1/engines/{}/completions".format(MODEL)

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {}".format("")
}


async def call_gpt(prompt):
    """
    Sends a prompt to the GPT API and returns the response.

    Args:
        prompt (str): A string representing the prompt to be sent to the GPT API.

    Returns:
        dict: The response from the GPT API. If an error occurs, returns a dictionary containing an error message.
    """

    openai.api_key = OPENAI_API_KEY
    loop = asyncio.get_event_loop()

    try:
        # Run the OpenAI call within a timeout context
        response = await asyncio.wait_for(loop.run_in_executor(None, lambda: openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ]
            )), timeout=TIMEOUT)
    except openai.error.OpenAIError as e:
        print(f"Full response: {e}")
        return {
            'error': str(e),
            'prompt': prompt,
            'response': {}
        }
    except asyncio.TimeoutError:
        print("Request timed out")
        return {
            'error': 'Timeout',
            'prompt': prompt,
            'response': {}
        }

    # If no exceptions, return the response
    return {'prompt': prompt, 'response': response.to_dict()}

async def gpt_api_calls(prompts):
    """
    Compose a list of prompts and returns a list of responses for each prompt.

    Args:
        prompts (list): A list of prompts to be sent to the GPT API.

    Returns:
        list: A list of responses, one for each prompt in the list.
    """
    tasks = []
    for prompt in prompts:
        tasks.append(call_gpt(prompt))

    responses = await asyncio.gather(*tasks, return_exceptions=True)
    return responses
