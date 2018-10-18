while True:
    pw = input("What is your password? ")
    if len(pw) < 8:
        print("not pass word")
    elif pw.isdigit():
        print("only letter")
    elif pw.isupper():
        print("not only upper letter")
    elif pw.islower():
        print("not only lower letter")
    else:
        print("welcome")
        break
    # l = len(pw)
    # if l >= 8:
        
    #     if not pw.isdigit():
    #         print("Welcome")
    #         break
    #     else:
    #         print("only letter")

    # else:
    #     print("Chuc ban may man lan sau")
    

    
