# 🛡️ Day 25/300 – Mastering Exception Handling in Python

Today was all about writing **robust, crash-proof Python code** using exceptions.  
In real-world systems — from **fintech to AI to APIs** — error handling is non-negotiable.

---

## ✅ Topics Practiced

- ⚠️ `try-except` blocks for safe code  
- 🧠 Custom exception classes  
- 🔄 Input validation  
- 📂 File & JSON error handling  
- 💥 Raising errors with conditions  
- 🛠️ Multi-error scenarios in logic-heavy code  

---

## 🔍 What I Solved Today

1. **Safe Division Calculator**  
   → Divide two numbers safely. Return friendly message for division by zero using `ZeroDivisionError`.

2. **Student Age Verifier**  
   → Ask for user age. Catch `ValueError` if input isn't a valid number.

3. **File Reader with Grace**  
   → Load user-specified file. Catch `FileNotFoundError` if the file doesn’t exist.

4. **Password Strength Checker**  
   → Enforce strong password rules using a custom `WeakPasswordError`.

5. **Bank Withdrawal Simulator**  
   → Simulate banking logic. Raise `InsufficientFundsError` for overdrawals.

6. **Even Number Enforcer**  
   → Ask user for even number. Raise and catch `ValueError` if not even.

7. **Multi-Error Calculator**  
   → Build a calculator handling `ZeroDivisionError`, `ValueError`, and unsupported operations.

8. **Flight Booking System**  
   → Prevent double seat booking using a custom `SeatAlreadyTakenError`.

9. **Robust List Accessor**  
   → Return list item by index. Catch both `IndexError` and `ValueError`.

10. **User Profile Loader**  
    → Parse a JSON file. Handle corrupted/invalid content with `json.JSONDecodeError`.

---

## 💭 Daily Reflection

**Today taught me:**  
🛡️ Great code doesn't just work — it fails gracefully.  
Every crash caught is a future bug avoided.  
In startup code, client apps, backend logic — **error handling separates amateurs from pros**.

### Lessons:
- `try-except` isn’t just a fix — it’s a habit  
- `raise` enforces logic rules like a guardrail  
- Custom exceptions = custom logic validators  
- **Robust > Clever**

---

## 🔧 Sample – Safe Division Calculator

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed"

print(safe_divide(10, 2))
print(safe_divide(5, 0))
