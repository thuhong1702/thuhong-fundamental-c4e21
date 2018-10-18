import datetime
yob = int(input("Year of birth? "))
sth = datetime.datetime.now()
age = sth.year - yob
print("age: ", age)
if age < 10:
    print("Child")
else:
    print("Not child")

print("pp")