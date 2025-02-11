import requests
from bs4 import BeautifulSoup

def get_fx_rate(currency):
    url = f"https://www.google.com/finance/quote/{currency}-USD"
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    fx_div = soup.find("div", attrs={"data-last-price": True})
    
    fx_rate = float(fx_div["data-last-price"])
    
    return fx_rate

    

def get_price_information(ticker, exchange):
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    price_div = soup.find("div", attrs={"data-last-price": True})
    
    price = float(price_div["data-last-price"])
    
    currency = price_div["data-currency-code"]
    
    fx_rate = get_fx_rate(currency)
    
    usd_price = price
    
    if currency != "USD":
        usd_price = round(price * fx_rate, 2)
    
    return {
        "ticker" : ticker,
        "exchange" : exchange,
        "price": price,
        "currency": currency,
        "usd_price": usd_price
    }
    
if __name__ == "__main__":
    print(get_price_information("SHOP", "TSE"))