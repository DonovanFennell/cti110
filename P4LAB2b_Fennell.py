import turtle
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("Dono & Van")

d = turtle.Turtle()
d.color("red")
d.pensize(5)

d.penup()
d.forward(-200)
d.pendown()
for i in range(1):
    d.circle(100,180)
    d.left(90)
    d.forward(200)
    d.left(90)
    d.penup()
    d.forward(150)
    d.pendown()
    d.left(90)
    d.forward(100)
    d.left(-90)
    d.forward(50)
    d.forward(-50)
    d.left(90)
    d.forward(100)
    d.left(-90)
    d.forward(100)
    
