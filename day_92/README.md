Today, I resolved the **Nutrition Facts problem** from **Harvard's CS50P Week 2**!  
This problem focused on **dictionaries**, **data lookup**, and **working with structured nutritional data**.  

---

## ✅ Problem Overview  

- 🍎 **Calorie Lookup System** → Search for fruits and display their calorie information.  
- 📚 **Dictionary Usage** → Store fruit names as keys and calories as values.  
- 🔤 **Case-Insensitive Search** → Handle user input regardless of capitalization.  
- 🎯 **Selective Output** → Only display calories if the fruit exists in the database.  

---

## 🎯 Problem Solved

### Fruit Calorie Lookup Tool
Built a program that:
- Stores nutritional data for 20 different fruits
- Accepts fruit names from user input
- Converts input to lowercase for flexible matching
- Looks up calories in a dictionary
- Displays calorie information only if fruit is found
- Handles invalid items gracefully (no output for non-fruits)

**Example**:
```
Item: Apple
Calories: 130

Item: banana
Calories: 110

Item: STRAWBERRIES
Calories: 50
```

**Edge Cases Handled**:
```
Item: Pizza
(no output - not in database)

Item: Watermelon
Calories: 80

Item:   orange   
Calories: 80
(handles extra whitespace)
```

---

## 🍇 Fruit Database

The program includes FDA nutritional data for:
- 🍎 Apple: 130 calories
- 🥑 Avocado: 50 calories
- 🍌 Banana: 110 calories
- 🍈 Cantaloupe: 50 calories
- 🍊 Grapefruit: 60 calories
- 🍇 Grapes: 90 calories
- 🍈 Honeydew Melon: 50 calories
- 🥝 Kiwifruit: 90 calories
- 🍋 Lemon: 15 calories
- 🍋 Lime: 20 calories
- 🍑 Nectarine: 60 calories
- 🍊 Orange: 80 calories
- 🍑 Peach: 60 calories
- 🍐 Pear: 100 calories
- 🍍 Pineapple: 50 calories
- 🍑 Plums: 70 calories
- 🍓 Strawberries: 50 calories
- 🍒 Sweet Cherries: 100 calories
- 🍊 Tangerine: 50 calories
- 🍉 Watermelon: 80 calories

---

## 💭 Daily Reflection  

This problem taught me about **dictionaries as lookup tables** and **handling user input variations**.  
The key insight was using `.lower()` and `.strip()` to normalize input, and `.get()` to safely query the dictionary without causing errors.  

> "Good data structures are like a well-organized pantry — you can find exactly what you need, exactly when you need it!" 🍎📊