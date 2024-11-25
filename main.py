# Import necessary libraries
import requests  # To make HTTP requests
import pandas as pd  # To handle and display data
import yfinance as yf
import matplotlib.pyplot as plt


# Function to fetch stock price data
def get_stock_price(symbol, api_key):
    """
    Fetches stock price data for a given symbol using the Alpha Vantage API.
    """
    # Alpha Vantage API endpoint
    base_url = "https://www.alphavantage.co/query"
    
    # Parameters for the API request
    params = {
        "function": "TIME_SERIES_INTRADAY",  # Fetch intraday stock prices
        "symbol": symbol,  # Stock ticker symbol
        "interval": "5min",  # Time interval between data points
        "apikey": api_key  # Your API key
    }
    
    # Make the API request
    response = requests.get(base_url, params=params)
    
    # Check if the response is successful
    if response.status_code == 200:
        return response.json()  # Return JSON response
    else:
        print(f"Error: Unable to fetch data for {symbol} (Status Code: {response.status_code})")
        return None

# Function to process and display stock price data
def display_stock_data(data, symbol):
    """
    Displays stock price data in a user-friendly format for a given symbol.
    """
    if data:
        # Extract the time series data
        time_series = data.get("Time Series (5min)")
        
        if time_series:
            # Convert the time series data to a Pandas DataFrame
            df = pd.DataFrame.from_dict(time_series, orient="index")
            df = df.rename(columns={
                "1. open": "Open Price",
                "2. high": "High Price",
                "3. low": "Low Price",
                "4. close": "Close Price",
                "5. volume": "Volume"
            })
            
            # Display the most recent data
            print(f"\nLatest Stock Prices for {symbol}:")
            print(df.head())  # Display the latest 5 rows
        else:
            print(f"No time series data available for {symbol}.")
    else:
        print(f"No data to display for {symbol}.")

# Main code block to run the program
if __name__ == "__main__":
    print("Welcome to the Stock Price Tracker!")
    
    # Predefined list of stock symbols
    symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]  # You can add more symbols here
    
    # User input: Choose a mode
    mode = input("\nChoose an option:\n1. Enter a stock ticker symbol\n2. View predefined stocks\nEnter your choice (1 or 2): ").strip()
    
    api_key = "NCN5RNI7UZD9KVI5"
    
    if mode == "1":
        # Ask the user for a specific stock symbol
        symbol = input("Enter the stock ticker symbol (e.g., AAPL, MSFT): ").upper()
        print(f"\nFetching stock data for {symbol}...")
        stock_data = get_stock_price(symbol, api_key)
        display_stock_data(stock_data, symbol)
    elif mode == "2":
        # Fetch and display stock data for predefined symbols
        for symbol in symbols:
            print(f"\nFetching stock data for {symbol}...")
            stock_data = get_stock_price(symbol, api_key)
            display_stock_data(stock_data, symbol)
    else:
        print("Invalid choice. Exiting the program.")
