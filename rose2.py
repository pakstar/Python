import turtle
number = int(input())
t = turtle.Pen()
t.speed(10)

for i in range(number):
    t.circle(100)
    t.left(360/number)



  
turtle.done()