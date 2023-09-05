"""
    Cody Strange
    9/13/2022
    CS3270-001
    Programming project B

    Summary:
        This program should read in a text file and 
        print out to another text file the amount of each words that 
        appear in the text. The printed text file should be sorted in 
        descending order by the quanity of words in the text.

    Version 0.1 --- 9/18/2022
        pre-session summary: Version 0.1 will simply be design, starting
                        high level design will consist of code comments
                        describing major functionalities of the code. 
                        Low level design will consist of Lucid chart 
                        diagram.
        post-session summary: Both high-level and low-level design have been completed
                        took longer than expected because I ended up having to change
                        the structure of my design but that is why we do design.

    Version 1.0 --- 9/20/2022
        pre-session summary: I am beginning actual programming, I am
                        confident this should be reletivily fast
        post-session summary: Overall time to write the program was roughly
                        an hour. The queries were by far the most time consuming parts
                        and that was only because I misunderstood how three of them would work.
                        The answer always ended up being nesting addional list comprehensions
                        although this did lead me to create ridiculously large lines of code. Not
                        something I would do to the extremity I did unless it was for this specific
                        project.

    Bugs:
        - none found

    Required features:
        - none remaining

    Recomended features
        - The queries don't return data in the same order that the 
        project has them returning them. Not a big deal but still a little
        annoying 
"""
from collections import namedtuple
def main():
    Parts_table = namedtuple("Parts", "pno pname color weight p")
    Projects_table = namedtuple("Projects", "jno jname jcity")
    Spjs_table = namedtuple("Spj", "ssno spno sjno qty")
    Suppliers_table = namedtuple("Supplers", "sno sname status scity")
    with open("parts.txt") as parts, open("projects.txt") as projects, open("spj.txt") as spjs, open("suppliers.txt") as suppliers:
        #creating the parts table
        parts = parts.readlines()
        parts = [word.strip().split(",") for word in parts]
        parts = parts[2:]
        parts_table = [Parts_table(part[0], part[1], part[2], part[3], part[4]) for part in parts]
        #creating the parts table
        projects = projects.readlines()
        projects = [word.strip().split(",") for word in projects]
        projects = projects[2:]
        projects_table = [Projects_table(project[0], project[1], project[2]) for project in projects]
        #creating the parts table
        spjs = spjs.readlines()
        spjs = [word.strip().split(",") for word in spjs]
        spjs = spjs[2:]
        spjs_table = [Spjs_table(spj[0], spj[1], spj[2], spj[3]) for spj in spjs]
        #creating the parts table
        suppliers = suppliers.readlines()
        suppliers = [word.strip().split(",") for word in suppliers]
        suppliers = suppliers[2:]
        suppliers_table = [Suppliers_table(supplier[0], supplier[1], supplier[2], supplier[3]) for supplier in suppliers]
        #combining tables to create database
        database = {"Parts": parts_table, "Suppliers": suppliers_table, "Projects": projects_table, "Spjs": spjs_table}
        #creating query requests
        query_one = {supplier.sname for supplier in database.get("Suppliers") for spj in database.get("Spjs") if spj.spno == "p2" and spj.ssno == supplier.sno}
        query_two = {supplier.sname for supplier in database.get("Suppliers") for spj in database.get("Spjs") if (spj.spno == "p3" or spj.spno == "p5") and spj.ssno == supplier.sno}
        query_three = {supplier.sname for supplier in database.get("Suppliers") if (supplier.sname not in [sup.sname for sup in database.get("Suppliers") for spj in database.get("Spjs") if (spj.sjno == "j3" or spj.sjno == "j4") and spj.ssno == sup.sno])}
        query_four = {(part.color, part.pname) for part in database.get("Parts") if (part.color, part.pname) not in [(pt.color, pt.pname) for pt in database.get("Parts") for spj in database.get("Spjs") if spj.sjno == "j6" and spj.spno == pt.pno]}
        query_five = { item for item in [(supplier_one.sname, supplier_two.sname) for supplier_one in database.get("Suppliers") for supplier_two in database.get("Suppliers") if (supplier_one.sno != supplier_two.sno) and (supplier_one.scity == supplier_two.scity)] if item[0] > item[1]}
        query_six = {supplier.scity: [x.sname for x in database.get("Suppliers") if x.scity == supplier.scity] for supplier in database.get("Suppliers")}
        #printing query results
        print(query_one)
        print(query_two)
        print(query_three)
        print(query_four)
        print(query_five)
        print(query_six)
if __name__ == "__main__":
    main()