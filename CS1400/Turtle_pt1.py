'''
Project Name: 
Author: 
Due Date: MM/DD/YYYY
Course: CS1400-zzz

Put your description here, lessons learned here, and any  other information someone using your
program would need to know to make it run.
'''
# (3) add functions here that your main program calls
# to do stuff.

def main():
    '''
    Program starts here.
    '''
    try:
        # (1) replace pass with your code
        import turtle
        import math
        width = int(input("Enter the width of the window: "))
        height = int(input("Enter the height of the window: "))
        turtle.setup(width, height)
    except ValueError:
        print("Enter postive integers for width and height.")
        return
    
    if width < 1 or height < 1:
       print("Enter postive integers for width and height.")
       return 
     
        # (2) replace pass with your code
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


if __name__ == "__main__":
    main()
    