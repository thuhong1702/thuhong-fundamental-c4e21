from turtle import *

speed(10)

pencolor("blue")
left(60)
forward(100)
right(120)
forward(100)
right(120)

for i in range(5):
    pencolor("red")
    forward(100)
    right(90)

pencolor("blue")
left(18)

for j in range(4):
    forward(100)
    right(72)

for k in range(6):
    pencolor("red")
    forward(100)
    right(60)



mainloop()
