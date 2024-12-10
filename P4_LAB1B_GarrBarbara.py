# Barbara Garr
# 8 December 24
# P4LAB1b
# This program draws my initals BG

import turtle 
win = turtle.Screen() 
t = turtle.Turtle() 
t.shape('turtle')
t.pensize(6)
t.pencolor("purple")

t.circle(37,180)
t.left(90)
t.forward(155)
t.left(90)
t.circle(40,180)

t.penup()
t.goto(150, 40)
t.pendown()

t.right(90)
t.forward(20)
t.left(90)
t.forward(30)
t.circle(65, 260)
t.left(100)
t.forward(50)

turtle.done()


