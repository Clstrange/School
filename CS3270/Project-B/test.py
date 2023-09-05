from collections import namedtuple

Parts_table = namedtuple("Parts", "pno pname color weight pcity")
Suppliers_table = namedtuple("Suppliers", "sno sname status scity")
Spjs_table = namedtuple("Spjs", "ssno spno sjno qty")


with open("parts.txt") as parts, open("projects.txt") as projects, open("spj.txt") as spjs, open("suppliers.txt") as suppliers:
    parts = parts.readlines()
    parts = [word.strip().split(",") for word in parts]
    parts = parts[2:]
    pno = [data[0] for data in parts]
    pname = [data[1] for data in parts]
    color = [data[2] for data in parts]
    weight = [data[3] for data in parts]
    pcity = [data[4] for data in parts]
    parts_table = [Parts_table(part[0], part[1], part[2], part[3], part[4]) for part in parts]


    suppliers = suppliers.readlines()
    suppliers = [word.strip().split(",") for word in suppliers]
    suppliers = suppliers[2:]
    sno = [data[0] for data in suppliers]
    sname = [data[1] for data in suppliers]
    status = [data[2] for data in suppliers]
    scity = [data[3] for data in suppliers]
    suppliers_table = [Suppliers_table(supplier[0], supplier[1], supplier[2], supplier[3]) for supplier in suppliers]

    spjs = spjs.readlines()
    spjs = [word.strip().split(",") for word in spjs]
    spjs = spjs[2:]
    ssno = [data[0] for data in spjs]
    spno = [data[1] for data in spjs]
    jpno = [data[2] for data in spjs]
    qty = [data[3] for data in spjs]
    spjs_table = [Spjs_table(spj[0], spj[1], spj[2], spj[3]) for spj in spjs]




    database = {"Parts": parts_table, "Suppliers": suppliers_table, "Spjs": spjs_table}

    query_one = {supplier.sname for supplier in database.get("Suppliers") for spj in database.get("Spjs") if spj.spno == "p2" and spj.ssno == supplier.sno}
    query_six = {supplier.scity: [x.sname for x in database.get("Suppliers") if x.scity == supplier.scity] for supplier in database.get("Suppliers")}
    print(query_six)

