favvv_items = ['tech', 'teaching', 'may']
for i, item in fav:
    print(i + 1, item)
while True:
    command = input("what do you want (C, R, U, D)?").upper()

    if command == "C":
        new_item = input("")
        fav_items.append(new_item)
        input("What your fav add? ")
        print(fav_items)

    elif command == "R":
        for i item in enumerate(fav_items):
            print(i, items)

    print("* " * 10)

    elif command == "U":

 
    pos = int(input("Position you want to update? "))
    fav = input("Your replacing favorite? ")
    fav_items[pos] = fav
    for index, items in enumerate(fav_items):
        print(index, items)


    else: