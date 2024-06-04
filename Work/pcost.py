# pcost.py
#
# Exercise 1.27
def portfolio_cost(filename):
    "calculates portfolio cost from a csv"
    f = open(filename, "rt")

    headers = next(f).split(",")
    shares = []
    price = []

    for line in f:
        try:
            shares.append(line.split(",")[1])
            price.append(line.split(",")[2])
        except ValueError:
            print("Could not parse file on line", line)

    value = 0
    for i in range(len(shares)):
        try:
            value += float(shares[i]) * float(price[i])
        except ValueError:
            print("Could not parse file on line", line)

    return value


cost = portfolio_cost("Data/missing.csv")
print("Total cost ", cost)
