# Total ginne ke liye do khali dabbe, shuru mein 0
total_without = 0
total_with = 0

# Token number 1 se 5 tak (range 6 se pehle ruk jaata hai)
for token_number in range(1, 6):
    without_cache = token_number     # bina cache: token n par n words process hote hain
    with_cache = 1                   # cache ke saath: har token par sirf 1 naya word

    total_without = total_without + without_cache    # dabbe mein jodte jao
    total_with = total_with + with_cache

    print("Token", token_number, "-> bina cache:", without_cache, "| cache ke saath:", with_cache)

print("---")
print("Total bina cache:", total_without)
print("Total cache ke saath:", total_with)