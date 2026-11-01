import json

# JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate. It is commonly used for transmitting data between a server and a web application as text.

text = '{"positive": "Coffee was good", "negative": "Waiter was rude", "rating": 3, "recommend": false, "tags": ["service", "coffee"], "refund": null}'

data = json.loads(text)          # text (string) -> Python dict
print(data["negative"])          # naam se value nikalo
print(type(data))                # kaunsa type bana?
print(data["rating"] + 1)        # number hai, to hisaab ho sakta hai
print(data["recommend"], data["refund"])   # false -> False, null -> None
print(data["tags"][0])           # list ka pehla item

print(json.dumps(data))          # dict -> wapas JSON text