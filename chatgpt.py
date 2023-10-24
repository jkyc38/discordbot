import openai
import os
KEY = os.environ['APIKEY']
openai.organization = "org-yzLbV3WjhpYbF4v77igITOdz"
openai.api_key = KEY

def chatgpt(prompt):
    model_engine = 'text-davinci-003'
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens = 1024,
        n=1, stop=None,
        temperature=0.5
    )
    response = completion.choices[0].text
    response = str(response)
    return response

def test(prompt):
    return chatgpt(prompt)


