clothe_items = ['T-Shit' , 'Sweater']

while True:
    command = input('''Welcome to our shop, what do you want (R, C, U, D)?''').upper()

    if command == "R":
        for i, item in enumerate(clothe_items):
            print(i, item,)
        print("* " * 10)

    elif command.upper() == "C":
        new_item = input("New item?")
        clothe_items.append(new_item)
        print(clothe_items)
        print("* " * 10)

    elif command.upper() == "U":
        n = int(input("Position you want to update? "))
        clothe_item = input("update to? ")
        clothe_items[n] = clothe_item
        print(clothe_items)
        print("* " * 10)
    
    else:
        n = int(input("Position you want to delete? "))
        clothe_items.pop(n)
        menu_items.remove('Jeans')
        print(menu_items)
        print("* " * 10)