import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

question = "Give me one short name for a coffee shop. Reply with only the name."

for temp in [0, 1.5]:
    print("temperature:", temp)
    for run in range(6):
        resp = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[{"role": "user", "content": question}],
            reasoning_effort="low",
            temperature=temp,
        )
        print("  run", run + 1, ":", resp.choices[0].message.content)