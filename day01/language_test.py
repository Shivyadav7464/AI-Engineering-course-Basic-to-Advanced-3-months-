import tiktoken

enc = tiktoken.get_encoding("o200k_base")

english = "I am learning AI engineering"
hindi = "मैं एआई इंजीनियरिंग सीख रहा हूँ"

print("English tokens:", len(enc.encode(english)))
print("Hindi tokens:  ", len(enc.encode(hindi)))

word = "unbelievable"
for i in enc.encode(word):
    print(i, "→", repr(enc.decode([i])))