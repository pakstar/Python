import turtle, random
t = turtle.Pen()
t.shape("turtle")
t.pensize(5)

colors = ["red","green","blue","orange","purple","pink","yellow","black"]
for i in range(5):
    color = random.choice(colors)
    t.color(color)
    t.forward(100)
    t.right(144)


turtle.done()