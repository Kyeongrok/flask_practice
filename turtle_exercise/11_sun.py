import turtle
import time

turtle.penup()
# turtle.goto(-250, 30)


tt = turtle.Turtle()
tt.color('blue')
tt.pensize(10)
tt.shape('turtle')
for i in range(12):
    tt.forward(100)
    tt.left(120)
    tt.forward(100)
    tt.left(120)
    tt.forward(100)

    tt.left(90)
    tt.penup()
    tt.forward(50)
    tt.pendown()

    # tt.left(90)




time.sleep(5)