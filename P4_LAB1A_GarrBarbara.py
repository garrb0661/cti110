# Barbara Garr
# 8 December 24
# P4LAB1a
# This program draws a square and a triangle

import turtle 
win = turtle.Screen() 
t = turtle.Turtle() 
t.shape('turtle')
t.pensize(4)
t.pencolor("pink")

square_sides = 4
square_side_length = 150
square_angle = 90

for i in range(square_sides):
        t.forward(square_side_length)
        t.right(square_angle)
        
t.penup()
t.goto(50,100)
t.pendown()

triangle_sides = 3
triangle_side_length = 150
triangle_angle = 360 / triangle_sides

for i in range(triangle_sides):
        t.forward(triangle_side_length)
        t.right(triangle_angle)

turtle.done()
