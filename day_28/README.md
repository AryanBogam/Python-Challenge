# 🧠 Day 28/300 – Dictionary Mastery & Error-Proof Data Systems in Python

Today I stepped into **intermediate to hard-level logic** using Python `dictionaries` and advanced `try-except` handling.  
This wasn’t just about key lookups — I built real-world **data systems** that could **fail gracefully** and still return results.

---

## ✅ Topics Practiced

- 🔑 Dictionary key-value management  
- 🛡️ Error handling with `try-except` and `KeyError`, `ValueError`, `ZeroDivisionError`  
- 🔁 Looping through dictionaries  
- 🧱 Nested dictionaries and access patterns  
- 💬 User input validation and error-proofing  
- 🔄 Data lookups in reverse (value → key)  
- 🚨 Graceful crash handling in logic apps

---

## 🔍 What I Solved Today

1. **Phonebook Lookup (With Error Handling)**  
   → User inputs a name, program returns the phone number from a dictionary.  
   → If name doesn’t exist, it shows `"Contact not found"` using `try-except`.

2. **Reverse Dictionary Search**  
   → User inputs an email, program searches the dictionary in reverse to return the username.  
   → If not found, it shows `"Email not registered"`.

3. **Inventory Manager**  
   → Simulates a store’s product stock system.  
   → Handles user orders, suggests similar items if not found, and uses error-proofed lookup.

4. **Student Marks Tracker**  
   → Nested dictionary with student names and subjects.  
   → Retrieves marks, handles both missing student and missing subject using `try-except`.

5. **Safe Division from Dictionary**  
   → Dictionary with numeric values.  
   → Performs `100 / value` for a given key. Handles:
   - Key not found  
   - Division by zero

6. **Banking System Simulator**  
   → User enters name and withdrawal amount.  
   → Handles invalid users, overdraft attempts, and negative values with friendly errors.

7. **Case-Insensitive Dictionary Lookup**  
   → Accepts country name in any case and returns code.  
   → Handles not found errors using `try-except` and `.lower()` transformations.

8. **Multiple Key Error Handling (City Population Diff)**  
   → Takes 2 cities and calculates the population difference.  
   → Handles cases where one or both cities don’t exist in the dictionary.

9. **Restaurant Order Processor**  
   → Menu stored in a dictionary.  
   → User orders 3 items. Handles:
   - Items not in menu  
   - Invalid quantity inputs using `try-except`

10. **Dictionary File Reader**  
    → Simulates loading a dictionary from a file with prices.  
    → Safely converts string prices to integers and filters invalid entries using `try-except`.

---

## 💭 Daily Reflection

**What I realized today:**  
🔁 Dictionaries + `try-except` = **Data systems with brains**.  
I wasn’t just storing values — I was validating, protecting, and searching like a real app would.  
Each problem tested my control over **unexpected inputs** and how I handled them like a calm developer.

### Lessons:
- `KeyError` is your friend — if you handle it.  
- Every `try-except` block is a confidence boost in user-facing logic.  
- Reverse lookups and nested dicts simulate real database thinking.  
- Smart apps don’t crash — they guide the user.

---

## 🔧 Sample – Phonebook Lookup

```python
contacts = {"Alice": "9123456789", "Bob": "9000000000"}

name = input("Enter contact name: ")

try:
    print(f"Number: {contacts[name]}")
except KeyError:
    print("Contact not found.")
