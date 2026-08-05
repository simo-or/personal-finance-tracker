import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


def get_stock_data():
    ticker = input("Enter stock ticker: ").upper()

    stock = yf.Ticker(ticker)

    try:
        info = stock.info

        print("\n COMPANY INFORMATION")
        print(f"Company Name : {info.get('longName', 'N/A')}")
        print(f"Sector       : {info.get('sector', 'N/A')}")
        print(f"Industry     : {info.get('industry', 'N/A')}")
        print(f"Country      : {info.get('country', 'N/A')}")
        print(f"Market Cap   : {info.get('marketCap', 'N/A')}")
        print(f"P/E Ratio    : {info.get('trailingPE', 'N/A')}")
        print(f"Current Price: ${info.get('currentPrice', 'N/A')}")
        print(f"52W High     : ${info.get('fiftyTwoWeekHigh', 'N/A')}")
        print(f"52W Low      : ${info.get('fiftyTwoWeekLow', 'N/A')}")

        history = stock.history(period="1y")

        if history.empty:
            print("\nNo historical data found.")
            return

        print("\nLast 5 trading days:\n")
        print(history[["Open", "High", "Low", "Close", "Volume"]].tail())

        plt.figure(figsize=(10, 5))
        plt.plot(history.index, history["Close"])

        plt.title(f"{ticker} Stock Price (Last Year)")
        plt.xlabel("Date")
        plt.ylabel("Closing Price ($)")
        plt.grid(True)

        plt.show()

    except Exception as e:
        print("\nError:", e)

