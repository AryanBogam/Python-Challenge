# 🧠 Day 15 – Exception Handling & Input Validation 💥

✅ **Topics Mastered**
- `try`, `except`, `else`, `finally`
- Data type casting & validation
- Handling runtime errors (ZeroDivisionError, ValueError, IndexError)
- Repeated input logic
- Custom error messages & condition-based checks
- Building user-proof, backend-safe programs

---

## 🚀 What I Practiced

Solved 10 real-world problems to build **resilience and reliability into my Python code**, including:

- 🔐 Age and password validation
- 🔄 Safe user input with retries
- 📤 Division and file access with fail-safes
- 🔁 Loop-based input checks until correct
- 💸 Transaction simulator with error handling

Each challenge was crafted to simulate real production errors, and taught me how to think like a **backend engineer** — not just a learner.

---

### 💡 To grow faster, I took help to:
- Understand how to approach harder problems   
- In day_14 problems I have took help of chatgpt to see the approach but, I solved this question my own

---

## 🧪 Sample – Transaction Simulator 💳

```python
try:
    balance = float(input("Enter current balance: "))
    spend = float(input("Enter amount to spend: "))

    if balance < 0 or spend < 0:
        raise ValueError("Values must be positive.")

    if spend > balance:
        raise ValueError("Insufficient funds!")

    print("✅ Transaction successful. Remaining balance:", balance - spend)

except ValueError as e:
    print("Transaction Error:", e)
