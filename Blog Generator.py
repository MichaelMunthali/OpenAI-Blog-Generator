

import os
from openai import OpenAI


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_blog(topic):
    prompt = f"Write a detailed blog post on: {topic}"
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that writes engaging blog posts."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

print(generate_blog("What initiatives are companies taking to guarantee Sustainable AI practices?"))

