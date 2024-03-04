import openai
import os

def test():
    # openai.api_key = os.getenv('OPENAI_API_KEY')
    print(os.getenv('OPENAI_API_KEY'))

    openai.api_key = os.getenv('OPENAI_API_KEY')
    client = openai.OpenAI()

    # if openai.api_key is None:
    #     print("Please set the OPENAI_API_KEY environment variable")
    # else:
    #     print("yaaaay")

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
    )

    print(completion.choices[0].message)

