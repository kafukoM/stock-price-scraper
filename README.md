# Stock Price Scraper

This Python project scrapes real-time stock price information from **Google Finance** using `requests` and `BeautifulSoup`. The script fetches the latest stock price and currency for a given ticker symbol and exchange.

## Features

- Fetches real-time stock prices from Google Finance.
- Uses `BeautifulSoup` for HTML parsing.
- Handles stock symbols and exchanges dynamically.
- Outputs structured data (ticker, exchange, price, currency).

## Requirements

Ensure you have Python 3 installed. Install dependencies using:

```bash
pip install beautifulsoup4==4.11.2 requests==2.28.2
```

## Usage

Run the script directly to fetch a stock price:

```bash
python stock_scraper.py
```

Example function usage in Python:

```python
from stock_scraper import get_price_information

stock_info = get_price_information("AAPL", "NASDAQ")
print(stock_info)
```
