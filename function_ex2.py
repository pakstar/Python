import turtle as t
#definirane za risuvane na robot
def draw_triangle(a, b, color):
    t.pendown()
    t.speed(1)
    t.color(color)
    t.begin_fill()
    for i in range(1, 3):
        t.forward(a)
        t.right(90)
        t.forward(b)
        t.right(90)
    t.end_fill()
    t.penup()

t.penup()
t.pensize("slow")
t.bgcolor('Dodger blue')

def feet():
    #feet
    t.goto(-100,-150)
    draw_triangle(50,20, "blue")
    t.goto(-30,-150)
    draw_triangle(50,20, "blue")

def legs():
    #legs
    t.goto(-25,-50)
    draw_triangle(15,100, "grey")
    t.goto(-55,-50)
    draw_triangle(-15,100, "grey")

def body():
    #body
    t.goto(-90, 100)
    draw_triangle(100,150, 'red')



def right_arm():
    #right arm
    t.goto(-150,70)
    draw_triangle(60,15, 'grey')
    t.goto(-150,110)
    draw_triangle(15,40, "grey")

def left_arm():
    #left arm
    t.goto(10,70)
    draw_triangle(60,15, "grey")
    t.goto(55,110)
    draw_triangle(15,40, "grey")

def neck():
    #neck
    t.goto(-50, 120)
    draw_triangle(15,20, "grey")
    #head 
    t.goto(-85, 170)
    draw_triangle(80,50, 'red')

def eyes():
    #eyes
    t.goto(-60,160)
    draw_triangle(30,20,"white")
    t.goto(-55,155)
    draw_triangle(5,5,'black')
    t.goto(-40,155)
    draw_triangle(5,5, 'black')

def mouth():
    #mouth
    t.goto(-65,135)
    draw_triangle(40,5,'black')




def draw_robot():
     feet()
     legs()
     body()
     right_arm()
     left_arm()
     neck()
     eyes()
     mouth()


draw_robot()
     





t.done()




