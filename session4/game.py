while True:
    game = {
        'loi dan': 'Hom nay c4e hoc, lop co rat nhieu con trai',
        'cau hoi': 'nguoi dep trai nhat lop la ai?',
        'dap_an' : ['anh Quan', 'anh Huy', 'nguoi viet chuong trinh', 'khong ai ca. ahihi' ]
    }
    print(game)
    choice = int(input("dap an cuoi cung cua ban la gi? 1,2,3 hay 4 "))

    if choice == 3:
        print("True")
        break
    elif choice > 4:
        print("Not to be")
    else:
        print("Flase")


    
            