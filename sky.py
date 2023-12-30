import turtle  as t
from random import randint, random
t.bgcolor('blue')
while True:
    points = randint(2,5) * 2 + 1
    size = randint(10, 50)
    color = (random(), random(), random())
    angel = 180 - (180/points)
    x = randint(-350, 300)
    y = randint(-250, 250)
    t.penup()
    t.goto(x ,y)
    t.color(color)
    t.pendown()
    t.begin_fill()

    for i in range(points):
        t.forward(size)
        t.right(angel)

    t.end_fill()



