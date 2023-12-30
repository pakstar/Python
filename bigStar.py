import turtle, random
t = turtle.Turtle()
t.shape('turtle')
t.pensize(5)
t.speed(10)


colors = ['blue','orange','black','red','green']
length = 5
for count in range(100):
    color = random.choice(colors)
    t.forward(length)
    t.right(135)
    t.color(color)
    length = length + 5

turtle.done()