fav_items = ["death note", "netflix", "teaching"]
for index, items in enumerate(fav_items):
    print(index + 1, "." items, sep="")
print("* " * 10)
pos = int(input("Position you want to update? "))
fav = input("Your replacing favorite? ")
fav_items[pos] = fav
for index, items in enumerate(fav_items):
    print(index, items)
