a = float(input("Enter a = "))
b = float(input("Enter b = "))
c = float(input("Enter c = "))


delta = b*b - 4*a*c

if d > 0:
    delta_sqrt = delta**0.5
    x1 = (-b + delta_sqrt)/ 2*a
    x2 = (-b + delta_sqrt)/ 2*a
    print(x1, x2 )
elif d == 0:
    x = -b/ 2*a
    print(x)
else:
    print("Phuong trinh vo nghiem")
