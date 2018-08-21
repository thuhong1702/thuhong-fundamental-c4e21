yob = int(input("Your year of brith? "))
age = 2018 - yob
print("Your age:", age)

if age < 10:
    print("Baby")
elif age < 18:
    print("Teanager")
else:
    print("Adult")
