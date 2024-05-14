# Assignment 8
# Written by Matthew Walczyk 
# 2/3/2024


# Main function
def main():

    stocks = {
        "F" : "12.89",
        "IBM" : "44.67",
        "AAPL" : "147.82",
        "META" : "385.14",
        "AMZN" : "315.77",
        "NVDA" : "257.59",
        "MSFT" : "279.65",
        "AMD" : "164.12",
        "GOOGL" : "542.87",
        "PLTR" : "104.47"
    }

    symbol = input("Please enter a stock ticker symbol")

    if symbol in stocks.keys():
        print(f"The price is {stocks.get(symbol)}")
    else:
        print(f"Could not find the symbol {symbol}")

# Call main function
main()