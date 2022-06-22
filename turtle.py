import turtle

turtle.shape('turtle')
z = 1
while z == 0:
    turtle.forward(2)
    turtle.left(1)
    turtle.goto(10, 10)


# squars 20

import turtle
def sq(x):
    for i in range(4):
        turtle.forward(x)
        turtle.left(90)


for i in range(10, 30, 10):
    print(i)
    sq(i)
    turtle.setpos(-i, -i)
