import csv
import os
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime


FILE_NAME = "portfolio.csv"


def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Ticker", "Shares", "Buy Price", "Purchase Date"])

def add_stock():
    purchase_date = datetime.now().strftime("%d/%m/%Y")
    ticker = input("Ticker: ").upper()

    try:
        shares = float(input("Number of shares: "))
        buy_price = float(input("Buy price: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([ticker, shares, buy_price, purchase_date])

    print(f"{ticker} added successfully.")


def show_portfolio():
    
    total_cost = 0
    total_value = 0

    print("\nPortfolio\n")

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:

            ticker = row[0]
            shares = float(row[1])
            buy_price = float(row[2])
            purchase_date = row[3]
            stock = yf.Ticker(ticker)

            try:
                current_price = stock.info["currentPrice"]
            except Exception:
                current_price = 0

            invested = shares * buy_price
            current_value = shares * current_price
            profit = current_value - invested

            if invested > 0:
                profit_percent = (profit / invested) * 100
            else:
                profit_percent = 0

            total_cost += invested
            total_value += current_value

            print(f"Ticker: {ticker}")
            print(f"Shares: {shares}")
            print(f"Buy Price: ${buy_price:.2f}")
            print(f"Purchase Date: {purchase_date}")
            print(f"Current Price: ${current_price:.2f}")
            print(f"Current Value: ${current_value:.2f}")
            print(f"Profit/Loss: ${profit:.2f} ({profit_percent:.2f}%)")
            print()
    total_profit = total_value - total_cost

    if total_cost > 0:
        total_percent = (total_profit / total_cost) * 100
    else:
        total_percent = 0

    print("Summary")
    print(f"Invested: ${total_cost:.2f}")
    print(f"Current Value: ${total_value:.2f}")
    print(f"Total Profit: ${total_profit:.2f}")
    print(f"Return: {total_percent:.2f}%")

def delete_stock():

    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)

        header = next(reader)

        for row in reader:
            rows.append(row)

    if not rows:
        print("Your portfolio is empty.")
        return

    print("\nPortfolio\n")

    for i, row in enumerate(rows, start=1):

        ticker = row[0]
        shares = float(row[1])
        buy_price = float(row[2])

        stock = yf.Ticker(ticker)

        try:
            current_price = stock.info["currentPrice"]
        except Exception:
            current_price = 0

        invested = shares * buy_price
        current_value = shares * current_price
        profit = current_value - invested

        if invested > 0:
            profit_percent = (profit / invested) * 100
        else:
            profit_percent = 0

        print(
            f"{i}. {ticker} | "
            f"{shares:.0f} shares | "
            f"${current_price:.2f} | "
            f"{profit_percent:.2f}%"
        )

    try:
        choice = int(input("\nSelect stock to delete: "))
    except ValueError:
        print("Invalid input.")
        return

    if choice < 1 or choice > len(rows):
        print("Invalid selection.")
        return

    deleted = rows.pop(choice - 1)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(rows)

    print(f"{deleted[0]} removed successfully.")

def portfolio_performance():

    labels = []
    returns = []

    total_invested = 0
    total_value = 0

    best_stock = ""
    best_return = float("-inf")

    worst_stock = ""
    worst_return = float("inf")

    largest_stock = ""
    largest_value = 0

    with open(FILE_NAME, "r") as file:

        reader = csv.reader(file)
        next(reader)

        for row in reader:

            ticker = row[0]
            shares = float(row[1])
            buy_price = float(row[2])

            stock = yf.Ticker(ticker)

            try:
                current_price = stock.info["currentPrice"]
            except Exception:
                current_price = 0

            invested = shares * buy_price
            current_value = shares * current_price
            profit = current_value - invested

            if invested > 0:
                return_percent = (profit / invested) * 100
            else:
                return_percent = 0

            total_invested += invested
            total_value += current_value

            labels.append(ticker)
            returns.append(return_percent)

            if return_percent > best_return:
                best_return = return_percent
                best_stock = ticker

            if return_percent < worst_return:
                worst_return = return_percent
                worst_stock = ticker

            if current_value > largest_value:
                largest_value = current_value
                largest_stock = ticker

    total_profit = total_value - total_invested

    if total_invested > 0:
        total_return = (total_profit / total_invested) * 100
    else:
        total_return = 0

    print("\nPortfolio Performance\n")

    print(f"Total Invested : ${total_invested:.2f}")
    print(f"Current Value  : ${total_value:.2f}")
    print(f"Total Profit   : ${total_profit:.2f}")
    print(f"Total Return   : {total_return:.2f}%")
    print()

    print(f"Best Performer : {best_stock} ({best_return:.2f}%)")
    print(f"Worst Performer: {worst_stock} ({worst_return:.2f}%)")
    print(f"Largest Holding: {largest_stock} (${largest_value:.2f})")

    plt.figure(figsize=(9, 5))
    plt.bar(labels, returns)

    plt.title("Portfolio Performance")
    plt.xlabel("Stocks")
    plt.ylabel("Return (%)")
    plt.grid(axis="y")

    plt.show()
