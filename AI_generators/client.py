import openai
import os


def get_client():
    openai.api_key = os.getenv('OPENAI_API_KEY')
    client = openai.OpenAI()


    if openai.api_key is None:
        print("Please set the OPENAI_API_KEY environment variable")
        return None
    
    return client