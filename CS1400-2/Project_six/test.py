"""
Date: 4/22/2022
Project: Random Walk
Name: Cody Strange

Summary: I was able to get it to work pretty well from the start.
I used the pythagorean theorm to determine distance. I ran into some
trouble with the Mi-Ma traveling south twice as often but was easy enough
to fix once i knew what was wrong.

"""
import subprocess
import tempfile
import random
import numpy
import math
import sys
import turtle

def save_to_image(dest='random_walk.png'):
    '''Saves the turtle canvas to dest. Do not modify this function.'''
    with tempfile.NamedTemporaryFile(prefix='random_walk',
                                     suffix='.eps') as tmp:
        turtle.getcanvas().postscript(file=tmp.name)
        subprocess.run(['gs',
                        '-dSAFER',
                        '-o',
                        dest,
                        '-r200',
                        '-dEPSCrop',
                        '-sDEVICE=png16m',
                        tmp.name],
                       stdout=subprocess.DEVNULL)

def pa_walk(walk_lyst, trial_count):
    """Random walk for Pa"""
    for walk in walk_lyst:
        print("Pa random walk of " + str(walk) + " steps")
        y_axis = 0 #North - South
        x_axis = 0 #East - West
        coordinates = 0 # sqrt(x_axis^2 + y_axis^2)
        trial_lyst = []
        for trial in range(trial_count):
            if trial == "pointless":
                print("pain")
            for step in range(walk):
                if step == "pointless":
                    print("pain")
                direction = random.randint(1,4)
                if direction == 1: #North
                    y_axis += 1
                elif direction == 2: #East
                    x_axis += 1
                elif direction == 3: #South
                    y_axis -= 1
                elif direction == 4: #West
                    x_axis -= 1
            coordinates = math.sqrt(x_axis**2 + y_axis**2)
            trial_lyst.append(coordinates)
            mean = round(sum(trial_lyst) / len(trial_lyst),1)
            walk_max = round(max(trial_lyst),1)
            walk_min = round(min(trial_lyst),1)
            cv_num = round(numpy.std(trial_lyst) / mean,1)
            y_axis = 0 #North - South
            x_axis = 0 #East - West

        print("Mean = " + str(mean), end=" ")
        print("CV = " + str(cv_num))
        print("Max = " + str(walk_max), end=" ")
        print("Min = " + str(walk_min))

def mi_ma_walk(walk_lyst, trial_count):
    """random walk for Pa"""
    for walk in walk_lyst:
        print("Mi-Ma random walk of " + str(walk) + " steps")
        y_axis = 0 #North - South
        x_axis = 0 #East - West
        coordinates = 0 # sqrt(x_axis^2 + y_axis^2)
        trial_lyst = []
        for trial in range(trial_count):
            if trial == "pointless":
                print("pain")
            for step in range(walk):
                if step == "pointless":
                    print("pain")
                direction = random.randint(1,5)
                if direction == 1: #North
                    y_axis += 1
                elif direction == 2: #East
                    x_axis += 1
                elif direction == 3: #South
                    y_axis -= 1
                elif direction == 4: #South
                    y_axis -= 1
                elif direction == 5: #West
                    x_axis -= 1
            coordinates = math.sqrt(x_axis**2 + y_axis**2)
            trial_lyst.append(coordinates)
            mean = round(sum(trial_lyst) / len(trial_lyst),1)
            walk_max = round(max(trial_lyst),1)
            walk_min = round(min(trial_lyst),1)
            cv_num = round(numpy.std(trial_lyst) / mean,1)
            y_axis = 0 #North - South
            x_axis = 0 #East - West

        print("Mean = " + str(mean), end=" ")
        print("CV = " + str(cv_num))
        print("Max = " + str(walk_max), end=" ")
        print("Min = " + str(walk_min))

