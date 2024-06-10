# pcost.py
#
# Exercise 1.27
import csv
import sys
import report
import stock

def portfolio_cost(filename):
    "calculates portfolio cost from a csv"

    portfolio_dict = report.read_portfolio(filename)
    value = 0
    for d in portfolio_dict:
        value += d.shares * d.price

    # f = open(filename, "rt")
    # rows = csv.reader(f)
    # headers = next(rows)

    # shares = []
    # price = []
    # value = 0

    # for rowno, row in enumerate(rows, start=1):
    #     record = dict(zip(headers, row))
    #     try:
    #         shares.append(record["shares"])
    #         price.append(record["price"])
    #         value += int(shares[rowno-1]) * float(price[rowno-1])
    #     except ValueError:
    #         print(f"Row {rowno}: Bad row: {row}")
    # # print(f"shares {shares}")
    # print(f"price {price}")
    # for i in range(len(shares)):
    return value


# if len(sys.argv) == 2:
#     filename = sys.argv[1]
# else:
#     filename = "Data/portfolio.csv"

# cost = portfolio_cost(filename)


def main(argv):
    if len(argv) != 2:
        raise SystemExit(f"Usage: {argv[0]}" "portfile")
    portfile = argv[1]
    cost = portfolio_cost(portfile)
    print("Total cost ", cost)

if __name__ == "__main__":
    main(sys.argv)
