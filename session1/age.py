import datetime
now = datetime.datetime.now()
y = input("When was you born? ")
print("You are ", now.year - int(y), "year olds")