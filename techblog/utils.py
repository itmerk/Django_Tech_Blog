import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # or another engine like "gpt-3.5-turbo"
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()
