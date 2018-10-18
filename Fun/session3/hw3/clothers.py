clothe_items = ['T-Shit' , 'Sweater']
print(clothe_items)
while True:
    command = input('''Welcome to our shop, what do you want (R, C, U, D)?''').upper()

    if command == "R":
        print(*clothe_items, sep = ", ")
        print("* " * 10)

    elif command == "C":
        new_item = input("New item?")
        clothe_items.append(new_item)
        print(*clothe_items, sep=", ")
       
        print("* " * 10)

    elif command == "U":
        pos = int(input("Position you want to update? "))
        update = input("Change to what? ")
        clothe_items[ pos-1 ] = update
        print(*clothe_items, sep = ", ")
        print("* " * 10)
    
    else:
        n = input("Position you want to delete? ")
        if n.isdigit():
            i = int(n)
            clothe_items.pop( i-1 )
            print(clothe_items)
        else:
            clothe_items.pop(n)
            print(*clothe_items, sep = ", ")
            print("* " * 10)