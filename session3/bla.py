
something = ['Chess', 'Zing', 'PacMan']
print(*something, sep = " | ")
while True:
    i = int(input("What do you see number? "))
    if i < len(something):
        print(i-1, ". ", something[i])
        break
    else:
        print("over in4")
