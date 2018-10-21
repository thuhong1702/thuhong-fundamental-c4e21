from turtle import *
def draw_star(size,color):
    angle = 144
    fillcolor(color)
    for i in range(5):
        pencolor("red")
        forward(size)
        right(angle)
        forward(size)
        right(72 - angle)
        end_fill()
        
    return
draw_star(100, "red")

mainloop()

