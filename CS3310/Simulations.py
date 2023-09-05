import MergeSort
import QuickSort
import time
import random

def elo_sim(sort_func, basic_ops_func, reset_ops_func, quantity = 2**10):
    """Sort a group of 2^20 gamers by their elo
    50% of the players elo is 1000-2400
    30% of the players elo is 2401-2700
    15% of the players elo is 2701-2900 
    05% of the players elo is 2901-3000"""

    lyst = []
    low_elo = int(quantity * 0.50)
    mid_elo = int(quantity * 0.30)
    high_elo = int(quantity * 0.15)
    pro_elo = int(quantity * 0.05)

    for i in range(low_elo):
        lyst.append(random.randint(1000, 2400))
    for i in range(mid_elo):
        lyst.append(random.randint(2401, 2700))
    for i in range(high_elo):
        lyst.append(random.randint(2701, 2900))
    for i in range(pro_elo):
        lyst.append(random.randint(2901, 3000))

    random.shuffle(lyst)
    start = time.perf_counter()
    sort_func(lyst)
    end = time.perf_counter()
    basic_ops = basic_ops_func()
    reset_ops_func()


    return (end-start, basic_ops)

def manufacturer_sim(sort_func, basic_ops_func, reset_ops_func, quantity = 2**10):
    """Sort a group of 2^10 manufacturer employees by their pay
    90% of the employees are basic workers who make $30000-$40000 varience is dependent on bonuses and overtime
    10% of employees are managers who make $60000-$80000"""
    lyst = []
    basic_worker = int(quantity * 0.90)
    manager = int(quantity * 0.10)

    for i in range(basic_worker):
        lyst.append(random.randint(30000, 40000))
    for i in range(manager):
        lyst.append(random.randint(60000, 80000))

    random.shuffle(lyst)
    start = time.perf_counter()
    sort_func(lyst)
    end = time.perf_counter()  
    basic_ops = basic_ops_func()
    reset_ops_func()
    return (end-start, basic_ops)

def highschool_sim(sort_func, basic_ops_func, reset_ops_func, quantity = 2**10):
    """Sort a group of 2^15 highschool students by their age
    25% of students are 15
    25% of students are 16
    25% of students are 17
    25% of students are 18"""
    lyst = []
    students = int(quantity * 0.25)

    for i in range(students):
        lyst.append(15)
    for i in range(students):
        lyst.append(16)
    for i in range(students):
        lyst.append(17)
    for i in range(students):
        lyst.append(18)
    random.shuffle(lyst)
    start = time.perf_counter()
    sort_func(lyst)
    end = time.perf_counter()
    basic_ops = basic_ops_func()
    reset_ops_func()
    return (end-start, basic_ops)

def workorder_employee_sim(sort_func, basic_ops_func, reset_ops_func, quantity = 2**20):
    """Sort a group of 2^20 service work orders by the employee who created the work order
    100% of work orders between 00000000 - 99999999"""
    lyst = []

    for i in range(quantity):
        lyst.append(random.randint(0,99999999))

    random.shuffle(lyst)
    start = time.perf_counter()
    sort_func(lyst)
    end = time.perf_counter()
    basic_ops = basic_ops_func()
    reset_ops_func()
    

    return (end-start, basic_ops)

def sim_print(function_name, sort_type, run_times, basic_ops):
    """Prints out a formatted table of the simulation data
    arguments:
        - function_name
        - sort_type
        - list of run times
        - list of basic ops"""
    run_sum = 0
    op_sum = 0
    print("-"*30)
    x=""
    print(f"{function_name} {sort_type}")
    print("\tRun Times:")
    for i in range(len(run_times)):
        run_sum += run_times[i]
        print(f"\t\t({i+1}) {run_times[i]}")
    run_average = run_sum/len(run_times)
    print("\t Op Counts:")
    for i in range(len(basic_ops)):
        op_sum += basic_ops[i]
        print(f"\t\t({i+1}) {basic_ops[i]}")
    op_average = op_sum / len(basic_ops)
    print("\n")

    print(f"Average Run Time = {run_average}")
    print(f"Average Number of Basic Operations = {op_average}")
    
def main():
    run_times = []
    basic_ops = []

    """Elo Simulation"""
    for i in range(10):
        
        info = elo_sim(MergeSort.mergeSort, MergeSort.basicOps, MergeSort.reset)
        run_times.append(info[0])
        basic_ops.append(info[1])
    sim_print("elo_sim", "merge_sort", run_times, basic_ops)
    run_times.clear()
    basic_ops.clear()

    for i in range(10):
        info = elo_sim(QuickSort.quickSort, QuickSort.basicOps, QuickSort.reset)
        run_times.append(info[0])
        basic_ops.append(info[1])
    sim_print("elo_sim", "quick_sort", run_times, basic_ops)
    run_times.clear()
    basic_ops.clear()

    """Manufacturer Simulation"""
    for i in range(10):
        
        info = manufacturer_sim(MergeSort.mergeSort, MergeSort.basicOps, MergeSort.reset)
        run_times.append(info[0])
        basic_ops.append(info[1])
    sim_print("manufacturer_sim", "merge_sort", run_times, basic_ops)
    run_times.clear()
    basic_ops.clear()

    for i in range(10):
        
        info = manufacturer_sim(QuickSort.quickSort, QuickSort.basicOps, QuickSort.reset)
        run_times.append(info[0])
        basic_ops.append(info[1])
    sim_print("manufacturer_sim", "quick_sort", run_times, basic_ops)
    run_times.clear()
    basic_ops.clear()

    """Highschool Simulation"""
    for i in range(10):
        
        info = highschool_sim(MergeSort.mergeSort, MergeSort.basicOps, MergeSort.reset)
        run_times.append(info[0])
        basic_ops.append(info[1])
    sim_print("highschool_sim", "merge_sort", run_times, basic_ops)
    run_times.clear()
    basic_ops.clear()

    for i in range(10):
        print("Loading...")
        info = highschool_sim(QuickSort.quickSort, QuickSort.basicOps, QuickSort.reset)
        run_times.append(info[0])
        basic_ops.append(info[1])
    sim_print("highschool_sim", "quick_sort", run_times, basic_ops)
    run_times.clear()
    basic_ops.clear()

    """Workorder Employee Simulation"""
    for i in range(10):   
        info = workorder_employee_sim(MergeSort.mergeSort, MergeSort.basicOps, MergeSort.reset)
        run_times.append(info[0])
        basic_ops.append(info[1])
    sim_print("workorder_employee_sim", "merge_sort", run_times, basic_ops)
    run_times.clear()
    basic_ops.clear()

    for i in range(10):
        info = workorder_employee_sim(QuickSort.quickSort, QuickSort.basicOps, QuickSort.reset)
        run_times.append(info[0])
        basic_ops.append(info[1])
    sim_print("workorder_employee_sim", "quick_sort", run_times, basic_ops)
if __name__ == "__main__":
    main()
