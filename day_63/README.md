# 🐍 Day 63/300 – Beginner → Intermediate DSA Problems in Python  

Today, I practiced **Data Structures & Algorithms (DSA)** problems in Python — focusing on **loops, lists, strings, matrices, and basic algorithms** to sharpen problem-solving skills.  

---

## ✅ Topics Practiced  

- 🔄 Left List Rotations  
- 🤝 Union of Lists  
- 🔁 String Rotations Check  
- ➕ Triplets with Target Sum  
- 🫧 Sorting Without Built-ins  
- 🅰️ Vowels & Consonants Counter  
- 📝 Longest Word Finder  
- 🟰 Symmetric Matrix Check  
- 🔗 List Intersection Finder  
- 🔺 Pascal's Triangle Generation  

---

## 🔍 What I Solved Today  

1. **Left Rotate a List by k Positions**  
   → Rotated a list to the left by `k` positions using loops and modular arithmetic.  

2. **Find Union of Two Lists**  
   → Merged two lists into one without duplicates using loops and sets.  

3. **Check if Two Strings are Rotations**  
   → Verified if one string is a rotation of the other using string concatenation.  

4. **Find All Triplets with Given Sum**  
   → Found all triplets in a list whose sum equals a target value.  

5. **Sort a List Without Built-in Sort**  
   → Implemented Bubble Sort to arrange numbers in ascending order.  

6. **Count Vowels and Consonants in a String**  
   → Counted vowels and consonants from a given string using loops.  

7. **Find the Longest Word in a Sentence**  
   → Extracted the longest word from a given sentence.  

8. **Check if Matrix is Symmetric**  
   → Verified whether a square matrix is symmetric across the diagonal.  

9. **Find Intersection Point in Two Lists**  
   → Found the first common element between two sorted lists.  

10. **Generate Pascal’s Triangle (First n Rows)**  
    → Generated Pascal's Triangle using nested loops for the first `n` rows.  

---

## 💭 Daily Reflection  

Today’s problems were **slightly more algorithmic** and required **logical thinking** rather than direct formula-based solutions.  

I learned new ways to manipulate **lists, strings, and matrices**, improving both my **problem-solving skills** and **coding speed**.  

As always, **“Code a little daily, grow massively eventually.”**  

---

## 🧠 Sample – Left Rotate a List by k Positions  

```python
def left_rotate_list(nums, k):
    n = len(nums)
    k = k % n  # handle if k > n
    rotated = []
    for i in range(n):
        rotated.append(nums[(i + k) % n])
    return rotated

# Example
numbers = [1, 2, 3, 4, 5]
k = 2
print("Original:", numbers)
print(f"Left Rotated by {k}:", left_rotate_list(numbers, k))
