from groq import Groq

client = Groq(
  api_key="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"
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

