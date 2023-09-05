import turtle
t = turtle
def drawCircle(x, y, radius):
    t.penup()
    t.goto(x, y)
    z = 0
    t.pendown()
    while z < 120:
        t.forward((2 * 3.14 * radius)/120)
        t.left(3)
        z += 1
    



drawCircle(50, 75, 100)
