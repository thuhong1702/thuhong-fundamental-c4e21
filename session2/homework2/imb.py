height = float(input("What is your height? "))
weight = float(input("what is your weight? ")) # 155 str = ['1','5','5']

IMB = weight / (height*height/0.0001)
if IMB < 16:
    print("Severely underweight")
elif 16 <= IMB < 18.5:
    print("Underweight")
elif 18.5 <= IMB < 25:
    print("Normal")
elif 25 <= IMB < 30:
    print("Overweight")
else:
    print("Obese")