# ---------- Part 1: zaruri cheezein ----------
import os                          # computer ki settings padhne ke liye (key yahin se aati hai)
from dotenv import load_dotenv     # .env file padhne ke liye
from groq import Groq              # Groq se baat karne wali library

# ---------- Part 2: Groq se connect karo ----------
load_dotenv()                                        # .env kholo, key yaad kar lo
client = Groq(api_key=os.getenv("GROQ_API_KEY"))     # key se Groq ka client banao

# ---------- Part 3: System prompt (bot ka rulebook) ----------
# Teen quotes ke andar kai line likh sakte hain
SYSTEM_PROMPT = """You are Brew Buddy, a friendly assistant for the coffee shop Bean & Brew.
Always reply in English, in at most 3 short lines."""

# ---------- Part 4: History (notebook) ----------
# Chat shuru hone se pehle hi list mein ek message hai: system.
# Ye list mein sabse pehle rehta hai aur poori chat mein ek baar hi hota hai.
history = [{"role": "system", "content": SYSTEM_PROMPT}]

print("Brew Buddy ready. Type quit to exit.")

# ---------- Part 5: Chat ka loop ----------
while True:                                    # tab tak chalta hai jab tak break na ho
    user_text = input("You: ")                 # tumse ek line leta hai

    if user_text.strip() == "":                # khali Enter par call mat karo
        continue                               # wapas input par jao

    if user_text.lower() == "quit":            # quit likha to chat band
        break

    # Step A: tumhara message history mein jodo
    history.append({"role": "user", "content": user_text})

    # Step B: POORI history (system + purani chat + naya sawal) model ko bhejo
    resp = client.chat.completions.create(
        model="openai/gpt-oss-20b",            # kaunsa model
        messages=history,                      # poori list, sirf naya message nahi
        reasoning_effort="low",                # kam sochne ke tokens (Day 3)
        temperature=0.3,                       # thodi variety, zyada random nahi (Day 4)
    )

    # Step C: model ka jawab nikalo
    reply = resp.choices[0].message.content

    # Step D: model ka jawab bhi history mein jodo, taaki agli baar model ko dikhe
    history.append({"role": "assistant", "content": reply})

    # Step E: dikhao
    print("Bot:", reply)
    print("   [prompt_tokens:", resp.usage.prompt_tokens, "]")