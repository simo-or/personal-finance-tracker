from portfolio import *
from charts import portfolio_pie_chart
from stock_info import get_stock_data
from portfolio import portfolio_performance
def menu():

    create_file()

    while True:

        print("\nPortfolio Tracker")
        print("1. Add stock")
        print("2. Show portfolio")
        print("3. Delete stock")
        print("4. Portfolio pie chart")
        print("5. Portfolio Performance")
        print("6. Stock Information")
        print("7. Exit")
        choice = input("\nChoice: ")

        if choice == "1":
            add_stock()

        elif choice == "2":
            show_portfolio()

        elif choice == "3":
            delete_stock()

        elif choice == "4":
            portfolio_pie_chart()

        elif choice == "5":
            portfolio_performance()

        elif choice == "6":
            get_stock_data()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")