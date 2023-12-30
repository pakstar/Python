
def draw_audi(t):
    t.speed(10)
    initial_x = -200
    t.penup()
    t.goto(initial_x,0)
    t.pendown()
    for i in range(4):
        t.circle(100)
        t.penup()
        initial_x += 150
        t.goto(initial_x,0)
        t.pendown()


