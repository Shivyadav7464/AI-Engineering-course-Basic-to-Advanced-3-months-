import math

words = ["cat", "mat", "on"]
scores = [3, 1, 0]

# Kaam 1: har score par exp lagao
exps = [math.exp(s) for s in scores]

# Kaam 2: sabka jod
total = sum(exps)

# Kaam 3: har exp ko total se divide karo
weights = [e / total for e in exps]

# Result dikhao
for w, p in zip(words, weights):
    print(w, round(p * 100, 1), "%")

print("Total:", round(sum(weights) * 100))