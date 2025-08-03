Q9. Sector Allocation Analyzer

Problem:
Given stocks and their sector tags, calculate how much % you’ve allocated to each sector.
portfolio = {
    "AAPL": {"qty": 10, "price": 195, "sector": "Tech"},
    "JNJ": {"qty": 5, "price": 170, "sector": "Healthcare"},
    "TSLA": {"qty": 5, "price": 780, "sector": "Auto"}
}

Goal: Output % of total portfolio in each sector.
Learn: Nested loop + grouping logic.