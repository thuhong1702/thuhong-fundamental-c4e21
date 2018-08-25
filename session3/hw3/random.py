from random import shuffle, choice
word_list = ['merci', 'lundi', 'petit', 'grand']
word = choice(word_list)
chars = list(word)
chars_len = len(chars)
shuffle(chars)
for i in range(chars_len):
    n = choice(chars)
    print(chars[n], end = "")
    chars.remove(n)
print()
read = input("Enter the word: ")
if  read == word:
    print("True")
else:
    print("False")

