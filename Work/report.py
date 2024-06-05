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
        headers = next(rows)
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
    names = []

    net = 0
    value = 0
    print(portfolio)
    for i in range(len(portfolio)):
        name = portfolio[i]["name"]
        shares = int(portfolio[i]["shares"])
        price = float(portfolio[i]["price"])
        value += prices[name] * shares
        
        gain = (prices[name] * shares) - (price * shares)
        print(f"for {name} the net change is {gain}")
        net += gain
    return net, value
