import random
import turtle

def simulate():
    pass

def main():
    #simplifing variables
    rnd = random
    t = turtle
    #User inputs
    trial_count = int(input("Enter amount of trials to commence:"))
    walk_dist = int(input("Enter walking distance:"))
    person_walk = input("Enter who will be walking:")



    #options for rnd.choice to pick from
    reg_walk = [0, 180]
    pa_walk = reg_walk + [90, 270]
    ma_walk = pa_walk + [270]

    #returns turtle to starting position
    def turtle_home ():
        t.penup()
        t.home()

    #pa function
    def pa ():
        for x in range(trial_count):
            turtle_home()       
            for y in range(walk_dist):
                #turtle moves in random direction
                t.setheading(rnd.choice(pa_walk))
                t.penup()
                t.forward(10)
            #leaves a marker    
            t.pendown()
            t.color("black")
            t.stamp()    
            print(t.pos())
    def ma ():
        for x in range(trial_count):
            turtle_home()       
            for y in range(walk_dist):
                #turtle moves south twice as often
                t.setheading(rnd.choice(ma_walk))
                t.penup()
                t.forward(10)
            #leaves a marker
            t.pendown()
            t.color("green")
            t.stamp()
            
    def reg():
        for x in range(trial_count):
            turtle_home()       
            for y in range(walk_dist):
                #turtle only moves east and west
                t.setheading(rnd.choice(reg_walk))
                t.penup()
                t.forward(10)
            #leaves a marker
            t.pendown()
            t.color("red")
            t.stamp()


    #instant graphing
    t.tracer(0,0)

    #change shape and run pa 
    t.shape("circle")
    pa()

    #change shape and run ma
    t.shape("square")
    ma()

    #change shape and run reg
    t.shape("classic")
    reg()
if __name__ == "__main__":
    main()
