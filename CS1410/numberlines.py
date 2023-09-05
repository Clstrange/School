file = input("Enter input file name: ")
file_two = input("Enter file name: ")
file_one = open(file, 'r')
i = 0
with open(file_two, 'w') as file_two:
    for x in file_one.readlines():
        i += 1
        file_two.write('{}>{:>{}}'.format(i, x, len(x) + 1))


