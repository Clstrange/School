
import random
import numpy
from math import sqrt
from sys import argv
import turtle

def pa_walk(walk_lyst, trial_count):
    for walk in walk_lyst:
        print("Pa random walk of " + str(walk) + " steps")
        y_axis = 0 #North - South
        x_axis = 0 #East - West
        coordinates = 0 # sqrt(x_axis^2 + y_axis^2)
        trial_lyst = []
        for trial in range(trial_count):
            for step in range(walk):
                direction = random.randint(1,4)
                if direction == 1: #North
                    y_axis += 1
                elif direction == 2: #South
                    y_axis -= 1
                elif direction == 3: #East
                    x_axis += 1
                elif direction == 4: #West
                    x_axis -= 1      
            coordinates = sqrt(x_axis**2 + y_axis**2)
            trial_lyst.append(coordinates)
            mean = round(sum(trial_lyst) / len(trial_lyst),1)
            walk_max = round(max(trial_lyst),1)
            walk_min = round(min(trial_lyst),1)
            cv = round(numpy.std(trial_lyst) / mean,1)
            y_axis = 0 #North - South
            x_axis = 0 #East - West

        print("Mean = " + str(mean), end=" ")
        print("CV = " + str(cv))
        print("Max = " + str(walk_max), end=" ")
        print("Min = " + str(walk_min))

def mi_ma_walk(walk_lyst, trial_count):
        for walk in walk_lyst:
            print("Mi-Ma random walk of " + str(walk) + " steps")
            y_axis = 0 #North - South
            x_axis = 0 #East - West
            coordinates = 0 # sqrt(x_axis^2 + y_axis^2)
            trial_lyst = []
            for trial in range(trial_count):
                for step in range(walk):
                    direction = random.randint(1,4)
                    if direction == 1: #North
                        y_axis += 1
                    elif direction == 2: #South
                        y_axis -= 2
                    elif direction == 3: #East
                        x_axis += 1
                    elif direction == 4: #West
                        x_axis -= 1      
                coordinates = sqrt(x_axis**2 + y_axis**2)
                trial_lyst.append(coordinates)
                mean = round(sum(trial_lyst) / len(trial_lyst),1)
                walk_max = round(max(trial_lyst),1)
                walk_min = round(min(trial_lyst),1)
                cv = round(numpy.std(trial_lyst) / mean,1)
                y_axis = 0 #North - South
                x_axis = 0 #East - West

            print("Mean = " + str(mean), end=" ")
            print("CV = " + str(cv))
            print("Max = " + str(walk_max), end=" ")
            print("Min = " + str(walk_min))

def reg_walk(walk_lyst, trial_count):
        for walk in walk_lyst:
            print("Reg random walk of " + str(walk) + " steps")
            y_axis = 0 #North - South
            x_axis = 0 #East - West
            coordinates = 0 # sqrt(x_axis^2 + y_axis^2)
            trial_lyst = []
            for trial in range(trial_count):
                for step in range(walk):
                    direction = random.randint(1,4)
                    if direction == 3: #East
                        x_axis += 1
                    elif direction == 4: #West
                        x_axis -= 1      
                coordinates = sqrt(x_axis**2 + y_axis**2)
                trial_lyst.append(coordinates)
                mean = round(sum(trial_lyst) / len(trial_lyst),1)
                walk_max = round(max(trial_lyst),1)
                walk_min = round(min(trial_lyst),1)
                cv = round(numpy.std(trial_lyst) / mean,1)
                x_axis = 0 #East - West

            print("Mean = " + str(mean), end=" ")
            print("CV = " + str(cv))
            print("Max = " + str(walk_max), end=" ")
            print("Min = " + str(walk_min))

def simulate(walk_lyst, trial_count, walker):
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
    turtle.screensize(300,400)
    turtle.penup()
    turtle.shapesize(.5)

    """Pa's plot graph"""
    turtle.shape("circle")
    y_axis = 0 #North - South
    x_axis = 0 #East - West
    coordinates = 0 # sqrt(x_axis^2 + y_axis^2)
    trial_lyst = []
    for trial in range(50):
        for step in range(100):
            direction = random.randint(1,4)
            if direction == 1: #North
                y_axis += 1
            elif direction == 2: #South
                y_axis -= 1
            elif direction == 3: #East
                x_axis += 1
            elif direction == 4: #West
                x_axis -= 1

        turtle.goto(x_axis * 5,y_axis * 5)    
        turtle.stamp()
        y_axis = 0 #North - South
        x_axis = 0 #East - West

        """Mi-Ma's plot graph"""
    turtle.shape("square")
    turtle.color("green")
    y_axis = 0 #North - South
    x_axis = 0 #East - West
    coordinates = 0 # sqrt(x_axis^2 + y_axis^2)
    trial_lyst = []
    for trial in range(50):
        for step in range(100):
            direction = random.randint(1,4)
            if direction == 1: #North
                y_axis += 1
            elif direction == 2: #South
                y_axis -= 2
            elif direction == 3: #East
                x_axis += 1
            elif direction == 4: #West
                x_axis -= 1

        turtle.goto(x_axis * 5,y_axis * 5)    
        turtle.stamp()
        y_axis = 0 #North - South
        x_axis = 0 #East - West

        """Mi-Ma's plot graph"""
    turtle.shape("triangle")
    turtle.color("red")
    y_axis = 0 #North - South
    x_axis = 0 #East - West
    coordinates = 0 # sqrt(x_axis^2 + y_axis^2)
    trial_lyst = []
    for trial in range(50):
        for step in range(100):
            direction = random.randint(1,4)
            if direction == 3: #East
                x_axis += 1
            elif direction == 4: #West
                x_axis -= 1

        turtle.goto(x_axis * 5,y_axis * 5)    
        turtle.stamp()
        y_axis = 0 #North - South
        x_axis = 0 #East - West
                        




def main():
    walk_lyst = []
    temp_lyst = argv[1].split(',')
    for walk in temp_lyst:
        walk_lyst.append(int(walk))     
    trial_count = int(argv[2])
    walker = argv[3]
    simulate(walk_lyst, trial_count, walker)
    plot()
if __name__ == "__main__":
    main()