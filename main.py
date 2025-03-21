import requests
from bs4 import BeautifulSoup
from dataclasses import dataclass
from tabulate import tabulate

@dataclass
class Stock:
    # Data class to store stock information
    ticker: str  # Stock ticker symbol (e.g., "AAPL")
    exchange: str  # Stock exchange (e.g., "NASDAQ")
    price: float = 0  # Stock price (default 0, will be updated)
    currency: str = "USD"  # Currency of the stock price (default USD)
    usd_price: float = 0  # Price converted to USD (default 0, will be updated)
    
    def __post_init__(self):
        # Runs after the dataclass __init__ method
        # Fetch real-time stock price and update the object attributes
        price_info = get_price_information(self.ticker, self.exchange)
        
        if price_info["ticker"] == self.ticker:
            self.currency = price_info["currency"]
            self.price = price_info["price"]
            self.usd_price = price_info["usd_price"]
            
@dataclass
class Position:
    # Data class to store position information - Stock & Quantity
    stock: Stock 
    quantity: int 
    
@dataclass 
class Portfolio:
    # Data class to store portfolio information - List of positions
    positions: list[Position] 
    
    def get_total_value(self):
        total_value = 0
        
        # Loop through each position in list to retrieve each position value
        for position in self.positions:
            total_value += position.quantity * position.stock.usd_price
        
        return round(total_value, 1)

def get_fx_rate(currency):
    # Fetches the exchange rate for a given currency against USD
    url = f"https://www.google.com/finance/quote/{currency}-USD"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find the div containing the exchange rate
    fx_div = soup.find("div", attrs={"data-last-price": True})
    
    fx_rate = float(fx_div["data-last-price"])  # Convert exchange rate to float
    
    return fx_rate  # Return the exchange rate

def get_price_information(ticker, exchange):
    # Fetches stock price and currency details from Google Finance
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find the div containing the stock price
    price_div = soup.find("div", attrs={"data-last-price": True})
    
    price = float(price_div["data-last-price"])  # Convert price to float
    
    currency = price_div["data-currency-code"]  # Extract currency code
    
    
    usd_price = price  # Default to same price if already in USD
    
    if currency != "USD":
        fx_rate = get_fx_rate(currency)  # Get exchange rate for the currency

        usd_price = round(price * fx_rate, 2)  # Convert to USD if needed
    
    return {
        "ticker" : ticker,
        "exchange" : exchange,
        "price": price,
        "currency": currency,
        "usd_price": usd_price
    }
    
    
def display_portfolio_summary(portfolio):
    if not isinstance(portfolio, Portfolio):
        raise TypeError("Please Provide a valid instance of Portfolio class")    
    
    portfolio_value = portfolio.get_total_value()
    
    position_data = []
    
    # Positions are sorted in descending order according to market value
    for position in sorted(portfolio.positions, key= lambda x: x.quantity * x.stock.usd_price, reverse=True):
        position_data.append(
            [
                position.stock.ticker,
                position.stock.exchange,
                position.quantity,
                position.stock.usd_price,
                position.quantity * position.stock.usd_price, # Market value
                position.quantity * position.stock.usd_price / portfolio_value * 100 # Percentage of allocation

            ]
        )
        
    print(tabulate(position_data,
                   headers=["Ticker", "Exchange", "Quantity", "Price", "Market value", "% Allocation"],
                   tablefmt="psql",
                   floatfmt=".2f"
                   ))
    
    print(f"Total portfolio value: ${portfolio_value:,.2f}")
        
    
if __name__ == "__main__":
    # Main execution block, creates a Stock object and prints it
    shop = Stock("SHOP", "TSE")
    google = Stock("GOOGL", "NASDAQ")
    msft = Stock("MSFT", "NASDAQ")
    
    portfolio = Portfolio([Position(shop, 10), Position(google, 2), Position(msft, 6)])
     
    display_portfolio_summary(portfolio)
     
    # print(portfolio.get_total_value())
