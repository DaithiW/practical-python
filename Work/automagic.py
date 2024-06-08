import csv
import pprint

def main():
    # names str shares int price float
    # Data/portfolio.csv
    types = [str, int, float]
    filename = "Data/portfolio.csv"
    with open(filename, "rt") as f:
        rows = csv.reader(f)

        headers = next(rows)
        original = headers
        # [ name, shares, price ]
        portfolio = [{name: func(val) for name, func, val in zip(headers, types, row)} for row in rows ]

    pprint.pprint(portfolio)


if __name__ == "__main__":
    main()
