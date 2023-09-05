'''
Project Name: Rabbits, Rabbits, Rabbits
Author: Bianca Ruiz
Due Date: 10/03/2020
Course: CS1400-X02

This program takes a single pair of adult
Rabbits and has them reproduce each month.
After a month the babies that the adults had will turn into adults.
And the next month all the adults will have a pair of babies again.
This will repeat until all 500 of the cages are filled.
'''

cages = 500 
month = 0
adults = 1
teens = 0
babies = 0
totalPairs = adults + babies
print("# Table of rabbit pairs")
print("%4s,%10s,%10s,%10s" % \
          ("month", "adults", "babies", "total"))
while totalPairs < cages:  #Formula for creating total number of Rabbits
    month += 1
    adults += teens  #Turning teens into adults
    teens = 0 
    teens += babies  #Turning babies into teens
    totalPairs = (adults + babies)
    print("%4s,%10s,%10s,%10s" % \
          (month, adults, babies, totalPairs))
    babies = adults #Adults having babies
    
print("# Cages will run out in month", month)