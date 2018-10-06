
person = {
    'name': 'Pink',
    'age': '19',
}
key = input("Enter a item: ")
if key in person:
    value = person[key]
    print(value)
else:
    print("Not found")

