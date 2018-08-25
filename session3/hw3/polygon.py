from turtle import *

n = 180 - (360*5)/(7*2)

pencolor("grey")
for i in range(7):
    forward(100)
    left(n)


left(120)

for j in range(5):
    color("yellow")
    forward(100)
    right(60)

right(108) 
for k in range(4):
    pencolor("brown")
    forward(100)
    left(72)
left(90)
for m in range(3):
    pencolor("blue")
    forward(100)
    right(90)


pencolor("red")
right(60)
forward(100)
left(120)
forward(100)

mainloop()