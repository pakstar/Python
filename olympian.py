import turtle

t = turtle.Pen()

t.speed(10)
initial_x = -200
initial_y = -70
t.penup()
t.goto(initial_x,0)
t.pendown()
for i in range(2):
        t.circle(100)
        t.penup()
        initial_x += 150
        t.goto(initial_x,0)
        t.pendown()


for j in range(3):
            t.circle(100)
            t.penup()
            initial_x -=100
            t.goto(initial_x,initial_y)
            t.pendown()
                   
            
turtle.done()