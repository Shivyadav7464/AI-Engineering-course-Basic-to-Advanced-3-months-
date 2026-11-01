import math

emb ={
    "king": [0.9,0.8],
    "queen": [0.9,0.7],
    "apple": [0.1,0.2],
}

#Dono marksheet kitni door hai ye nikalte hai

def distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

print("Difference between king and queen:", distance(emb["king"], emb["queen"]))
print("Difference between king and apple:", distance(emb["king"], emb["apple"]))