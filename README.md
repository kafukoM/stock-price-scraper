# Stock Price & Portfolio Tracker

This Python project scrapes real-time stock price information from **Google Finance** using `requests` and `BeautifulSoup`. It also provides a portfolio tracking feature to calculate total portfolio value and individual stock allocations.

## Features

- Fetches real-time stock prices from Google Finance.
- Converts stock prices to USD if needed.
- Tracks multiple stock positions in a portfolio.
- Calculates total portfolio value and percentage allocation per stock.
- Uses `BeautifulSoup` for HTML parsing.
- Displays structured data in a tabular format using `tabulate`.

## Requirements

Ensure you have Python 3 installed. Install dependencies using:

```bash
pip install beautifulsoup4==4.11.2 requests==2.28.2 tabulate==0.9.0
```

## Usage

Run the script directly to display a stock portfolio summary:

```bash
python main.py
```

### Fetch Stock Price Information

Example function usage in Python:

```python
from stock_scraper import get_price_information

stock_info = get_price_information("AAPL", "NASDAQ")
print(stock_info)
```

### Create a Portfolio and Display Summary

```python
from stock_scraper import Stock, Position, Portfolio, display_portfolio_summary

# Create stock objects
shop = Stock("SHOP", "TSE")
google = Stock("GOOGL", "NASDAQ")
msft = Stock("MSFT", "NASDAQ")

# Create a portfolio with stock positions
portfolio = Portfolio([Position(shop, 10), Position(google, 2), Position(msft, 6)])

# Display portfolio summary
display_portfolio_summary(portfolio)
```
