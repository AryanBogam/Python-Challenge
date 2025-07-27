# 🧠 Day 27/300 – Functions & Exception Handling Mastery in Python

Today I focused on creating my own **Python functions** and writing **crash-proof logic** using `try-except`.  
This was a huge leap from basic scripting — now I’m building **reusable tools** that fail gracefully and think smartly.

---

## ✅ Topics Practiced

- 🔁 Defining custom `def` functions  
- 🎯 Using `return` vs `print` correctly  
- 🛡️ `try-except` blocks for safe logic  
- 🧱 Input validation with user prompts  
- 🧮 Argument handling + default values  
- 💥 Raising custom error messages  
- 🔄 Looping through function logic  
- 🧪 Graceful failure in input-based apps

---

## 🔍 What I Solved Today

1. **Tip Calculator with Error Handling**  
   → Asked user for bill and tip %, handled invalid inputs, returned correct tip with `try-except`.

2. **Safe Division Function**  
   → Divided numbers safely. Handled division by zero with a friendly error message.

3. **Custom Greet Function**  
   → Greeted users with or without name input using default arguments.

4. **Even or Odd Checker**  
   → Wrote a function to detect even/odd, handled non-integer errors.

5. **ATM Withdrawal Simulator**  
   → Checked balance before withdrawal, raised "Insufficient Funds" error if needed.

6. **Grade Converter**  
   → Converted numeric score to letter grade (A–F). Handled bad inputs.

7. **Simple Login System**  
   → Checked credentials against hardcoded values. Raised login errors if credentials didn’t match.

8. **String Reverser with Error Handling**  
   → Reversed any input string. Handled non-string errors with `try-except`.

9. **Factorial Finder**  
   → Calculated factorial using loop. Validated for negative and non-integer values.

10. **Discount Price Calculator**  
    → Applied discount to price. Handled invalid numeric input gracefully.

---

## 🔁 Why I Repeated Some Questions

Some of today’s problems were **intentional repetitions** of earlier concepts like safe division, input validation, and reverse string.  
But this time, I implemented them **as functions with proper error handling**.

> ✅ Repeating with added complexity = **deeper mastery**  
> 🧠 I don’t just want to solve things once — I want to be able to use them *anytime, anywhere*

---

## 💭 Daily Reflection

**Today taught me:**  
🧠 Clean code isn’t just about writing — it’s about thinking like a **problem-solver**.  
Functions give structure. `try-except` gives resilience.  
The moment I wrapped logic inside functions, my code became **modular, scalable, and error-proof**.

### Lessons:
- `try-except` = trust shield for bad user input  
- `def` = blueprint for future reuse  
- `raise` lets me enforce logic like a gatekeeper  
- Repeating hard problems → builds deep muscle memory

---

## 🔧 Sample – Safe Division Function

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Division by zero is not allowed"
    except TypeError:
        return "Invalid input type. Please enter numbers only."

print(safe_divide(10, 2))  # ✅ 5.0
print(safe_divide(5, 0))   # ❌ "Division by zero is not allowed"
print(safe_divide("5", 2)) # ❌ "Invalid input type"
