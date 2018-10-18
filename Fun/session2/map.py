from turtle import *
shape("turtle")
speed(0)
begin_fill()
color("pink")

for i in range(720):
    forward(i/50)

    left(8)
mainloop()