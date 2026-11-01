# ---------- Part 1: zaruri cheezein ----------
import os
import re                          # text mein se numbers dhundhne ke liye
import time
from dotenv import load_dotenv
from groq import Groq

# ---------- Part 2: Groq se connect karo ----------
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ---------- Part 3: Do tareeke ke instructions ----------
DIRECT = "Answer with only the final number. No explanation."
COT = "Think step by step. Then write the final answer on the last line exactly as: Final: <number>"

# ---------- Part 4: Sawal aur unka sahi jawab ----------
QUESTIONS = [
    {"q": "A bat and a ball cost 110 rupees together. The bat costs 100 rupees more than the ball. How much does the ball cost in rupees?", "answer": 5},
    {"q": "If 5 machines take 5 minutes to make 5 widgets, how many minutes would 100 machines take to make 100 widgets?", "answer": 5},
    {"q": "A shirt costs 850 rupees. A 20 percent discount is applied, then 5 percent GST is added on the discounted price. What is the final price in rupees?", "answer": 714},
]


# ---------- Part 5: Function 1: "Final:" wali line se jawab nikalo ----------
def get_final(text):
    for line in reversed(text.strip().split("\n")):        # text ko neeche se upar padho
        if line.strip().startswith("Final:"):              # jis line ki shuruaat "Final:" se ho
            return line.strip()[len("Final:"):].strip()    # "Final:" hatake baaki wapas karo
    return text.strip()                                    # nahi mili to poora text wapas


# ---------- Part 6: Function 2: kya jawab sahi hai? ----------
def is_correct(text, correct):
    numbers = re.findall(r"\d+(?:\.\d+)?", text.replace(",", ""))    # text mein se saare numbers nikalo
    return any(abs(float(n) - correct) < 0.01 for n in numbers)      # koi bhi number sahi jawab ke barabar?


# ---------- Part 7: Har sawal, dono modes mein ----------
for item in QUESTIONS:                                      # BAHAR wala loop: ek-ek sawal
    print("QUESTION:", item["q"][:60], "...")

    for mode, system_text in [("direct", DIRECT), ("cot", COT)]:     # ANDAR wala loop: direct, phir cot
        resp = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "system", "content": system_text},          # mode ka instruction
                {"role": "user", "content": item["q"]},              # sawal
            ],
            reasoning_effort="low",
            temperature=0,                                           # taaki tulna sahi ho
        )
        text = resp.choices[0].message.content
        final = get_final(text) if mode == "cot" else text.strip()   # cot mode mein "Final:" wali line nikalo
        ok = is_correct(final, item["answer"])

        print("  mode:", mode)
        print("  final answer:", final)
        print("  correct:", ok)
        print("  completion_tokens:", resp.usage.completion_tokens,
              "| reasoning_tokens:", resp.usage.completion_tokens_details.reasoning_tokens)
        time.sleep(1)
    print("---")