"""
Cody Strange
CS1400-006
3/3/2022

Overall pretty simple project didn't run
into many troubles when programming. Not 
much to really note on it.

"""
def do_research(cages, adults, babies):
    '''calculates the number of months it will take before cages run out'''
    month = 1
    total = adults + babies

    with open("rabbits.csv", 'w') as research_csv:
        research_csv.write("# Table of rabbit pairs\n")
        research_csv.write("Month Adults Babies Total \n")
        while adults + babies < cages:
            '''every month every pair of adults produce a pair of babies
            and every non-newborn baby grows into an adult, total is then calculated and result is output
            into a csv table'''
            research_csv.write(str(month) + ", " + str(adults) + ", " + str(babies) + ", "+ str(total) + "\n")
            month += 1
            babies = adults
            adults = total
            total = adults + babies
        research_csv.write(str(month) + ", " + str(adults) + ", " + str(babies) + ", "+ str(total) + "\n")
        month += 1
        babies = adults
        adults = total
        total = adults + babies
        research_csv.write("# Cages will run out in month " + str(month - 1))

def main():
    do_research(500, 1, 0)

if __name__ == "__main__":
    main()