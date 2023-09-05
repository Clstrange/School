import turtle

'''
Project Name: turtle.
Author: Cody L. Strange
Due Date: 2022-2-13
Course: CS1400-X02

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
# (3) add functions here that your main program calls
# to do stuff.

def main():
    '''
    Program starts here.
    '''
    #set turtle. to be invisible
    turtle.ht()

    try:
        width = int(input())
        height = int(input())
    except ValueError:
        print('Width and height must be positive integers.')
        return

    if width < 1 or height < 1:
        print('Width and height must be positive integers.')
        return
 #creates the window
    turtle.setup(width , height)

    # variables for turtle.'s X and Y coordinate
    x_coordinate = (width - 50)/2
    y_coordinate = (height - 50)/2

    #set turtle. speed
    turtle.speed(10)

    #create function for blue rectangle (sky) using x and y coordinates
    def rectangle(x_scale, y_scale, scale=1):
        
        #scaling the shape size
        x_scale *= scale
        y_scale *= scale
        
        #black border color start
        turtle.pencolor("black")
        turtle.begin_fill()
        
        #rectangle shape
        turtle.setx(-x_scale)
        turtle.sety(y_scale)
        turtle.setx(x_scale)
        turtle.sety(y_scale-y_scale)
        turtle.setx(x_scale-x_scale)
        
        #skyblue color end
        turtle.color("skyblue")
        turtle.end_fill()

    #create function for gray triangle(mounain) using x and y coordinates
    def triangle(x_scale, y_scale, scale=1):
        
        #scaling the shape size
        x_scale *= scale
        y_scale *= scale
        
        #green color start
        turtle.pencolor("gray")
        turtle.begin_fill()
        turtle.setx(-x_scale/2)
        turtle.goto(x_scale-x_scale , (y_scale * 2/3))
        turtle.goto((x_scale * 1/2) , y_scale-y_scale)
        turtle.home()
        
        #green color end
        turtle.color("gray")
        turtle.end_fill()

    #create function for yellow diamond(star) using x and y coordinates
    def diamond(x_scale, y_scale, scale=1):
        
        #scaling the shape size
        x_scale *= scale
        y_scale *= scale
        
        #starting postition
        turtle.penup()
        turtle.sety(y_scale * 5/6)
        turtle.setx(x_scale * -3/4)
        turtle.pendown()
        
        #yellow color start
        turtle.pencolor("yellow")
        turtle.begin_fill()
        
        #diamond shape
        turtle.setx(x_scale * -7/8)
        turtle.setx(x_scale * -5/8)
        turtle.goto((x_scale * -6/8) , (y_scale * 12/12))
        turtle.goto((x_scale * -7/8) , (y_scale * 10/12))
        turtle.goto((x_scale * -6/8) , (y_scale * 8/12))
        turtle.goto((x_scale * -5/8) , (y_scale * 10/12))
        
        #yellow color end
        turtle.color("yellow")
        turtle.end_fill()

    #function for tree, triangle and rectangle combined
    def tree(x_scale, y_scale, scale=1):
        
        #scaling shape size
        x_scale *= scale
        y_scale *= scale
        
        #starting position(rectangle)
        turtle.penup()
        turtle.goto(x_scale * -25/32 , (y_scale-y_scale))
        # turtle.pendown
        
        #brown color start
        turtle.pencolor("brown")
        turtle.begin_fill()
        
        #base of tree (rectangle)
        turtle.setx(x_scale * -27/32)
        turtle.sety(y_scale * 4/16)
        turtle.setx(x_scale * -25/32)
        turtle.sety(y_scale-y_scale)
        
        #brown color end
        turtle.color("brown")
        turtle.end_fill()
        
        #starting position(triangle)
        turtle.sety(y_scale * 1/4)
        
        #green color start
        turtle.pencolor("green")
        turtle.begin_fill()
        
        #top of tree(triangle)
        turtle.setx(x_scale * -24/32)
        turtle.setx(x_scale * -28/32)
        turtle.goto((x_scale * -26/32) ,  (y_scale * 7/16))
        turtle.goto((x_scale * -24/32) , (y_scale * 4/16))
        
        #green color end
        turtle.color("green")
        turtle.end_fill()
        
    #function for house (rectangle, triangle)
    def house(x_scale, y_scale, scale=1):
        
        #scaling shape size
        x_scale *= scale
        y_scale *= scale
        
        #set position
        turtle.penup()
        turtle.goto((x_scale * 5/8), (y_scale-y_scale))
        
        #red color start
        turtle.pencolor("red")
        turtle.begin_fill()
        
        #base of house(rectangle)
        turtle.setx(x_scale * 7/8)
        turtle.sety(y_scale * 1/8)
        turtle.setx(x_scale * 5/8)
        turtle.sety(y_scale * 1/8)
        
        #red color end
        turtle.color("red")
        turtle.end_fill()
        
        #setposition
        turtle.sety(y_scale * 1/8)
        
        #tan color start
        turtle.pencolor("tan")
        turtle.begin_fill()
        
        #roof of house(triangle)
        turtle.goto((x_scale * 11/16) , (y_scale * 1/6))
        turtle.goto((x_scale * 7/8) , (y_scale * 1/8))
        
        #tan color end
        turtle.color("tan")
        turtle.end_fill()

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

    #setting starting postion for turtle.
    turtle.penup()
    turtle.goto(x_coordinate-x_coordinate, y_coordinate-y_coordinate)
    turtle.pendown()



if __name__ == "__main__":
    main()
