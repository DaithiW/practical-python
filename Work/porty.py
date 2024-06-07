import csv


def main():
    f = open("Data/portfoliodate.csv")
    rows = csv.reader(f)
    headers = next(rows)

    want = ["name", "shares", "price"]
    indices = [headers.index(colname) for colname in want]
    # index method (list) returns the position of the first occurrence
    row = next(rows)
    record = {colname: row[index] for colname, index in zip(want, indices)}

    print(f"record = {record}")

    portfolio = [
        {colname: row[index] for colname, index in zip(want, indices)} for row in rows
    ]

    print(f"portfolio = {portfolio}")


if __name__ == "__main__":
    main()
