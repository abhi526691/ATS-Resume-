import openai, os
from dotenv import load_dotenv
load_dotenv()
class openaiFunc():
    def __init__(self):
        openai.api_key = os.getenv('API_KEY')

    def qna(self, prompt):
        pred_result = openai.Completion.create(
            prompt=prompt,
            temperature=0,
            max_tokens=300,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            model="gpt-3.5-turbo-instruct",
        )
        return pred_result["choices"][0]["text"].split("\n")