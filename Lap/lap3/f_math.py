from random import randint, choice
from calc import eval
def generate_quiz():
    x = randint (1, 10)
    y = randint (1, 10)
    op = choice(["+", "-", "*", "/"])
    error = randint(-1, 1)
    r = eval(x, y, op) + error
    return [x, y, op, r, error]

quiz = generate_quiz()
x, y, op ,r, error = generate_quiz()
print("{0} {3} {1} = {2}".format(x, y, r, op))
tick = input("true or false? ").upper()

if error == 0:
    if tick == "true":
        print("true")
    else:
        print("false")
else:
    if tick == "false":
        print("true")
    else:
        print("false")