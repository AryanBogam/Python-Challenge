# 🧠 Day 6 – Python If-Else Logic Builder ⚙️

✅ **Topics Covered**
- `if`, `elif`, `else` decision-making
- Logical operators: `and`, `or`, `not`
- Numeric comparisons: `>`, `<`, `>=`, `==`
- String conditionals
- Nested conditionals
- Real-world decision logic simulations

---

## 🚀 What I Built Today

I created **10 real-life logic-based programs** using Python's `if-else` structure — without relying on loops or advanced concepts.

Each project simulated real-world thinking:
- Admissions filter based on GPA + GitHub
- Freelance income evaluator
- Crypto badge classifier
- Daily discipline analyzer
- Trading PnL logic

---

## 🧪 Sample Code Snippet – Crypto Holder Badge 

```python
portfolio = float(input("Enter your crypto portfolio size in ₹: "))

if portfolio > 1000000:
    print("Whale")
elif portfolio >= 100000:
    print("Mid-level")
else:
    print("Shrimp")
