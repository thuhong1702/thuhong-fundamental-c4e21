# 1. Chuyen chu hoa ve chu thuong
sentence = input("Enter your sentense: ").lower()
chars = list(sentence)
print(chars)
# 2. Bo het dau cach trong sentence (replace)


# 3.1
char_dict = {}
for char in sentence:
    if char not in char_dict:
        char_dict[char] = 1
        print(char_dict)
    else:
        char_dict[char] += 1
        print(char_dict)