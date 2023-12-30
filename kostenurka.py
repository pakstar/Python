import turtle

t = turtle.Turtle()
length = 5
for count in range(100):
    t.forward(length)
    t.right(135)
    length = length + 5


turtle.done()

# +5 za da se uvelichava vseki put, forward e raven na legth 