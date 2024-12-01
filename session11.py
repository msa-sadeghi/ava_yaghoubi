import turtle
def draw_shape(x,y):
    n = int(sc.numinput("sides", "enter sides: "))
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    for i in range(n):
        t.forward(100)
        t.left(360/n)
    t.end_fill()
    t.color("lightblue")

sc = turtle.Screen()
sc.register_shape("python.gif")
t = turtle.Turtle()
t.speed("normal")
t.shape("turtle") #'arrow', 'turtle', 'circle', 'square', 'triangle', 'classic'
t.shape("python.gif")
t.color("darkgreen")
t.shapesize(4)
t.pencolor("red")
t.pensize(5)
t.fillcolor("orange")
sc.onclick(draw_shape)
turtle.done()