import openai
import os

def test(prompt:str):
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
        {"role": "system", "content": prompt},
    ]
    )

    response = completion.choices[0].message

    return response

