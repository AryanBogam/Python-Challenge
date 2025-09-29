Today, I resolved the **Vanity Plates problem** from **Harvard's CS50P Week 2**!  
This problem focused on **string validation**, **conditional logic**, and **implementing multiple validation rules** for license plates.  

---

## ✅ Problem Overview  

- 🚗 **License Plate Validation** → Check if vanity plates meet Massachusetts DMV requirements.  
- 📏 **Length Constraints** → Plates must be between 2 and 6 characters.  
- 🔤 **Letter Requirements** → Must start with at least two letters.  
- 🔢 **Number Rules** → Numbers must be at the end, and first number cannot be '0'.  
- ⛔ **Character Restrictions** → No periods, spaces, or punctuation allowed.  

---

## 🎯 Problem Solved

### Vanity Plate Validator
Built a program that validates license plates according to these rules:

1. **Length Rule**: Must be 2-6 characters long
2. **Starting Rule**: First two characters must be letters
3. **Number Placement**: Numbers can only appear at the end (no letters after numbers)
4. **Zero Rule**: First number used cannot be '0'
5. **Character Rule**: Only alphanumeric characters (no spaces, periods, punctuation)

**Valid Examples**:
```
Plate: CS50
Valid

Plate: HELLO
Valid

Plate: AAA222
Valid

Plate: CS
Valid
```

**Invalid Examples**:
```
Plate: CS05
Invalid (first number is 0)

Plate: CS50P
Invalid (letter after numbers)

Plate: PI3.14
Invalid (contains punctuation)

Plate: H
Invalid (too short)

Plate: OUTATIME
Invalid (too long - 8 characters)

Plate: 50
Invalid (doesn't start with 2 letters)

Plate: CS 50
Invalid (contains space)
```

---

## 🔍 Implementation Details

### Key Functions

**`main()`**
- Gets plate input from user
- Calls validation function
- Displays "Valid" or "Invalid"

**`is_valid(s)`**
- Checks all 5 validation rules
- Returns `True` if all rules pass
- Returns `False` if any rule fails

### Validation Logic

```python
# Rule 1: Length check
if len(s) < 2 or len(s) > 6:
    return False

# Rule 2: First 2 characters must be letters
if not s[0].isalpha() or not s[1].isalpha():
    return False

# Rule 3: Only alphanumeric characters
if not s.isalnum():
    return False

# Rules 4 & 5: Number placement and zero check
# Iterate through string checking digit rules
```

---

## 💭 Daily Reflection  

This problem taught me about **layered validation** and **string analysis**.  
The key insight was checking rules in logical order and understanding that numbers must form a continuous block at the end of the plate.  

> "Good validation is like a bouncer at a club — it knows exactly what's allowed in and what stays out!" 🚗✨

---

## 🚀 What I Learned

- **String Methods**: Using `.isalpha()`, `.isdigit()`, `.isalnum()`
- **Boolean Logic**: Combining multiple conditions efficiently
- **Edge Cases**: Handling boundary conditions (length, first digit)
- **State Tracking**: Using flags to track number placement
- **Clean Code**: Separating validation logic into a dedicated function