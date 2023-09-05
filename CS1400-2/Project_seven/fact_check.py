"""
Date: 4/23/2022
Name: Cody Strange
Project: Was Clinton right?

Summary: The project in a vacuum was very easy to do, just read in some files
and do some string/list manipulations. The real challenge is the using the information your
given to prove/disprove Clinton's claim. This is tricky because the data that you are handed
is not quite the same data that Clinton used. Your given the 'original data value'
while Clinton uses the 1-month net change. Or at least that was the only way
I could find data that even some what resembles his.
"""
def main():
    """is the main function"""
    with open("BLS_private.csv",'r') as file:
        #convert BLS data into a list and remove non-numeric lines
        file = file.readlines()
        file = file[6:]
        job_total = []

        #Combine monthly job counts into yearly job counts and
        #Put it into a list
        for line in file:
            job_sum = 0
            job_lyst = line.strip().split(',')
            job_lyst = job_lyst[1:]
            for job in job_lyst:
                if job.isnumeric():
                    job_sum += int(job)
            job_total.append(job_sum)

        democrat_jobs = 0
        republican_jobs = 0
        count = -1

        with open('presidents.txt', 'r') as file_two:
            file_two = file_two.readlines()
            file_two = file_two[1:]
            for president in file_two:
                affliation_years = president.strip().split(',')[1:]

                if affliation_years[0] == "Democratic":
                    for years in range(int(affliation_years[1])):
                        if years == "something":
                            print("nothing")
                        count += 1
                        democrat_jobs += job_total[count]
                else:
                    for years in range(int(affliation_years[1])):
                        count += 1
                        republican_jobs += job_total[count]

            result = f"""Republican jobs {republican_jobs * 1000}
Democrat jobs {democrat_jobs * 1000}

I came up with these totals by combining the monthly jobs from Republican
years and combining the monthly jobs from Democrat years, you have to multiply the results by 1000 because that's how they are given in the BLS.
And this data really proves nothing in regards to Clinton's specific claims. Because he claims JOBS CREATED and this data we were given is about 
JOBS TOTAL. So please view conclusion.md for a more detailed explanation on the matter. """
            print(result)
if __name__ == "__main__":
    main()
