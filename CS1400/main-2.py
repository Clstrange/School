'''
Project Name: Stock Exchange Data
Author: Cody Strange
Due Date: 10/31/2020
Course: CS1400-X02

The program opens up the stock data file and splits the data up.
It then assigns the date and the monentary value to the appropriate
using dictionaries. The file then grabs the minimum, maximum, and
the average of each symbol and prints them out, along with the
overall minimum and maximum.

'''


def main():
    try:
        file = open(input("Enter the name of the stock data file:"), "r")
        file.read
        file.close

    except:
        print("File not Found")
        exit(0)

    # Create a dictionary to store data in
    # stock_data {
    #   symbol : {
    #       date : value,
    #       date : value
    #   }
    # }
    stock_data = {}
    first_line = False
    output = ""

    for line_of_data in file:
        # Toss the first line of data
        if not first_line:
            first_line = True
            continue

        # split the data into parts
        data = line_of_data.split(",")

        # see if we have handled this symbol before, if not, create a dictionary for the symbol
        try:
            stock_data[data[0]]
        except:
            stock_data[data[0]] = {}

        # assign the data to the symbol
        stock_data[data[0]][data[1]] = data[2].replace("\n", "")

    # Create some defaults for the overall stats
    overall_min = 9999999999999.0
    overall_max = 0.0
    overall_min_date = ""
    overall_max_date = ""
    overall_min_symbol = ""
    overall_max_symbol = ""

    for symbol, data in stock_data.items():
        # Create some defaults for the symbol stats
        symbol_min = 999999999999999.0
        symbol_max = 0.0
        max_date = ""
        min_date = ""
        avg = 0.0
        count = 0
        total = 0.0

        for date, value in data.items():
            if float(value) > overall_max:
                overall_max = float(value)
                overall_max_date = date
                overall_max_symbol = symbol

            if float(value) < overall_min:
                overall_min = float(value)
                overall_min_date = date
                overall_min_symbol = symbol

            if float(value) > symbol_max:
                symbol_max = float(value)
                max_date = date

            if float(value) < symbol_min:
                symbol_min = float(value)
                min_date = date

            count += 1
            total += float(value)

        avg = total/count

        output += symbol + ":\n"
        output += "Min: " + min_date + ": " + str(symbol_min) + "\n"
        output += "Max: " + max_date + ": " + str(symbol_max) + "\n"
        output += "Avg: " + str(avg) + "\n"
        output += "\n"

    output += "Lowest: " + overall_min_symbol + ": " + overall_min_date + " " + str(overall_min) +"\n"
    output += "Highest: " + overall_max_symbol + ": " + overall_max_date + " " + str(overall_max) + "\n"

    try:
        output_file = open(input("What is the name of the output file: "), "w")
        output_file.write(output)
        output_file.close

    except:
        print("Unable to open the file for writing")

    print(output)
if __name__ == "__main__":
    main()

