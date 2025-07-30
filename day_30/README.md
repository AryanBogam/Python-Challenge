# 🧠 Day 30/300 – Real-World Logic Using Lists & Tuples in Python

Today was about **practical data handling** using Python `lists`, `tuples`, and simple math.  
I went deep into memory optimization, real-world systems like billing, inventory lookups, and coordinate-based calculations.

Each question wasn’t just a syntax drill — it was a simulation of real-world data patterns and everyday logic tools.

---

## ✅ Topics Practiced

- 📦 Tuple unpacking & string formatting  
- 🧠 Finding max from a structured dataset  
- 🔁 Filtering data using conditions  
- 🔃 Reversing word order in strings  
- 🧮 List comparison and differences  
- 🎟️ Seat allocation simulation using nested lists  
- 🛒 Shopping cart billing logic  
- 🧷 Memory measurement with `sys.getsizeof()`  
- 📐 Distance formula between coordinate points  
- 🚫 Safe user-driven search in tuple-based datasets

---

## 🔍 What I Solved Today

1. **Student Topper Finder**  
   → From a list of `(name, score)` tuples, found **student(s) with the highest score**.  
   → Handled ties and returned all top scorers.

2. **Tuple Unpacker: Employees**  
   → Cleanly unpacked tuples like `(name, age, department)` and printed readable descriptions.  
   → Improved clarity using string interpolation.

3. **Temperature Filter**  
   → Filtered temperatures over **37.5°C** from a list — simulating fever detection.  
   → Great intro to medical or IoT data processing.

4. **Reverse Words in a Sentence**  
   → Took a sentence string, split into words, **reversed**, and joined again.  
   → Practiced `.split()`, slicing, and `.join()`.

5. **List Difference Tool**  
   → Compared two lists and found items **only in the first** (like a diff tool).  
   → Useful in sync systems, log analyzers, and API deltas.

6. **Movie Seat Allocator (Nested Lists)**  
   → Counted **all "Empty" seats** in a nested list (2D matrix).  
   → Simulated basic seat booking logic.

7. **Product Inventory Lookup**  
   → Looked up stock count from a list of `(item, quantity)` tuples based on user input.  
   → Displayed availability or graceful "not found" message.

8. **Shopping Cart Summary**  
   → Calculated total bill from a cart like `[item, qty, price]`.  
   → Applied quantity × price and summed for final billing.

9. **Memory Saver: Convert List to Tuple**  
   → Measured memory of a list vs. the same as a tuple using `sys.getsizeof()`.  
   → Reinforced why tuples are more memory-efficient.

10. **Tuple of Coordinates – Distance Calculator**  
    → Took two `(x, y)` tuples and calculated **Euclidean distance**.  
    → Practiced the `sqrt()` formula from `math` module.

---

## 💭 Daily Reflection

**What I realized today:**  
🔢 Lists and tuples are **powerful data models** that shape everything — from APIs to billing systems and even memory-efficient storage.

When you master how to navigate, filter, and extract logic from structured containers like lists or tuples, you unlock a level of Python that’s clean, clear, and production-ready.

### Lessons:
- Don’t just store data — **structure** it to solve real problems  
- Memory awareness helps you write **better, scalable systems**  
- Clean tuple unpacking → clean readable output  
- 2D lists simulate **grids, maps, seating, matrices** in real-world systems

---

## 🔧 Sample – Shopping Cart Summary

```python
cart = [["Milk", 2, 30], ["Bread", 1, 40], ["Eggs", 12, 5]]

def calculate_total(cart):
    total = 0
    for item in cart:
        name, qty, price = item
        total += qty * price
    return total

print("Total Bill: ₹", calculate_total(cart))
