import math

words = ["dog", "food", "the"]

# "it" ka sawal (Query)
query = [2, 0.5]

# Har word ka label (Key)
keys = [
    [1, 0],        # dog
    [0, 1],        # food
    [0.1, 0.1],    # the
]

# Har word ka content (Value)
values = [
    [8, 2],        # dog
    [2, 8],        # food
    [1, 1],        # the
]

# Kaam 1: Query ka har Key se match score
scores = []
for k in keys:
    score = query[0] * k[0] + query[1] * k[1]
    scores.append(score)

# Kaam 2: softmax (percentage banao)
exps = [math.exp(s) for s in scores]
total = sum(exps)
weights = [e / total for e in exps]

for w, p in zip(words, weights):
    print(w, round(p * 100, 1), "%")

# Kaam 3: percentage ke hisaab se Value mix karo
out = [0, 0]
for weight, v in zip(weights, values):
    out[0] += weight * v[0]
    out[1] += weight * v[1]

print("Naya vector:", [round(x, 2) for x in out])