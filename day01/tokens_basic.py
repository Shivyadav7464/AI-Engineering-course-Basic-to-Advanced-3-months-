import tiktoken

# Tokenizer load karo
enc = tiktoken.get_encoding("o200k_base")

# Ek text likho
text = "Hello, I am learning AI"

# Text ko numbers mein badlo
ids = enc.encode(text)

print("Numbers (token IDs):", ids)
print("Total tokens:", len(ids))

for i in ids:
    print(i, "→", repr(enc.decode([i])))