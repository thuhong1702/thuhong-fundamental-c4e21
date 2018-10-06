quiz_a = {
    1 : 35,
    2 : 36,
    3 : 40,
    4 : 44
}
quiz_b = {
    1 : 'About 55',
    2 : 'About 65',
    3 : 'About 75',
    4 : 'About 85'
}
while True:
    print("Answer the following question:")
    print("If x = 8, then what is the values of 4(x+3)? ")
    for k, v in quiz_a.items():
        print(k, v, sep = ". ")
    choise_a = int(input("Your choise? "))
    if choise_a == 4:
        print(choise_a, "bingo")
    else:
        print(choise_a, ":(")
    print("Estimate this answer (exact caculation not list)")
    print("Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean? ")
    for m, n in quiz_b.items():
        print(m, n, sep = ". ")
    choise_b = int(input("Your choise? "))
    if choise_b == 2:
        print(choise_b, "bingo")
    else:
        print(choise_b, ":(")
     
    if choise_a == 4 and choise_b == 2:
        print(choise_a, choise_b)
        print("You answed correctly 2 questions")
    elif choise_a == 4 or choise_b == 2:
        print("You answed correctly 1 in 2 questions")
    else:
        print("You answed incorrectly 2 questions")
    break