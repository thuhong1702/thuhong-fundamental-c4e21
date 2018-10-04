from turtle import *
speed(0)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
colors_size = len(colors)
pensize(0)
for i in range(colors_size):
    
    color(colors[i])
    begin_fill()
    for j in range(2):
        
        right(90)
        forward(100)
        
        right(90)
        forward(50)
    fillcolor(colors[i])
    end_fill()
    penup()
    forward(50)
    pendown()
penup()
backward(50)
mainloop()
