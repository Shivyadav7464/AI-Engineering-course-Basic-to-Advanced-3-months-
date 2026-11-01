import math

words = ["The", "cat", "sat", "on"]

# Har row = ek word, jo baaki words ko dekh raha hai
scores = [
    [2, 1, 3, 0],    # The
    [1, 2, 0, 1],    # cat
    [0, 3, 1, 2],    # sat
    [1, 0, 2, 3],    # on
]

for i in range(len(words)):
    row = []
    for j in range(len(words)):
        if j > i:                          # j aage ka word hai
            row.append(float("-inf"))      # parda lagao
        else:
            row.append(scores[i][j])       # peeche ka word, score rakho

    # Ab wahi softmax jo pehle likha tha
    exps = [math.exp(s) for s in row]
    total = sum(exps)
    weights = [e / total for e in exps]

    print(words[i], [round(w * 100, 1) for w in weights])