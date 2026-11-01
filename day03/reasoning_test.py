# import os
# from dotenv import load_dotenv
# from groq import Groq

# load_dotenv()
# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# questions = [
#     "Say hello in one line.",
#     "A shop sells 3 pens for 12 rupees. How much do 7 pens cost? Explain briefly.",
# ]

# for q in questions:
#     resp = client.chat.completions.create(
#         model="openai/gpt-oss-20b",
#         messages=[{"role": "user", "content": q}],
#     )
#     u = resp.usage
#     print("Question:", q)
#     print("Answer:", resp.choices[0].message.content)
#     print("completion_tokens:", u.completion_tokens)
#     print("reasoning_tokens:", u.completion_tokens_details.reasoning_tokens)
#     print("---")

# import os
# from dotenv import load_dotenv
# from groq import Groq

# load_dotenv()
# client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# question = "Say hello in one line."
# question = "A shop sells 3 pens for 12 rupees. How much do 7 pens cost? Explain briefly."

# for effort in ["low", "high"]:
#     print("effort:", effort)
#     totals = []
#     for run in range(3):
#         resp = client.chat.completions.create(
#             model="openai/gpt-oss-20b",
#             messages=[{"role": "user", "content": question}],
#             reasoning_effort=effort,
#         )
#         t = resp.usage.completion_tokens
#         totals.append(t)
#         print("  run", run + 1, "completion_tokens:", t)
#     print("  min:", min(totals), "max:", max(totals), "average:", sum(totals) / len(totals))


# ---------- Part 1: zaruri cheezein bulao ----------
import os                          # computer ki settings padhne ke liye (API key yahin se aati hai)
from dotenv import load_dotenv     # .env file padhne ke liye
from groq import Groq              # Groq se baat karne wali library

# ---------- Part 2: Groq se connect karo ----------
load_dotenv()                                        # .env file kholo aur key yaad kar lo
client = Groq(api_key=os.getenv("GROQ_API_KEY"))     # key se Groq ka "client" banao (ye hamara phone hai)

# ---------- Part 3: sawalon ki list ----------
questions = [
    # Sawal 1: gaadi wala. "Give only the final answer" isliye, taaki jawab chhota aaye
    "A train leaves a station at 9:00 AM at 60 km/h. A second train leaves the same station at 10:00 AM at 90 km/h in the same direction. At what time does the second train catch the first? Give only the final answer.",
    # Sawal 2: ginti wala
    "How many positive integers less than 100 are divisible by 3 or 5 but not by 15? Give only the final number.",
]

# ---------- Part 4: dono loops ----------
for q in questions:                          # BAHAR WALA LOOP: ek-ek sawal uthao, naam rakho q
    print("QUESTION:", q[:60], "...")        # sawal ke sirf pehle 60 akshar dikhao

    for effort in ["low", "high"]:           # ANDAR WALA LOOP: usi sawal ke liye pehle low, phir high

        # Groq ko sawal bhejo
        resp = client.chat.completions.create(
            model="openai/gpt-oss-20b",                       # kaunsa model use karna hai
            messages=[{"role": "user", "content": q}],        # hamara sawal (q dabba)
            reasoning_effort=effort,                          # left = Groq ka naam, right = hamara dabba (low ya high)
        )

        # Jawab aur tokens bahar nikalo
        answer = resp.choices[0].message.content    # model ka jawab (text)
        tokens = resp.usage.completion_tokens       # kitne tokens kharch hue (sochne wale bhi)

        # Natija dikhao
        print("  effort:", effort, "| tokens:", tokens, "| answer:", answer)

    print("---")                                   # ek sawal khatam, line kheench do
    print("---")