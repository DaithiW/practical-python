# report.py
#
# Exercise 2.4
import csv
import fileparse
import sys
import stock
import tableformat


def read_portfolio(filename, **opts):
    "this is a some info"
    # assuming this is for prices when purchased...
    # portfolio = []
    with open(filename, "rt") as f:
        portdicts = fileparse.parse_csv(
            f, select=["name", "shares", "price"], types=[str, int, float], **opts
        )

    # with open(filename, "rt") as f:
    #     rows = csv.reader(f)
    #     headers = next(rows)
    #     # each stock should be a dict, not tuple - keys - "name" "shares" "price"
    #     for i, row in enumerate(rows):
    #         try:
    #             holding = {
    #                 "name": row[0],
    #                 "shares": int(row[1]),
    #                 "price": float(row[2]),
    #             }
    #             # return the portfolio list
    #             portfolio.append(holding)
    #         except ValueError:
    #             print("unable to parse file on line", i)

    portfolio = [stock.Stock(**d) for d in portdicts]
    return portfolio


def read_prices(filename):
    "some more info"
    # assume this is for current price
    with open(filename, "rt") as f:
        price_tup = fileparse.parse_csv(f, types=[str, float], has_headers=False)
    # this is a list of tuples (name, price (str))
    # price_dict = {}
    # with open(filename, "rt") as f:
    #     rows = csv.reader(f)

    #     # assume headers

    #     for row in rows:
    #         try:
    #             price_dict[row[0]] = float(row[1])
    #         except IndexError:
    #             print("some error on row", row)
    price_dict = {name: price for name, price in price_tup}
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
        name = portfolio[i].name  # ["name"]
        shares = int(portfolio[i].shares)  # ["shares"])
        price = float(portfolio[i].price)  # ["price"])

        # gain = (prices[name] * shares) - (price * shares)
        changes = prices[name] - price
        record = (name, shares, prices[name], changes)
        report.append(record)
    return report


def print_report(reportdata, formatter):
    """
    Make a stock report given portfolio and price data files.
    """
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f"{price:0.2f}", f"{change:0.2f}"]
        formatter.row(rowdata)

    # headers = ("Name", "Shares", "Price", "Change")
    # print(" ".join(f"{head:>10s}" for head in headers))
    # print(" ".join("-" * 10 for _ in headers))
    # for name, shares, price, change in report:
    #     price = "$" + f"{price:>.2f}"
    #     print(f"{name:>10s} {shares:>10d} {price:>10s} {change:>10.2f}")


def portfolio_report(portfoliofile, pricefile, fmt="txt"):
    """
    Make a stock report fiven portfolio and price data files.
    """
    # Read data files
    portfolio = read_portfolio(portfoliofile)
    prices = read_prices(pricefile)

    # Create the report data
    report = make_report(
        portfolio, prices
    )  # In the tutorial this is called make_report_data

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

    # pf = read_portfolio(portfolio)
    # pr = read_prices(prices)

    # rp = make_report(pf, pr)
    # print_report(rp)


def main():
    if len(sys.argv) != 4:
        raise SystemExit(f"Usage: {sys.argv[0]} " "portfile pricefile format")
    portfile = sys.argv[1]
    pricefile = sys.argv[2]
    fmt = sys.argv[3]
    portfolio_report(portfile, pricefile, fmt)


if __name__ == "__main__":
    main()
