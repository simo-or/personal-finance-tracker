# Personal Finance Tracker

A personal Python project for tracking stock investments and monitoring portfolio performance using live market data.

## Features

- Add stocks to a portfolio
- Remove stocks from the portfolio
- View current stock prices
- Calculate profit or loss for each investment
- Display the overall portfolio performance
- Portfolio allocation pie chart
- Portfolio performance chart

## Built With

- Python
- yfinance
- pandas
- matplotlib
- CSV

## Getting Started

Clone the repository:

```bash
git clone https://github.com/simo-or/personal-finance-tracker.git
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the project:

```bash
python main.py
```

## Project Structure

```
personal-finance-tracker/
│
├── main.py
├── menu.py
├── portfolio.py
├── stock_info.py
├── charts.py
├── requirements.txt
└── .gitignore
```

## Future Plans

- Build a graphical interface with CustomTkinter
- Store data in SQLite instead of CSV
- Add portfolio history and performance over time
- Export reports to Excel or PDF

## About

This project was created as a way to practice Python while building something useful. It combines file handling, APIs, data analysis, and data visualization in a single application.
