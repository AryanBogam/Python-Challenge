Today, I resolved the **Twttr problem** from **Harvard's CS50P Week 2**!  
This problem focused on **string manipulation**, **character filtering**, and **simulating Twitter-style text shortening**.  

---

## ✅ Problem Overview  

- 🐦 **Text Shortening Logic** → Remove all vowels to create Twitter-style abbreviated text.  
- 🔤 **String Iteration** → Loop through each character to filter out vowels.  
- 📝 **Case Handling** → Remove both uppercase and lowercase vowels (A, E, I, O, U, a, e, i, o, u).  
- 🛡️ **Character Preservation** → Keep all non-vowel characters including numbers, punctuation, and spaces.  

---

## 🎯 Problem Solved

### Twitter Text Shortener
Built a program that:
- Takes any string as input from the user
- Identifies and removes all vowels (both cases)
- Preserves consonants, numbers, punctuation, and spacing
- Maintains original capitalization of remaining characters
- Returns the shortened "Twitter-style" text

**Example**:
```
Input: Twitter
Output: Twttr

Input: What's your name?
Output: Wht's yr nm?

Input: Hello, World!
Output: Hll, Wrld!
```

**Edge Cases Handled**:
```
Input: AEIOU
Output: 

Input: CS50
Output: CS50

Input: bcdfg
Output: bcdfg
```

---

## 💭 Daily Reflection  

This problem taught me about **string manipulation** and **character-by-character processing**.  
The key insight was using string membership testing to efficiently identify vowels while preserving all other characters.  

> "Sometimes the best way to communicate is to remove what's unnecessary — just like early Twitter taught us!" 🐦✂️