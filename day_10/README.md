# 🧠 Day 10 – Python Fundamentals Revision 🔁

✅ **Topics Revised**:  
Lists, Strings, Dictionaries, Sets, Tuples, For/While Loops, Patterns, Functions

---

## 🚀 What I Practiced

Solved 10 hands-on problems to revise everything I’ve learned so far:

- 🔁 Reversed and modified a list
- 🔢 Printed prime numbers (1–50)
- 🔠 Reversed + sliced strings
- 📦 Updated and printed dictionary
- 🧵 Stripped + formatted strings
- 🔃 While loop for even sum
- 🧪 Set union, intersection, diff
- 🧱 Tuple → List → Tuple conversion
- 🌟 Star pattern using nested loops
- 🧠 Counted even/odd using a function

Every question helped me strengthen logic, syntax memory, and confidence to build projects faster.

---

## 🧪 Sample – Even & Odd Counter
```python
def count_even_odd(numbers):
    even = sum(1 for n in numbers if n % 2 == 0)
    odd = len(numbers) - even
    return even, odd

print(count_even_odd([1, 2, 3, 4, 5, 6]))
