line = "ThiS is String with Upper and and lower case letter "
line.lower()
print(line)
letter_alphabet = {
    "a": "2",
    "c": "1",
    "d": "1",
    "e": "5",
    "g": "1",
    "h": "2",
    "i": "4",
    "l": "2",
    "n": "2",
    "o": "1",
    "p": "2",
    "r": "4",
    "s": "5",
    "t": "5",
    "u": "1",
    "w": "2",
}
while True:
    letter = input("What do you wwant to count letter?")
    if letter in letter_alphabet:
        print(letter_alphabet[letter])
    else:
        print("Not found")

