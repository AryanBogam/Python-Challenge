# 🐍 Day 62/300 – Beginner → Easy DSA Problems in Python  

Today, I practiced **Basic DSA (Data Structures & Algorithms)** problems in Python — focusing on **loops, lists, sets, dictionaries, and basic algorithms** to keep building problem-solving skills.  

---

## ✅ Topics Practiced  

- 🔄 List Rotations  
- 🤝 Intersection of Lists  
- 0️⃣ Moving Zeros to End  
- 🔢 Missing Number Finder  
- 🆔 First Non-Repeating Character  
- ➕ Pair Sum Problem  
- 🅰️ Anagram Checker  
- 📊 Majority Element Logic  
- 🧩 Subarray Sum Problems  
- 🌀 Spiral Matrix Traversal  

---

## 🔍 What I Solved Today  

1. **Rotate a List by k Positions**  
   → Rotated a list to the right by `k` positions using loops and modular arithmetic.  

2. **Intersection of Two Lists**  
   → Found common elements between two lists using loops and sets.  

3. **Move All Zeros to the End**  
   → Moved all zeros to the end while preserving order of other elements.  

4. **Find the Missing Number**  
   → Found the missing number in a sequence using sum formulas.  

5. **First Non-Repeating Character**  
   → Identified the first character in a string that doesn’t repeat.  

6. **Pair Sum Problem**  
   → Found all pairs in a list that sum up to a given target.  

7. **Check for Anagrams**  
   → Checked if two strings are anagrams of each other.  

8. **Majority Element Problem**  
   → Found the element appearing more than n/2 times in a list if it exists.  

9. **Find All Subarrays with a Given Sum**  
   → Identified all subarrays whose sum equals the target.  

10. **Spiral Order Matrix Traversal**  
    → Printed elements of a matrix in spiral order using loops.  

---

## 💭 Daily Reflection  

Today’s problems were **fun but slightly more challenging** than previous days.  
I learned how to break bigger problems into smaller steps and solve them logically.  

These questions improved my **data handling skills** and **algorithmic thinking** in Python.  

As always, **“Small daily wins create massive future results.”**  

---

## 🧠 Sample – Rotate a List by k Positions  

```python
def rotate_list(nums, k):
    n = len(nums)
    k = k % n  # handle if k > n
    rotated = []
    for i in range(n):
        rotated.append(nums[(i - k) % n])
    return rotated

# Example
numbers = [1, 2, 3, 4, 5]
k = 2
print("Original:", numbers)
print(f"Rotated by {k}:", rotate_list(numbers, k))
```
