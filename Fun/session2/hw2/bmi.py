height = int(input("What is your height?(cm) "))
w = int(input("What is your weight?(kg) "))
h = height / 100
BMI = w/(h*h)
print("Your BMI: ", BMI)
if BMI < 16:
    print("Severely underweight")
elif 16 <= BMI <= 18.5:
    print("Underweight")
elif 18.5 < BMI <= 25:
    print("Normal")
elif 25 < BMI < 30:
    print("Overweight")
else:
    print("Obese")