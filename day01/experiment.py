import tiktoken;

enc = tiktoken.get_encoding("o200k_base")

tests = [
    "Hello",
    "hello",
    " hello",
    "HELLO",
    "Aaryan",
    "Mai AI engineering seekh raha hoon",

]

for t in tests:
    ids = enc.encode(t)
    print(repr(t), "→", len(ids), "tokens →", [enc.decode([i]) for i in ids])