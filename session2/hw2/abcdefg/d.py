n = int(input("Enter a number "))
m = int(n / 2)
d = int(n % 2)
for i in range(m):
    print(" x *", end = "")
if d == 1:
    print(" x")
else:
    print("")