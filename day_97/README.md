Today, I resolved the **Felipe's Taqueria problem** from **Harvard's CS50P Week 3**!  
This problem focused on **dictionaries**, **running totals**, and **handling end-of-file (EOF) exceptions**.  

---

## ✅ Problem Overview  

- 🌮 **Menu System** → Store menu items and prices in a dictionary.  
- 💰 **Running Total** → Calculate cumulative cost as items are ordered.  
- 🔤 **Case-Insensitive Input** → Accept items in any capitalization format.  
- ⌨️ **EOF Handling** → Exit gracefully when user presses control-d.  
- 🚫 **Silent Validation** → Ignore invalid items without error messages.  

---

## 🎯 Problem Solved

### Interactive Taqueria Ordering System
Built a program that:
- Displays Felipe's Taqueria menu with 9 items
- Accepts continuous item input from customers
- Converts input to title case for flexible matching
- Looks up prices in dictionary
- Maintains running total of order cost
- Displays formatted total after each valid item
- Silently ignores items not on the menu
- Exits cleanly when user presses control-d (EOF)

**Example Order**:
```
Welcome to Felipe's Taqueria!
Item: taco
Total: $3.00
Item: taco
Total: $6.00
Item: burrito
Total: $13.50
Item: NACHOS
Total: $24.50
Item: quesadilla
Total: $33.00
Item: ^D

```

**Invalid Items (Silently Ignored)**:
```
Item: pizza
Item: soda
Item: chips
Item: taco
Total: $3.00
```

---

## 🍴 Felipe's Menu

| Item | Price |
|------|-------|
| 🌮 Baja Taco | $4.25 |
| 🌯 Burrito | $7.50 |
| 🥣 Bowl | $8.50 |
| 🧀 Nachos | $11.00 |
| 🧀 Quesadilla | $8.50 |
| 🌯 Super Burrito | $8.50 |
| 🧀 Super Quesadilla | $9.50 |
| 🌮 Taco | $3.00 |
| 🥗 Tortilla Salad | $8.00 |

---

## 🔍 Implementation Details

### Key Components

**Menu Dictionary**
```python
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    # ... more items
}
```

**Main Loop Logic**
1. Initialize `total = 0.0`
2. Wrap input loop in `try/except EOFError`
3. Get item and convert to title case with `.title()`
4. Check if item exists in menu dictionary
5. Add price to total if valid
6. Display formatted total with `${total:.2f}`
7. Continue until control-d pressed

**Input Normalization**
- `"taco"` → `"Taco"`
- `"BURRITO"` → `"Burrito"`
- `"sUpEr QuEsAdIlLa"` → `"Super Quesadilla"`

---

## 💭 Daily Reflection  

This problem taught me about **accumulator patterns** and **graceful program termination**.  
The key insight was using EOFError exception handling to detect control-d, and `.title()` method to normalize user input for dictionary lookups.  

> "A good ordering system is like a friendly cashier — it understands you no matter how you say it, and knows exactly when you're done!" 🌮💵

---

## 🧪 Test Cases Covered

| Scenario | Input | Total Display | Notes |
|----------|-------|---------------|-------|
| Single item | `taco` | $3.00 | Basic order |
| Multiple items | `taco`, `burrito` | $3.00, $10.50 | Running total |
| Case variations | `TACO`, `BuRrItO` | $3.00, $10.50 | Title case conversion |
| Invalid item | `pizza` | (no output) | Silently ignored |
| Mixed valid/invalid | `pizza`, `taco` | $3.00 | Only valid counted |
| Exit | control-d | (exits) | EOF handled |
| Expensive items | `nachos`, `super quesadilla` | $11.00, $20.50 | High-value items |

---

## 🚀 What I Learned

- **Dictionaries as Databases**: Using key-value pairs for menu lookups
- **Accumulator Pattern**: Building running totals in loops
- **String Methods**: Using `.title()` for case normalization
- **EOF Exception**: Catching EOFError for control-d handling
- **Price Formatting**: Using f-strings with `:.2f` for currency
- **Silent Validation**: Ignoring invalid input without messages
- **User Experience**: Creating intuitive ordering flows

---

## 🎓 Key Takeaways

This problem demonstrates real-world application design:
- **Flexible input handling** makes programs user-friendly
- **Dictionary lookups** are perfect for menu/price systems
- **Running totals** are essential for shopping cart logic
- **EOF handling** provides clean exit mechanisms
- **Silent ignoring** can improve UX in certain contexts