def reg_walk(walk_lyst, trial_count):
    "random walk for Reg"
    for walk in walk_lyst:
        print("Reg random walk of " + str(walk) + " steps")
        y_axis = 0 #North - South
        x_axis = 0 #East - West
        coordinates = 0 # sqrt(x_axis^2 + y_axis^2)
        trial_lyst = []
        for trial in range(trial_count):
            if trial == "pointless":
                print("pain")
            for step in range(walk):
                if step == "pointless":
                    print("pain")
                direction = random.randint(1,2)
                if direction == 1: #East
                    x_axis += 1
                elif direction == 2: #West
                    x_axis -= 1
            coordinates = math.sqrt(x_axis**2 + y_axis**2)
            trial_lyst.append(coordinates)
            mean = round(sum(trial_lyst) / len(trial_lyst),1)
            walk_max = round(max(trial_lyst),1)
            walk_min = round(min(trial_lyst),1)
            cv_num = round(numpy.std(trial_lyst) / mean,1)
            x_axis = 0 #East - West

        print("Mean = " + str(mean), end=" ")
        print("CV = " + str(cv_num))
        print("Max = " + str(walk_max), end=" ")
        print("Min = " + str(walk_min))

def simulate(walk_lyst, trial_count, walker):
    """Runs whichever walk the user decides"""
    if walker == "Pa":
        pa_walk(walk_lyst, trial_count)
    elif walker == "Mi-Ma":
        mi_ma_walk(walk_lyst, trial_count)
    elif walker == "Reg":
        reg_walk(walk_lyst, trial_count)
    elif walker == "all":
        pa_walk(walk_lyst, trial_count)
        mi_ma_walk(walk_lyst, trial_count)
        reg_walk(walk_lyst, trial_count)
    else:
        print("Please enter on of the options: Pa, Mi-Ma, Reg, All")

def plot():
    """creates an image of the graph that is created by a walk"""
    turtle.screensize(300,400)
    turtle.penup()
    turtle.shapesize(.5)
    turtle.shape("circle") #Pa's plot graph
    y_axis = 0 #North - South
    x_axis = 0 #East - West
    for trial in range(50):
        if trial == "pointless":
            print("pain")
        for step in range(100):
            if step == "pointless":
                print("pain")
            direction = random.randint(1,4)
            if direction == 1: #North
                y_axis += 1
            elif direction == 2: #East
                x_axis += 1
            elif direction == 3: #South
                y_axis -= 1
            elif direction == 4: #West
                x_axis -= 1

        turtle.goto(x_axis * 5,y_axis * 5)
        turtle.stamp()
        y_axis = 0 #North - South
        x_axis = 0 #East - West

    turtle.shape("square") #Ma's plot graph
    turtle.color("green")
    y_axis = 0 #North - South
    x_axis = 0 #East - West
    for trial in range(50):
        if trial == "pointless":
            print("pain")
        for step in range(100):
            if step == "pointless":
                print("pain")
            direction = random.randint(1,5)
            if direction == 1: #North
                y_axis += 1
            elif direction == 2: #East
                x_axis += 1
            elif direction == 3: #South
                y_axis -= 1
            elif direction == 4: #South
                y_axis -= 1
            elif direction == 5: #West
                x_axis -= 1

        turtle.goto(x_axis * 5,y_axis * 5)
        turtle.stamp()
        y_axis = 0 #North - South
        x_axis = 0 #East - West

    turtle.shape("triangle") #Reg's plot graph
    turtle.color("red")
    y_axis = 0 #North - South
    x_axis = 0 #East - West
    for trial in range(50):
        if trial == "pointless":
            print("pain")
        for step in range(100):
            if step == "pointless":
                print("pain")
            direction = random.randint(1,2)
            if direction == 1: #East
                x_axis += 1
            elif direction == 2: #West
                x_axis -= 1

        turtle.goto(x_axis * 5,y_axis * 5)
        turtle.stamp()
        y_axis = 0 #North - South
        x_axis = 0 #East - West
    save_to_image()

def main():
    """main function"""
    walk_lyst = []
    temp_lyst = sys.argv[1].split(',')
    for walk in temp_lyst:
        walk_lyst.append(int(walk))
    trial_count = int(sys.argv[2])
    walker = sys.argv[3]
    simulate(walk_lyst, trial_count, walker)
    plot()
if __name__ == "__main__":
    main()
