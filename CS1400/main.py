'''
random walk
Cody L. Strange
12/5/2020
CS1400-X02

main.py

Usage:
main.py -l <[list_of_walk_lengths]> -t <number_of_trials> -w <Pa,Mi-Ma,Reg,All>
'''

import random as rnd
import statistics as stats
import math
import sys
import turtle as t
import getopt


def pa(trial_count, walk_dist):
    """calculate for pa"""
    
    #empty list
    dist_list = []
    max_c_list = []
    
    for x in range(trial_count):
        
        #starting position
        position = [0, 0]
        t.tracer(0,0)
        t.penup()
        z = x
        max_d = 0
        max_c = []
        
        
        #four different directions
        xy_cor = ["North", "South", "East", "West"]
        
        #randomly select a direction to move
        for y in range(walk_dist):
            z = y
            direction = rnd.choice(xy_cor)
            
            if direction == "North":
                position[1] += 1
                    
            elif direction == "South":
                position[1] -= 1
                
                
            elif direction == "East":
                position[0] += 1
                
            elif direction == "West":
                position[0] -= 1
                    
            else:
                print("Error! Direction non-existant")
            
            #measures distance of each list
            dist = math.dist([0, 0], position)
            dist_list.append(dist)
            if max_d < dist:
                max_d = dist
                max_c = position
                
        max_c_list.append(max_c)     
    
    z +=1
    if walk_dist == 100:
        for c in max_c_list:
            t.penup()
            t.goto(c[0]*10,c[1]*10)
            t.pendown()
            t.shape("circle")
            t.stamp()
            
    #max, min, mean, CV
    max_list = max(dist_list)
    min_list = min(dist_list)
    mean_list = stats.mean(dist_list)
    dev_list =stats.stdev(dist_list)
    cv_list = int(dev_list)/int(mean_list)
    
    #print formatting
    print("Pa random walk of", walk_dist, "steps")
    print("Mean = " + "{:.1f}".format(mean_list)
    + " CV = " + "{:.1f}".format(cv_list)
    + "\n"
    + "Max = " + "{:.1f}".format(max_list)
    + " Min = " + "{:.1f}".format(min_list))



def mima(trial_count, walk_dist):
    """calculate for mima"""
    #empty list
    dist_list = []
    
    for x in range(trial_count):
        
        #starting position
        position = [0, 0]
        z = x
        
        #four different directions, Mi-MA moves south more often
        xy_cor = ["North", "South", "East", "West", "South"]
        
        #randomly move in a direction
        for y in range(walk_dist):
            z = y
            direction = rnd.choice(xy_cor)
            
            if direction == "North":
                position[1] += 1
                    
            elif direction == "South":
                position[1] -= 1
                
                
            elif direction == "East":
                position[0] += 1
                
            elif direction == "West":
                position[0] -= 1
                    
            else:
                print("Error! Direction non-existant")
                
        #distance between lists
        dist = math.dist([0, 0], position)
        dist_list.append(dist)
        
    z += 1
    #max, min, mean, CV
    max_list = max(dist_list)
    min_list = min(dist_list)
    mean_list = stats.mean(dist_list)
    dev_list =stats.stdev(dist_list)
    cv_list = int(dev_list)/int(mean_list)
    
    #print format
    print("Mi-Ma random walk of", walk_dist, "steps")
    print("Mean = " + "{:.1f}".format(mean_list)
    + " CV = " + "{:.1f}".format(cv_list)
    + "\n"
    + "Max = " + "{:.1f}".format(max_list)
    + " Min = " + "{:.1f}".format(min_list))
        

def reg(trial_count, walk_dist):
    """calculate for reg"""
    #empty list
    dist_list = []
    
    for x in range(trial_count):
        
        #starting position
        position = [0, 0]
        z = x
        
        #two different directions
        xy_cor = ["East", "West"]
        
        #randomly move in a direction
        for y in range(walk_dist):
            z = y
            direction = rnd.choice(xy_cor)
            
            if direction == "East":
                position[0] += 1
                
            elif direction == "West":
                position[0] -= 1
                    
            else:
                print("Error! Direction non-existant")
        
        #distance between list
        dist = math.dist([0, 0], position)
        dist_list.append(dist)
    
    z += 1
    #max, min, mean, CV
    max_list = max(dist_list)
    min_list = min(dist_list)
    mean_list = stats.mean(dist_list)
    dev_list =stats.stdev(dist_list)
    cv_list = int(dev_list)/int(mean_list)
    
    #print format
    print("Reg random walk of", walk_dist, "steps")
    print("Mean = " + "{:.1f}".format(mean_list)
    + " CV = " + "{:.1f}".format(cv_list)
    + "\n"
    + "Max = " + "{:.1f}".format(max_list)
    + " Min = " + "{:.1f}".format(min_list)) 
  
#program starts here
def main(argv):
    """The main function of the application"""
    error_message = (
        "main.py "
        + "-l <[list_of_walk_lengths]> "
        + "-t <number_of_trials> "
        + "-w <Pa,Mi-Ma,Reg,All>"
    )
    lengths = []
    trials = 0
    who = ""

    try:
        opts, args = getopt.getopt(argv, "hl:t:w:", ["lengths=",
                                                    "trials=", "who="])
        args.append(2)
    except getopt.GetoptError:
        print(error_message)
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print(error_message)
            sys.exit()

        if opt in ("-l", "--lengths"):
            l = arg.strip("][").split(",")
            for v in l:
                lengths.append(int(v))
        elif opt in ("-t", "--trials"):
            trials = int(arg)
        elif opt in ("-w", "--who"):
            who = arg

    if who == "All":
        for l in lengths:
            pa(trials, l)
        for l in lengths:
            mima(trials, l)
        for l in lengths:
            reg(trials, l)
    elif who == "Pa":
        for l in lengths:
            pa(trials, l)
    elif who == "Mi-Ma":
        for l in lengths:
            mima(trials, l)
    elif who == "Reg":
        for l in lengths:
            reg(trials, l)
    else:
        print(error_message)


    
    
if __name__ == "__main__":
    main(sys.argv[1:])
                
                
                
        
            
            






