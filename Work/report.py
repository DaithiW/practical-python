# report.py
#
# Exercise 2.4
import csv


def read_portfolio(filename):
    "this is a some info"
    # assuming this is for prices when purchased...
    portfolio = []
    with open(filename, "rt") as f:
        rows = csv.reader(f)

        # each stock should be a dict, not tuple - keys - "name" "shares" "price"
        for row in rows:
            try:
                holding = {
                    "name": row[0],
                    "shares": int(row[1]),
                    "price": float(row[2]),
                }
                # return the portfolio list
                portfolio.append(holding)
            except ValueError:
                print("unable to parse file on line", row)

        return portfolio


def read_prices(filename):
    "some more info"
    # assume this is for current price

    price_dict = {}
    with open(filename, "rt") as f:
        rows = csv.reader(f)

        # assume headers

        for row in rows:
            try:
                price_dict[row[0]] = float(row[1])
            except IndexError:
                print("some error on row", row)

        return price_dict


def calc_diff(portfolio, prices):
    "calculates sum diff from purchase to current"
    # for name in i in portfolio...

    net = 0
    value = 0
    for i in range(len(portfolio)):
        name = portfolio[i]["name"]
        shares = int(portfolio[i]["shares"])
        price = float(portfolio[i]["price"])
        value += prices[name] * shares

        gain = (prices[name] * shares) - (price * shares)
        print(f"for {name} the net change is {gain}")
        net += gain
    return net, value


def make_report(portfolio, prices):
    "makes a report"
    # for name in i in portfolio...
    report = []

    for i in range(len(portfolio)):
        name = portfolio[i]["name"]
        shares = int(portfolio[i]["shares"])
        price = float(portfolio[i]["price"])

        # gain = (prices[name] * shares) - (price * shares)
        changes = prices[name] - price
        record = (name, shares, prices[name], changes)
        report.append(record)
    return report


def print_report(report):
    "prints nicely formatted report"
    headers = ("Name", "Shares", "Price", "Change")
    print(" ".join(f"{head:>10s}" for head in headers))
    print(" ".join("-" * 10 for _ in headers))
    for name, shares, price, change in report:
        price = "$" + f"{price:>.2f}"
        print(f"{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}")
