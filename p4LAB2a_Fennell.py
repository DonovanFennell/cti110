import turtle
wn = turtle.Screen()
wn.bgcolor("blue")
wn.title("Dono & Van")

dono = turtle.Turtle()
dono.color("red")
dono.pensize(5)

van = turtle.Turtle()
van.color("white")
van.pensize(5)

for i in [0,1,2,3]:
    dono.forward(250)
    dono.left(90)
    

for i in [0,1,2]:
    van.forward(160)             
    van.left(240)
    van.forward(160)
     
    
