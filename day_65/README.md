# 🐍 Day 65/300 – Beginner → Intermediate DSA Problems in Python  

Today, I practiced **Data Structures & Algorithms (DSA)** problems in Python — focusing on **lists, strings, matrices, subarrays, and set operations** to strengthen my problem-solving foundation.  

---

## ✅ Topics Practiced  

- 🔄 Matrix Rotation  
- 🔢 Even & Odd Counters  
- 🗑️ Element Removal from Lists  
- 📈 Maximum Sum Subarray  
- 🅰️ Pangram Checker  
- 🔗 Intersection of Multiple Lists  
- 🧮 Boundary Sum in Matrices  
- 🔠 Unique Character Checker  
- ✖️ Product of Array Except Self  
- ➕ Row-wise Maximum Sum Finder  

---

## 🔍 What I Solved Today  

1. **Rotate Matrix by 90 Degrees**  
   → Rotated a square matrix 90 degrees clockwise in place.  

2. **Count Even and Odd Numbers**  
   → Counted the number of even and odd elements in a list.  

3. **Remove All Occurrences of a Given Element**  
   → Removed all instances of a given element without using built-ins.  

4. **Find Maximum Sum Subarray**  
   → Used Kadane’s Algorithm to find the max sum of contiguous subarray.  

5. **Check if a String is Pangram**  
   → Checked if a given string contains every alphabet at least once.  

6. **Find Intersection of Multiple Lists**  
   → Found elements common to all given lists.  

7. **Sum of Boundary Elements in Matrix**  
   → Calculated sum of all outermost elements of a matrix.  

8. **Check if String Has All Unique Characters**  
   → Verified if all characters in a string are unique.  

9. **Product of Array Except Self**  
   → Computed product of all array elements except the current one.  

10. **Find Row with Maximum Sum in Matrix**  
    → Identified the row with the highest sum in a matrix.  

---

## 💭 Daily Reflection  

Today’s set was **fun and logical** — especially the **Kadane’s Algorithm** and **Product of Array Except Self**, which improved my understanding of subarray and prefix-suffix concepts.  

Problem-solving speed is getting better, and patterns are becoming clearer. The journey is **building strong coding muscles** day by day!  

As always, **“Code a little daily, grow massively eventually.”**  

---

## 🧠 Sample – Product of Array Except Self  

```python
def product_except_self(nums):
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n
    result = [1] * n

    # Prefix products
    for i in range(1, n):
        prefix[i] = prefix[i-1] * nums[i-1]

    # Suffix products
    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] * nums[i+1]

    # Result = prefix * suffix
    for i in range(n):
        result[i] = prefix[i] * suffix[i]

    return result

# Example
nums = [1, 2, 3, 4]
print(product_except_self(nums))  # Output: [24, 12, 8, 6]
```
