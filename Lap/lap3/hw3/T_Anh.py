from turtle import *
speed(0)
begin_fill()

def draw_square(x, y):

    x = i
    y = pencolor("red")
    
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
end_fill()
mainloop()