import csv
import matplotlib.pyplot as plt

FILE_NAME = "portfolio.csv"


def portfolio_pie_chart():
    labels = []
    values = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            ticker = row[0]
            shares = float(row[1])
            buy_price = float(row[2])

            value = shares * buy_price

            labels.append(ticker)
            values.append(value)

    if not values:
        print("Portfolio is empty.")
        return

    plt.figure(figsize=(7, 7))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.title("Portfolio Allocation")
    plt.show()