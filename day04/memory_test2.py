# ---------- Part 1: zaruri cheezein ----------
import os
from dotenv import load_dotenv
from groq import Groq

# ---------- Part 2: Groq se connect karo ----------
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---------- Part 3: khali notebook (history) ----------
history = []

print("Chat shuru. Band karne ke liye quit likho.")

# ---------- Part 4: chat ka loop ----------
while True:                                   # ye loop tab tak chalta hai jab tak hum break na karein
    user_text = input("You: ")  
    if(user_text.strip() == ""):    
        continue              # tumse ek line likhwata hai

    if user_text.lower() == "quit":           # agar tumne quit likha
        break                                 # to loop band

    # Step A: tumhara message notebook mein jodo
    history.append({"role": "user", "content": user_text})

    # Step B: POORI notebook model ko bhejo
    resp = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=history,                     # sirf naya message nahi, poori history
        reasoning_effort="low",
    )
    reply = resp.choices[0].message.content   # model ka jawab

    # Step C: model ka jawab bhi notebook mein jodo
    history.append({"role": "assistant", "content": reply})

    # Step D: dikhao
    print("Bot:", reply)
    print("   [prompt_tokens:", resp.usage.prompt_tokens, "| messages in history:", len(history), "]")