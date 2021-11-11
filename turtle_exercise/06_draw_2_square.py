import turtle
import time

tt = turtle.Turtle()
tt.shape('turtle')
tt.color('magenta')
tt.pensize(5)

tt.penup()
tt.goto(-175,100)
tt.pendown()
for i in range(4):
    tt.forward(100)
    tt.left(90)
tt.penup()


tt = turtle.Turtle()
tt.shape('turtle')
tt.color('orange')
tt.pensize(5)

tt.penup()
tt.goto(-60,100)
tt.pendown()
for i in range(4):
    tt.forward(100)
    tt.left(90)
tt.penup()



time.sleep(5)

