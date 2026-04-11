from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()  # IMPORTANT

api_key = os.getenv("GROQ_API_KEY")

client = Groq(
api_key = api_key
)


def generate_story(prompt, genre, length):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": f"Write a {length.lower()} {genre.lower()} story."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content

