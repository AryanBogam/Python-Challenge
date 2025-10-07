Today, I resolved the **Grocery List problem** from **Harvard's CS50P Week 3**!  
This problem focused on **dictionaries**, **item counting**, and **sorting data for organized output**.  

---

## ✅ Problem Overview  

- 🛒 **Item Counting** → Track quantity of each grocery item entered.  
- 📚 **Dictionary Usage** → Store items as keys and counts as values.  
- 🔤 **Case Normalization** → Convert all items to uppercase for consistency.  
- 🔤 **Alphabetical Sorting** → Display items in sorted order.  
- ⌨️ **EOF Handling** → Process list when user presses control-d.  

---

## 🎯 Problem Solved

### Grocery List Counter
Built a program that:
- Accepts unlimited grocery items
- Counts duplicates (case-insensitive)
- Sorts items alphabetically
- Displays format: `COUNT ITEM`

**Example**:
```
mango
strawberry
mango
strawberry
strawberry
^D

2 MANGO
3 STRAWBERRY
```

**Case Insensitive**:
```
apple
APPLE
Apple
^D

3 APPLE
```

---

## 💭 Daily Reflection  

This problem taught me about **frequency counting with dictionaries** and **data organization**.  
The key insight was using dictionaries as counters and normalizing input with `.upper()` to handle case variations.  

> "A well-organized grocery list is like a well-structured dictionary — every item has its place, and you know exactly how much you need!" 🛒✨