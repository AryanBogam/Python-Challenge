Q10. Arbitrage Opportunity Detector

Problem:
If the price of a stock is significantly different across exchanges, detect it as an arbitrage opportunity.
stock_prices = {
    "AAPL": {"NYSE": 195.5, "NASDAQ": 194.9},
    "TSLA": {"NYSE": 780.2, "NASDAQ": 780.0}
}

Goal: If price difference > 0.5%, flag it.
Learn: Market inefficiency detection logic.