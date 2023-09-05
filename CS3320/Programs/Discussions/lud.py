import sympy 
from copy import deepcopy


def factor(A,n,pivot):
    A = deepcopy(A)
    pivot_point = -1
    pivot_row = 0
    i = 0
    for row in A:
        if row[0] > pivot_point:
            pivot_point = row[0]
            pivot_row = i
        i += 1
    temp = deepcopy(A[0])
    A[0] = A[pivot_row]
    A[pivot_row] = temp

    pivot.append((0, pivot_row))

    return A

def solve(A, n, pivot, b, x):
    A = deepcopy(A)
    L = []
    for i in range(n):
        L.append([])
        for j in range(n):
            L[i].append(0)
        L[i][i] = 1

    for i in range(1,n):
        for j in range(i):
            x = deepcopy(A[i][j])
            if (A[i - 1][j] == 0):
                y = A[0][j] #could have error
                chosen_row = 0
                R1 = deepcopy(A[chosen_row][j])
                R2 = deepcopy(A[i][j])
            else:
                y = deepcopy(A[i-1][j])
                chosen_row = i-1
                R1 = deepcopy(A[chosen_row][j])
                R2 = deepcopy(A[i][j])
            
            A[i][j] = (-(x/y) * R1 + R2)
            L[i][j] = x/y
            if (j+1 == n-j):
                R1 = deepcopy(A[chosen_row][k])
                R2 = deepcopy(A[i][k])
                A[i][k] = (-(x/y) * R1 + R2)
            for k in range(j+1, n-j):
                R1 = deepcopy(A[chosen_row][k])
                R2 = deepcopy(A[i][k])
                A[i][k] = (-(x/y) * R1 + R2)
        U = deepcopy(A)


    equation_lyst = []   
    for i in range(n):
        equation_lyst.append([])
        for j in range(i+1):
            equation_lyst[i].append((L[i][j], "x"+str(j+1)))
        equation_lyst[i].append(-b[i])

    variable_lyst = []

    for i in equation_lyst:
        z = 0
        for j in range(len(variable_lyst)):
            z += variable_lyst[j]*i[j][0]
        x = sympy.symbols(i[-2][1])
        y = sympy.solve(z + i[-2][0] *x + i[-1], x)
        variable_lyst.append(y[0])


    equation_lyst = []
    B2 = variable_lyst 
    variable_lyst2 = []
    n = 3 #temp
    for i in range(n):
        equation_lyst.append([])
        for j in range(i, n):
            equation_lyst[i].append((U[i][j], "x"+str(j+1)))
        equation_lyst[i].append(-B2[i])
    # print(equation_lyst)
    for i in range(len(equation_lyst)-1, -1,-1):
        z = 0
        for j in range(len(variable_lyst2)):
            z += variable_lyst2[j]*equation_lyst[i][j][0]
        x = sympy.symbols(equation_lyst[i][-2][1])
        y = sympy.solve(z + equation_lyst[i][-2][0] *x + equation_lyst[i][-1], x)
        # print(y)
        if len(y) == 0:
            # print("test")
            y.append(0)

        variable_lyst2.append(y[0])
    return(variable_lyst2)


def main():
    with open("File lu2.dat", 'r') as file:
        new_file = file.readlines()
        row_count = int(new_file.pop(0).strip())
        matrix = []
        for i in range(row_count):
            matrix.append([])
            next_file = new_file.pop(0).strip()
            coefficients = next_file.split(" ")
            for j in coefficients:
                matrix[i].append(int(j))

        A = matrix
        # print(A)
        # print([[2,1,-2],[4,-1,2],[2,-1,1]])
        n = row_count
        pivot = []
        A = factor(A,n,pivot)
        b_count = int(new_file.pop(0).strip())

        for i in range(b_count):
            b = new_file.pop(0).strip().split(" ")
            for j in range(len(b)):
                b[j] = int(b[j])

            x = []
            # print([5,1,2])
            print(b)
            # print(A)
            print(solve(A, n, pivot, b, x))
            # solve(A, n, pivot, b, x)


if __name__ == "__main__":
    main()