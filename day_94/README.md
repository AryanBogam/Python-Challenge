Today, I resolved the **Fuel Gauge problem** from **Harvard's CS50P Week 3**!  
This problem focused on **exception handling**, **fraction parsing**, and **converting fractions to percentages**.  

---

## ✅ Problem Overview  

- ⛽ **Fraction to Percentage** → Convert fuel level fractions (X/Y) to percentages.  
- 🔢 **Input Validation** → Ensure X and Y are integers, X ≤ Y, and Y ≠ 0.  
- 🔄 **Error Handling** → Re-prompt on invalid input using try/except blocks.  
- 📊 **Special Display** → Show "E" for empty (≤1%), "F" for full (≥99%), or percentage.  

---

## 🎯 Problem Solved

### Fuel Level Calculator
Built a program that:
- Accepts fraction input in X/Y format
- Validates that X and Y are integers
- Ensures X is not greater than Y
- Handles division by zero errors
- Converts fraction to rounded percentage
- Displays "E" for empty, "F" for full, or percentage value
- Re-prompts on any invalid input

**Normal Examples**:
```
Fraction: 3/4
75%

Fraction: 1/2
50%

Fraction: 2/3
67%

Fraction: 1/4
25%
```

**Special Cases**:
```
Fraction: 0/100
E

Fraction: 1/100
E

Fraction: 99/100
F

Fraction: 100/100
F
```

**Error Handling**:
```
Fraction: cat/dog
Fraction: 5/0
Fraction: 10/5
Fraction: 1.5/3
Fraction: 1/3
33%
```

---

## 🔍 Implementation Details

### Three Core Functions

**`main()`**
- Runs infinite loop until valid input received
- Catches ValueError and ZeroDivisionError
- Re-prompts on exceptions without error messages
- Displays final fuel gauge result

**`convert(fraction)`**
- Splits fraction string by '/'
- Converts X and Y to integers
- Validates X ≤ Y
- Calculates and returns rounded percentage
- Raises appropriate exceptions for invalid input

**`gauge(percentage)`**
- Returns "E" if percentage ≤ 1%
- Returns "F" if percentage ≥ 99%
- Returns "X%" for all other values

### Validation Rules

| Rule | Check | Exception |
|------|-------|-----------|
| Format | Must be X/Y | ValueError |
| Integer | X and Y must be integers | ValueError |
| Range | X must be ≤ Y | ValueError |
| Zero | Y cannot be 0 | ZeroDivisionError |

---

## 💭 Daily Reflection  

This problem taught me about **robust exception handling** and **user-friendly re-prompting**.  
The key insight was separating concerns into three functions: parsing, validation, and display logic.  

> "A good fuel gauge doesn't just show levels — it handles every possible error gracefully, just like good code should!" ⛽✨

---

## 🚀 What I Learned

- **Exception Handling**: Using try/except to catch specific errors
- **String Parsing**: Splitting and validating input formats
- **Function Design**: Separating parsing, calculation, and display logic
- **Silent Re-prompting**: Handling errors without printing error messages
- **Edge Cases**: Testing boundary conditions (0%, 1%, 99%, 100%)
- **User Experience**: Creating intuitive, forgiving input systems