person = {
    "name": "Hong",
    "age": "19",
    "city": "Hanoi",
}
# print(person["age"])
# print(person["status"])
person['status'] = 'complicated'
print(person)
del person['age']
print(person)

for x in person.keys():
    print(x)

for v in person.values():
    print(v)

for k, v in person.items():
    print(k, ",", v)

# list gom nhieu dic
# trong dic chua list