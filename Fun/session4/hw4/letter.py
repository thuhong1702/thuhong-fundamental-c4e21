sentence = input("Enter your sentense: ").lower()
chars = list(sentence)
print(chars)

char_dict = {}
for char in sentence:
    if char not in char_dict:
        char_dict[char] = 1
        print(char_dict)
    else:
        char_dict[char] += 1
        print(char_dict)