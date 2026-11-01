import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Call 1: model ko apna naam batao
resp1 = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[{"role": "user", "content": "My name is Rahul."}],
    reasoning_effort="low",
)
print("Call 1 jawab:", resp1.choices[0].message.content)

# Call 2: ek NAYI call, pichli baat nahi bheji
resp2 = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[{"role": "user", "content": "What is my name?"}],
    reasoning_effort="low",
)
print("Call 2 jawab:", resp2.choices[0].message.content)