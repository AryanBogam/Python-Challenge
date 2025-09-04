# 🐍 Day 66/300 – Beginner → Intermediate DSA Problems in Python  

Today, I practiced **Data Structures & Algorithms (DSA)** problems in Python — focusing on **lists, strings, matrices, and number operations** to build strong logical foundations.  

---

## ✅ Topics Practiced  

- 👑 Leaders in Arrays  
- 🔗 Subsequences in Strings  
- 🔢 Distinct Element Counting  
- 📈 Peak Element in Lists  
- 🔠 String Sorting  
- 🧮 Matrix Upper Triangle Sum  
- 🔄 String Rotation  
- 🚫 Disjoint List Check  
- ✖️ Maximum Product Pair  
- 🔁 Palindrome Number Check  

---

## 🔍 What I Solved Today  

1. **Find Leaders in a List**  
   → Identified elements greater than all elements to their right.  

2. **Check for Subsequence**  
   → Verified if one string is a subsequence of another.  

3. **Count Distinct Elements in a List**  
   → Counted unique elements without using `set()`.  

4. **Find Peak Element**  
   → Found an index of an element greater than or equal to its neighbors.  

5. **Sort a String Alphabetically**  
   → Rearranged characters in ascending order manually.  

6. **Sum of Upper Triangle of Matrix**  
   → Computed the sum of elements above and including the diagonal.  

7. **Rotate a String**  
   → Rotated string characters by `k` positions.  

8. **Check if Two Lists are Disjoint**  
   → Checked whether two lists have no common elements.  

9. **Maximum Product of Two Numbers in List**  
   → Found two numbers in a list with the maximum product.  

10. **Check for Palindrome Number**  
    → Verified if an integer reads the same forward and backward without string conversion.  

---

## 💭 Daily Reflection  

Today’s set gave me a mix of **array, string, and matrix logic**.  
I especially liked the **Leaders in Array** and **Palindrome Number** problems because they pushed me to think about iteration and conditions differently.  

The journey is shaping problem-solving intuition one day at a time.  
As always, **“Code a little daily, grow massively eventually.”**  

---

## 🧠 Sample – Leaders in a List  

```python
def find_leaders(arr):
    n = len(arr)
    leaders = []
    max_from_right = arr[-1]
    leaders.append(max_from_right)

    # Traverse from right to left
    for i in range(n - 2, -1, -1):
        if arr[i] >= max_from_right:
            leaders.append(arr[i])
            max_from_right = arr[i]

    return leaders[::-1]  # reverse to keep original order

# Example
nums = [16, 17, 4, 3, 5, 2]
print(find_leaders(nums))  # Output: [17, 5, 2]
