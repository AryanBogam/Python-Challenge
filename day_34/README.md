# 💼 Day 34/300 – Hedge Fund Simulation in Python

Today was all about building a **basic hedge fund engine** using Python.

From tracking P&L, fees, drawdowns, and positions to simulating Sharpe ratios and arbitrage detection — this felt like building the **backend brain of a quant fund**.

And I won’t lie — **this was one of the hardest days so far**.  
I struggled with logic-heavy calculations like max drawdown and rolling signals.  
Had to break the problems down multiple times and even used **Claude AI** to deeply understand some concepts and edge cases.

---

## ✅ Topics Practiced

- 💰 Portfolio valuation using nested dictionaries  
- ⚖️ Risk exposure & position logic (Long/Short/Neutral)  
- 📉 Drawdown calculation (peak-trough tracking)  
- 📊 Sharpe ratio approximation (mean, stdev, risk-free)  
- 🧠 Strategy signals via rolling price logic  
- 🔄 Daily P&L & hedge fund 2/20 fee structure  
- 🧾 Sector allocation with grouped summarization  
- 🚨 Arbitrage detection across exchanges  
- 🔧 Thinking like a financial system, not just a script  
- 🔍 Clean financial logic and modular calculations

---

## 🔍 What I Solved Today

1. **Portfolio Value Calculator**  
   → Multiplied quantity × price for each asset and summed up total.  
   → Practiced nested dictionary traversal and aggregation.

2. **Risk Exposure Checker**  
   → Identified if any stock made up >30% of total portfolio value.  
   → Simulated real-world allocation risk detection.

3. **Long vs Short Positions Tracker**  
   → Checked if position quantity was positive, negative, or zero.  
   → Labeled assets as LONG / SHORT / NEUTRAL accordingly.

4. **Daily P&L (Profit & Loss) Calculator**  
   → Calculated per-stock and total net gain/loss using day-to-day price changes.  
   → Practiced data structure usage and arithmetic logic.

5. **Hedge Fund Fee Structure Calculator (2/20)**  
   → Simulated classic hedge fund model: 2% management fee + 20% performance fee.  
   → Built reusable logic around capital, final value, and profits.

6. **Drawdown Detector**  
   → Found the largest drop from peak to bottom in portfolio value history.  
   → Used a smart peak-tracking algorithm — this was a real challenge.

7. **Sharpe Ratio (Simplified)**  
   → Computed average return, standard deviation, and built a basic Sharpe Ratio.  
   → Reinforced how risk-adjusted returns are calculated.

8. **Signal-Based Buy/Sell Simulation**  
   → Used rolling logic to detect 3-day streaks (up or down) and generated BUY/SELL signals.  
   → Required careful index tracking and pattern logic.

9. **Sector Allocation Analyzer**  
   → Grouped assets by sector and calculated each sector’s percentage allocation.  
   → Tricky nested loops — required precise data parsing.

10. **Arbitrage Opportunity Detector**  
    → Compared prices across exchanges for each stock and flagged if the difference exceeded 0.5%.  
    → Simulated real-time arbitrage bots.

---

## 💭 Daily Reflection

Today made me realize:  
**Finance isn't about money — it's about logic, strategy, and survival.**

This challenge pushed my brain beyond basic syntax.  
It was **designing real hedge fund systems** — simplified, yes, but true to how real quants think.

Struggled hard with drawdown logic and Sharpe calculation.  
Even had to lean on **Claude AI** to break down some advanced logic pieces.  
But I didn’t give up — I refactored, retried, and **learned to think like a system builder, not just a scripter.**

Tomorrow? We go deeper.  
Because **average doesn’t build legacies.**

---

## 🧠 Sample – Portfolio Value Calculator

```python
portfolio = {
    "AAPL": {"qty": 10, "price": 195},
    "TSLA": {"qty": 5, "price": 780},
    "GOOG": {"qty": 2, "price": 2600}
}

def calculate_total_value(portfolio):
    total = 0
    for stock, data in portfolio.items():
        total += data["qty"] * data["price"]
    return total

print("Total Portfolio Value:", calculate_total_value(portfolio))
# Output: Total Portfolio Value: 10650
