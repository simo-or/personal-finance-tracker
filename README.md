# Personal Finance Tracker

A Python command-line application for tracking a personal stock portfolio — pulls live market prices, calculates profit/loss, and visualizes portfolio allocation and performance.

## Features

- **Live stock prices** via the `yfinance` API
- **Portfolio management** — add and remove holdings
- **Profit/Loss tracking** for each position
- **Data visualization** — portfolio allocation (pie chart) and performance by stock (bar chart), built with `matplotlib`
- **CSV-based storage** for portfolio data

## Screenshots

**Portfolio Allocation**

![Portfolio Allocation](screenshots/portfolio_allocation.png)

**Portfolio Performance**

![Portfolio Performance](screenshots/portfolio_performance.png)

## Tech Stack

`Python` · `pandas` · `yfinance` · `matplotlib`

## Getting Started

### Prerequisites

- Python 3.9+

### Installation

```bash
# Clone the repo
git clone https://github.com/simo-or/personal-finance-tracker.git
cd personal-finance-tracker

# (Recommended) create a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Usage

```bash
python main.py
```

Follow the on-screen menu to add stocks to your portfolio, view profit/loss, and generate charts.

## Roadmap

- [ ] Migrate storage from CSV to SQLite
- [ ] Add unit tests for portfolio calculations
- [ ] Add historical performance tracking over time

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
