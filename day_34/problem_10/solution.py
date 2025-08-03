stock_prices = {
    "AAPL": {"NYSE": 195.5, "NASDAQ": 194.9},
    "TSLA": {"NYSE": 780.2, "NASDAQ": 780.0}
}

print("Arbitrage Opportunity Analysis:")
print("(Looking for price differences > 0.5%)")

for stock in stock_prices:
    nyse_price = stock_prices[stock]["NYSE"]
    nasdaq_price = stock_prices[stock]["NASDAQ"]

    price_diff = abs(nyse_price - nasdaq_price)

    higher_price = max(nyse_price, nasdaq_price)
    percentage_diff = (price_diff / higher_price) * 100
    
    print(f"\n{stock}:")
    print(f"  NYSE: ${nyse_price}")
    print(f"  NASDAQ: ${nasdaq_price}")
    print(f"  Difference: ${price_diff:.2f} ({percentage_diff:.2f}%)")

    if percentage_diff > 0.5:
        print("ARBITRAGE OPPORTUNITY!")

        if nyse_price < nasdaq_price:
            print("Strategy: Buy on NYSE, Sell on NASDAQ")
        else:
            print("Strategy: Buy on NASDAQ, Sell on NYSE")
    else:
        print("No significant arbitrage opportunity")