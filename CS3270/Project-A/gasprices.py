
import re

def calculate_low_price(year_report):
    """Calculates low price per year by comparing the lowest price of each month"""
    low_price = 100000.00
    for month in year_report.values():
        price = month[0]
        if price <= low_price:
            low_price = price
    return format(low_price, '.2f')

def calculate_high_price(year_report):
    """Calculates high price per year by comparing the highest price of each month"""
    high_price = 0
    for month in year_report.values():
        price = month[-1]
        if price >= high_price:
            high_price = price
    return format(high_price, '.2f')

def calculate_avg_price(year_report):
    """Calculates average price per year"""
    price_count = 0
    price_total = 0
    for month in year_report.values():
        price_count  += len(month)
        price_total += sum(month)
    return format(price_total / price_count, '.2f')

def calculate_monthly_prices(year_report):
    """Calculates the average for each month of a given year"""
    monthly_prices = {}
    for month in year_report:
        monthly_prices[month] = format(sum(year_report[month]) / len(year_report[month]), '.2f')
    return monthly_prices

def main():
    """takes the text file and turns it into a list of
    lines and parses the year, month, and price from each line"""
    gas_report = {}
    
    with open("gas_prices.txt", 'r') as raw_text:
        raw_text = raw_text.readlines()
        for line in raw_text:
            clean_text = line.strip()
            parsed_text = re.split('-|:', clean_text)
            year = parsed_text[2]
            month = parsed_text[0]
            price = parsed_text[3]

            if year not in gas_report.keys(): # gas_report{year:{month:[price, price]}}
                gas_report[year] = {}
                year_report = gas_report[year]
                year_report[month] = []
                price_report = year_report[month]
                price_report.append(float(price))
            elif month not in year_report.keys():
                year_report[month] = []
                price_report = year_report[month]
                price_report.append(float(price))
            else:
                price_report.append(float(price))
            price_report.sort()

        for year in gas_report:
            low_price = calculate_low_price(gas_report[year])
            high_price = calculate_high_price(gas_report[year])
            avg_price = calculate_avg_price(gas_report[year])
            monthly_prices = calculate_monthly_prices(gas_report[year])
            print(f"""{year}:
                Low: ${low_price}, Avg: ${avg_price}, High: ${high_price}
                January     ${monthly_prices['01']}
                February    ${monthly_prices['02']}
                March       ${monthly_prices['03']}
                April       ${monthly_prices['04']}
                May         ${monthly_prices['05']}
                June        ${monthly_prices['06']}
                July        ${monthly_prices['07']}
                August      ${monthly_prices['08']}
                September   ${monthly_prices['09']}
                October     ${monthly_prices['10']}
                November    ${monthly_prices['11']}
                December    ${monthly_prices['12']}

            """)
if __name__ == "__main__":
    main()