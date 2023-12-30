import turtle 
t = turtle.Pen()
t.speed(10)
initial_x = -200
initial_y = 0
t.penup()
t.goto(initial_x,0)
t.pendown()
for count in range(3):  
    t.penup()
    t.pendown()
    t.circle(100)
    t.penup()
    t.goto(200)
    t.pendown()
    t.circle(100)

turtle.done()