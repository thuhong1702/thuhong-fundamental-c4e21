items = ['Sky', 'Sea', 'Land', 'Fire']
print(items)
n = input("What do you delete? ")
print(n.isdigit())
if n.isdigit():
    i = int(n)
    items.pop( i - 1)
    print(items)
else:
    items.remove(n)
    print(items)