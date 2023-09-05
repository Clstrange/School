import turtle
import math

windowWidth = int(input("Enter the width of the window: "))
windowHeight = int(input("Enter the height of the window: "))
turtle.setup(windowWidth, windowHeight)

#square
turtle.left(30)
turtle.pencolor("brown")
turtle.fillcolor("red")
turtle.begin_fill()
for square in range(4):
    turtle.forward(20)
    turtle.left(90)
turtle.color("blue")
turtle.end_fill()
turtle.penup()

#rectangle
turtle.forward(100)
turtle.pendown()
turtle.left(15)
turtle.pencolor("yellow")
turtle.fillcolor("green")
turtle.begin_fill()
for rectangle in range(2):
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
turtle.color("brown")
turtle.end_fill()
turtle.penup()

#triangle
turtle.forward(100)
turtle.pendown()
turtle.left(45)
turtle.pencolor("pink")
turtle.fillcolor("blue")
turtle.begin_fill()
for triangle in range(3):
    turtle.forward(100)
    turtle.left(120)
turtle.color("black")
turtle.end_fill()
turtle.penup()
