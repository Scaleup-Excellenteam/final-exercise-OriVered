import os
import asyncio

import httpx as httpx


# Define constants
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-3.5-turbo"
TIMEOUT = 10
SYSTEM_PROMPT = "You are an expert at evaluating and providing critical analysis of .pptx presentations."
OPENAI_URL = "https://api.openai.com/v1/engines/{}/completions".format(MODEL)

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer {}".format("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")
}

async def call_gpt(prompt):
    """
    Sends a prompt to the GPT API and returns the response.

    Args:
        prompt (str): A string representing the prompt to be sent to the GPT API.

    Returns:
        dict: The response from the GPT API. If an error occurs, returns a dictionary containing an error message.
    """
    data = {
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            response = await client.post(
                OPENAI_URL,
                headers=headers,
                json=data,
            )
            response.raise_for_status()
    except (httpx.TimeoutException, httpx.HTTPStatusError, httpx.RequestError) as e:
        # Instead of raising the exception, return it as part of the response
        return {
            'error': str(e),
            'prompt': prompt,
            'response': {}
        }

    # If no exceptions, return the response
    return {'prompt': prompt, 'response': response.json()}

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

    responses = await asyncio.gather(*tasks)
    return responses