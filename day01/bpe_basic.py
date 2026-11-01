from collections import Counter

# Function 1: jodiyan ginta hai
def get_pairs(tokens):
    return Counter(zip(tokens, tokens[1:]))

# Function 2: ek jodi ko naye token se badal deta hai
def merge(tokens, pair, new_id):
    out = []
    i = 0
    while i < len(tokens):
        if i < len(tokens) - 1 and (tokens[i], tokens[i + 1]) == pair:
            out.append(new_id)
            i += 2
        else:
            out.append(tokens[i])
            i += 1
    return out

text = "low low low lower lowest"

# Har akshar ko number (0-255) mein badlo
tokens = list(text.encode("utf-8"))
print("Shuru:", tokens)
print("Shuru mein tokens:", len(tokens))
print()

# NAYA: vocabulary. Shuru mein sirf 256 single bytes hain
vocab = {i: bytes([i]) for i in range(256)}

# 5 baar merge karo
for step in range(5):
    pairs = get_pairs(tokens)
    best = max(pairs, key=pairs.get)       # sabse zyada aane wali jodi
    new_id = 256 + step                    # naya token number
    tokens = merge(tokens, best, new_id)

    # NAYA: naye token ka matlab vocab mein likho (dono tukde jod kar)
    vocab[new_id] = vocab[best[0]] + vocab[best[1]]

    print(f"Step {step}: naya token {new_id} = {vocab[new_id].decode()!r}, ab tokens: {len(tokens)}")

print()
print("Final tokens:", tokens)
print("Final tokens ka text:", [vocab[t].decode() for t in tokens])