dic_intro = {
    'name': 'Conan',
    'day': '1900',
    'by': 'Aoyama',
}
print(dic_intro)
command = input('''you want to (D or U)? ''').upper()
if command == "D":
    key = input("what key? ")
    if key not in dic_intro:
        print("")
    else:
        del dic_intro[key]
        print(dic_intro)
else:
    key = input("what key? ")
    value = input("what value?")
    dic_intro[key] = value
    print(dic_intro)



