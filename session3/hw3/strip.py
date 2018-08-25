from turtle import *

colors = ['red', 'blue', 'brown', 'yellow', 'grey']
color_size = len(colors)

speed(0)

pensize(0)

for i in range(color_size):
    color_n = colors[i]
    color(color_n)
    begin_fill()
    for t in range(2):
        right(90)
        forward(100)
        right(90)
        forward(50)
    fillcolor(color_n)
    end_fill()
    penup()
    forward(50)
    pendown()
penup()
backward(50)

mainloop()
