# pcost.py
#
# Exercise 1.27
import csv
import sys

def portfolio_cost(filename):
    "calculates portfolio cost from a csv"
    f = open(filename, "rt")
    rows = csv.reader(f)
    headers = next(rows)

    shares = []
    price = []

    for rowno, row in enumerate(rows, start=1):
        try:
            shares.append(row[1])
            price.append(row[2])
        except ValueError:
            print(f"Row {rowno}: Bad row: {row}")
    print(f"shares {shares}")
    print(f"price {price}")
    value = 0
    for i in range(len(shares)):
        try:
            value += int(shares[i]) * float(price[i])
        except ValueError:
            print(f"Row {rowno}: Bad row: {row}")

    return value

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = "Data/portfolio.csv"
    
cost = portfolio_cost(filename)
print("Total cost ", cost)
