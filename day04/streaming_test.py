import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

resp = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[{"role": "user", "content": "Write a 5-line story about Virat Kohli in easy englis words."}],
    reasoning_effort="low",
    stream= True,
)

for chunk in resp:
    piece = chunk.choices[0].delta.content
    if piece:
        print(piece,end="", flush=True)

print()