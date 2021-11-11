import turtle

tt = turtle.Turtle()
tt.color('red')
tt.pensize(5)

def draw_square():
    for i in range(4):
        tt.left(90)
        tt.forward(100)

draw_square()

tt.penup()
tt.goto(120, 0)
tt.pendown()
tt.color('magenta')

draw_square()