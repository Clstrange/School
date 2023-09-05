import statistics

def main():
    number_lyst = [3, 1, 7, 1, 4, 10]

    def mean(lyst):
        
        if lyst == []:
            return(0)
        else:
            return(sum(lyst)/len(lyst))
    
    def median(lyst_two):

        if lyst_two == []:
            return(0)
        else:
            return(len(lyst_two)/2 + 0.5)
    
    def mode(lyst_three):

        if lyst_three == []:
            return(0)
        else:
            return(statistics.mode(lyst_three))

    print("List:  ", number_lyst)
    print("Mode: ", mode(number_lyst))
    print("Median: ", median(number_lyst))
    print("Mean: ", mean(number_lyst))

if __name__ == '__main__':
    main()

