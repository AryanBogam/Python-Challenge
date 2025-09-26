Today, I resolved the **Coke Machine problem** from **Harvard's CS50P Week 2**!  
This problem focused on **loops**, **input validation**, and **simulating a vending machine** transaction system.  

---

## ✅ Problem Overview  

- 🥤 **Vending Machine Logic** → Simulate purchasing a 50-cent Coke.  
- 🔄 **While Loops** → Keep asking for coins until payment is complete.  
- 💰 **Coin Validation** → Only accept quarters (25¢), dimes (10¢), and nickels (5¢).  
- 🧮 **Change Calculation** → Calculate and display change owed when overpaid.  

---

## 🎯 Problem Solved

### Coke Vending Machine Simulator
Built a program that:
- Sets Coke price at 50 cents
- Displays current amount due
- Accepts only valid coin denominations (25, 10, 5 cents)
- Updates amount due after each valid coin insertion
- Ignores invalid coins and non-integer inputs
- Calculates and displays change when overpaid

**Example**:
```
Amount Due: 50
Insert Coin: 25
Amount Due: 25
Insert Coin: 10
Amount Due: 15
Insert Coin: 10
Amount Due: 5
Insert Coin: 10
Change Owed: 5
```

**Invalid Input Example**:
```
Amount Due: 50
Insert Coin: 30
Amount Due: 50
Insert Coin: cat
Insert Coin: 25
Amount Due: 25
```

---

## 💭 Daily Reflection  

This problem taught me about **persistent loops** and **robust input validation**.  
The key insight was handling both invalid coin types and non-numeric input gracefully.  

> "Real-world programming is like a vending machine — you have to handle every crazy thing users might try to feed it!" 🥤💰