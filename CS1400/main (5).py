'''
Was Clinton right?
Cody L. Strange
12/16/2020
CS1400-X02

main.py

Usage:
Program proves that Bill Clinton was wrong, it gives the
following information: president affiliation count,
total affiliation years served, and total affiliated jobs.
The program also provides the optional information of the
following raw informatoin: affilated presidents with years
served and jobs created per year, list of job totals
per year, and overall employment total. Enough information
is given that if user doesn't agree with results they can
double check with the raw data given.

Bonus Question:
Now to answer the question given and to better prove as to why
Clinton was wrong off of the data given. The biggest flaw
with the data given is the "seasonally adjusted". This causes
any outlying data to be removed. If a president did any job
creation in on of these "seasonal" times it wouldn't be
created. That is the major reason that the numbers are so
close. The republicans are bound to create more job off of
averages because they have served four more years. Though
this does not prove that Clinton was actually correct, it
does show how he COULD be right. Though for him to be right
there would have to be massive fluctuations in employment.
To create a nearly twenty million job gap that was erased by
seasonal adjustment there would have to be extremely
unreasonbly amounts of temporary jobs.
'''

def main():
    """main function that runs program"""



    # global lists
    total_employees = []
    democratic_proof = []
    democrat_jobs_created = []
    republican_jobs_created = []
    republican_proof = []
    employment = []
    sum_employment = []
    with open("BLS_private.csv", "r") as BLS_file: 
        for file in BLS_file.readlines()[6:]:
            
            #removes /n and splits list by commas
            new_file = file.strip().split(',')
            employment.append(new_file)
            #turning list into integar
            new_list = []
            for i in new_file[1:]:
                try:
                    new_list.append(int(i))
                except:
                    pass
            
            #changing list numbers by year rather than by month
            sum_list = sum(new_list)
            
            #global sum_list
            total_employees.append(sum_list)
            sum_employment.append(sum_list)
            
            
            
            
            
            

    with open("Presidents.txt", "r") as presidents:
    
        #Variables for presidents and the years they served
        democratic_president_count = 0
        republican_president_count = 0
        total_dem_years = 0
        total_rep_years = 0
        
        #creates lists that combine democratic/republican totals separately
        for presidents_file in presidents.readlines()[1:]:
            
            #removing /n from list and seperating by commas
            x = presidents_file.strip().split(',')
            
            #seperates info by affiliation
            for president_affiliation in x[1:2]:
                
                #democrat affiliation
                if president_affiliation == "Democratic":
                    
                    democratic_proof.append(presidents_file.strip().split(',')[0:2])
                    
                    #totals democratic presidents
                    democratic_president_count += 1
                    
                    #slices years served by democrats from list to use
                    democrat_years = x[2:3]
                    for x in democrat_years[0:]:
                        
                        #totals years served by democratic presidents
                        dem_years = int(x)
                        total_dem_years += dem_years
                        
                        #totals jobs created by democrats
                        for jobs in range(dem_years):
                            
                            for t in total_employees[0:1]:
                                democratic_proof.append(t)
                                try:
                                    democrat_jobs_created.append(int(t))
                                except:
                                    pass
                                
                                #removes numbers already added to the list from said list
                                total_employees.pop(0)
                
                #republican affiliation 
                elif president_affiliation == "Republican":
                    
                    republican_proof.append(presidents_file.strip().split(',')[0:2])
                    
                    #totals republican presidents
                    republican_president_count += 1
                    
                    #slices years served by republicans from list to use
                    republican_years = x[2:3]
                    for m in republican_years[0:]:
                        
                        #totals years served by republican presidents
                        rep_years = int(m)
                        total_rep_years += rep_years
                        
                        #totals jobs created by republicans
                        for z in range(rep_years):
                            for p in total_employees[0:1]:
                                republican_proof.append(p)
                                try:
                                    republican_jobs_created.append(int(p))      
                                except:
                                    pass
                                
                                #removes numbers already added to the list from said list
                                total_employees.pop(0)
                
                #just in case something fails
                else:
                    print("ERROR!!!")
           
        #visual code   
        if sum(republican_jobs_created) > sum(democrat_jobs_created):
            answer = "No!"
        else:
            answer = "Yes!"
        print("Democratic presidents count:", democratic_president_count)
        print("Republican presidents count:", republican_president_count)
        print("Total Democratic years served:", total_dem_years)
        print("Total Republican years served:", total_rep_years)
        print("Total Democratic jobs created:", sum(democrat_jobs_created))
        print("Total Republican jobs created:", sum(republican_jobs_created))
        print("Was Clinton right:", answer)
        
        
        dem_proof = input("Would you like to view the Democratic info? (yes or no)")
        if dem_proof == "yes":
            """Provides raw info on presidents, their affiliation, and years served"""
            print(democratic_proof)
            print("\n", "THE INFO GIVES: PRESIDENT NAME, AFFILIATION, TOTAL JOBS CREATED IN YEARS SERVED")
        else:
            pass
        
        rep_proof = input("Would you like to view the Republican info? (yes or no)")
        if rep_proof == "yes":
            """Provides raw info on presidents, their affiliation, and years served"""
            print(republican_proof)
            print("\n", "THE INFO GIVES: PRESIDENT NAME, AFFILIATION, TOTAL JOBS CREATED IN YEARS SERVED")
        else:
            pass
        
        job_proof = input("Would you like to see individual total employment for each year? (yes or no)")
        if job_proof == "yes":
            """Provides raw info on employment created for each year"""
            print(employment)
        else:
            pass
        
        job_totals = input("Would you like to see the total employment for all years combined? (yes or no)")
        if job_totals == "yes":
            """Provides info on total employment"""
            print(sum(sum_employment))
        else:
            pass
        
if __name__ == "__main__":
    main()

        
        

