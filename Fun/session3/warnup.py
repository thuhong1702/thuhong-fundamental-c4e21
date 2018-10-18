while True:
    yob_str = (input("What is your brithday? "))
    if yob_str.isdigit():
        yob = int(yob_str)
        age = 2018 - yob
        print(age)
        break
    else:
        print("You was wrong. Enter a number ")