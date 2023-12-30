import turtle as t
from itertools import cycle 


colors = cycle(['red', 'orange', 'yellow', 'blue', 'purple'])

t.bgcolor('black')
t.pensize(4)
t.speed("fast")




def circle(radius, angle, shift):
    color = next(colors)
    t.pencolor(color)
    t.circle(radius)
    t.right(angle)
    t.forward(shift)
    circle(radius+5, angle+1, shift+1)

circle(30, 0 ,1)








circle()

t.done()