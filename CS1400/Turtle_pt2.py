'''
Turtle
Cody L. Strange
4/7/2022
CS1400-006

During this project I used a fractional system to create all of the shapes in proportion of one another
as if on a grid. In a 1500 pixel window you would have a grid that had x and y values of -750 and 750.
Using this grid I was able to create the shapes in exact locaton of eachother based on the screen size.
It allows you to mathmatically plot your shapes exactly where you want them to be but it comes at a cost.
I couldn't use traditional loops to create the shapes because you had to manually plot each point where
you would want it in relation to other shapes and the window size. It scales wonderfully and scales perfectly
as the window size changes but requires a lot more code. I used a while loop to create a consectutive scaling image that would
constanly decrease in size by one half. I assigned each object a function that I could set parameters for so that it would be
able to scale as needed and to save lines of code when I wanted to create copies.

'''
#importing modules
import turtle
#set turtle to a shorter named variable
t = turtle
def triangle(xcordinate, ycordinate, scale=1):
    """create function for gray triangle(mounain) using xcordinate and y coordinates """
    #scaling the shape size
    xcordinate *= scale
    ycordinate *= scale

    #green color start
    t.pencolor("gray")
    t.begin_fill()
    t.setx(-xcordinate/2)
    t.goto(xcordinate-xcordinate , (ycordinate * 2/3))
    t.goto((xcordinate * 1/2) , ycordinate-ycordinate)
    t.home()

    #green color end
    t.color("gray")
    t.end_fill()

def diamond(xcordinate, ycordinate, scale=1):
    """create function for yellow diamond(star) using x and y coordinates"""
    #scaling the shape size
    xcordinate *= scale
    ycordinate *= scale

    #starting postition
    t.penup()
    t.sety(ycordinate * 5/6)
    t.setx(xcordinate * -3/4)
    t.pendown()

    #yellow color start
    t.pencolor("yellow")
    t.begin_fill()

    #diamond shape
    t.setx(xcordinate * -7/8)
    t.setx(xcordinate * -5/8)
    t.goto((xcordinate * -6/8) , (ycordinate * 12/12))
    t.goto((xcordinate * -7/8) , (ycordinate * 10/12))
    t.goto((xcordinate * -6/8) , (ycordinate * 8/12))
    t.goto((xcordinate * -5/8) , (ycordinate * 10/12))

    #yellow color end
    t.color("yellow")
    t.end_fill()

def tree(xcordinate, ycordinate, scale=1):
    """function for tree, triangle and rectangle combined"""
    #scaling shape size
    xcordinate *= scale
    ycordinate *= scale

    #starting position(rectangle)
    t.penup()
    t.goto(xcordinate * -25/32 , (ycordinate-ycordinate))
    t.pendown()

    #brown color start
    t.pencolor("brown")
    t.begin_fill()

    #base of tree (rectangle)
    t.setx(xcordinate * -27/32)
    t.sety(ycordinate * 4/16)
    t.setx(xcordinate * -25/32)
    t.sety(ycordinate-ycordinate)

    #brown color end
    t.color("brown")
    t.end_fill()

    #starting position(triangle)
    t.sety(ycordinate * 1/4)

    #green color start
    t.pencolor("green")
    t.begin_fill()

    #top of tree(triangle)
    t.setx(xcordinate * -24/32)
    t.setx(xcordinate * -28/32)
    t.goto((xcordinate * -26/32) ,  (ycordinate * 7/16))
    t.goto((xcordinate * -24/32) , (ycordinate * 4/16))

    #green color end
    t.color("green")
    t.end_fill()

def house(xcordinate, ycordinate, scale=1):
    """function for house (rectangle, triangle)"""

    #scaling shape size
    xcordinate *= scale
    ycordinate *= scale

    #set position
    t.penup()
    t.goto((xcordinate * 5/8), (ycordinate-ycordinate))

    #red color start
    t.pencolor("red")
    t.begin_fill()

    #base of house(rectangle)
    t.setx(xcordinate * 7/8)
    t.sety(ycordinate * 1/8)
    t.setx(xcordinate * 5/8)
    t.sety(ycordinate * 1/8)

    #red color end
    t.color("red")
    t.end_fill()

    #setposition
    t.sety(ycordinate * 1/8)

    #tan color start
    t.pencolor("tan")
    t.begin_fill()

    #roof of house(triangle)
    t.goto((xcordinate * 11/16) , (ycordinate * 1/6))
    t.goto((xcordinate * 7/8) , (ycordinate * 1/8))

    #tan color end
    t.color("tan")
    t.end_fill()

def rectangle(xcordinate, ycordinate, scale=1):
    """create function for blue rectangle (sky) using x and y coordinates"""
    #scaling the shape size
    xcordinate *= scale
    ycordinate *= scale

    #black border color start
    t.pencolor("black")
    t.begin_fill()

    #rectangle shape
    t.setx(-xcordinate)
    t.sety(ycordinate)
    t.setx(xcordinate)
    t.sety(ycordinate-ycordinate)
    t.setx(xcordinate-xcordinate)

    #skyblue color end
    t.color("skyblue")
    t.end_fill()

def main():
    """Main function"""

    #set turtle to a shorter named variable
    t.ht()

    # #preset values for width and height
    width = int(input("input width: "))
    height = int(input("input height: "))

    #creates the window
    t.setup(width , height)

    # variables for turtle's X and Y coordinate
    x_coordinate = (width - 50)/2
    y_coordinate = (height - 50)/2

    #set turtle speed
    t.speed(10)

    #drawing rectangle blue sky
    rectangle(x_coordinate, y_coordinate)

    #drawing triangle gray mountain
    triangle(x_coordinate, y_coordinate)

    #drawing diamond yellow star
    diamond(x_coordinate, y_coordinate)

    #drawing brown and green tree
    tree(x_coordinate, y_coordinate)

    #drawing red and tan house
    house(x_coordinate, y_coordinate)

    #setting starting postion for turtle
    t.penup()
    t.goto(x_coordinate-x_coordinate, y_coordinate-y_coordinate)
    t.pendown()

    #variable for scaling down shapes
    scale_down = .5

    #throw away variable for while loop
    xcordinate = 0

    #function creates consecutive scaled down scenes
    while xcordinate < 5:

        #scaled down rectangle
        rectangle(x_coordinate, y_coordinate, scale_down)

        #scaled down triangle
        triangle(x_coordinate, y_coordinate, scale_down)

        #scaled down diamond
        diamond(x_coordinate, y_coordinate, scale_down)

        #scaled down tree
        tree(x_coordinate, y_coordinate, scale_down)

        #scaled down house
        house(x_coordinate, y_coordinate, scale_down)

        #setting starting postion for turtle
        t.penup()
        t.goto(x_coordinate-x_coordinate, y_coordinate-y_coordinate)
        t.pendown()

        #amount of times the program runs
        xcordinate +=1

        #consecutive scaling down
        scale_down = scale_down/2

    #ending turtle program
    turtle.done()

if __name__ == "__main__":
    main()
