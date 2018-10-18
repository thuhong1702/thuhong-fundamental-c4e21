quiz = {
    1 : 35,
    2 : 36,
    3 : 40,
    4 : 44
}
while True:
    print("Answer the following question:")
    print("If x = 8, then what is the values of 4(x+3)? ")
    for k, v in quiz.items():
        print(k, v, sep = ". ")
    choise = int(input("Your choise? "))
    if choise == 4:
        print("bingo")
        break
    
    else:
        print(":(")
