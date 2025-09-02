# 🐍 Day 64/300 – Beginner → Intermediate DSA Problems in Python  

Today, I practiced **Data Structures & Algorithms (DSA)** problems in Python — focusing on **lists, strings, matrices, stacks, and subarray problems** to build logical problem-solving skills.  

---

## ✅ Topics Practiced  

- 🧩 Missing Positive Integer Finder  
- 🧮 Matrix Transpose  
- ➖ Move Negative Numbers to One Side  
- 📈 Longest Increasing Subarray  
- 📝 Word Counter in a Sentence  
- 🔢 Diagonal Sum of Matrix  
- ⚖️ Balanced Parentheses Check  
- ♻️ Duplicate Elements Finder  
- ➕ Row-wise Matrix Sum  
- 📉 Monotonic List Checker  

---

## 🔍 What I Solved Today  

1. **Find the Missing Positive Integer**  
   → Found the smallest positive integer not present in the list.  

2. **Transpose of a Matrix**  
   → Converted rows into columns for a given matrix.  

3. **Move Negative Numbers to One Side**  
   → Shifted negative numbers to the left while preserving order.  

4. **Longest Increasing Subarray**  
   → Calculated the length of the longest increasing subarray.  

5. **Count Words in a Sentence**  
   → Counted the number of words in a string.  

6. **Diagonal Sum of a Matrix**  
   → Found the sum of diagonal elements in a square matrix.  

7. **Check for Balanced Parentheses**  
   → Verified if a string has balanced parentheses using stacks.  

8. **Find Duplicate Elements**  
   → Identified all duplicate elements in a list.  

9. **Sum of Each Row in a Matrix**  
   → Calculated the sum of each row in a matrix.  

10. **Check for Monotonic List**  
    → Checked if the list is entirely non-increasing or non-decreasing.  

---

## 💭 Daily Reflection  

Today’s problems were **fun yet tricky** — especially the **Balanced Parentheses** and **Longest Increasing Subarray** ones, which required extra logical thinking.  

I feel my **loops, conditions, and problem-solving patterns** are improving day by day. The consistency is paying off!  

As always, **“Code a little daily, grow massively eventually.”**  

---

## 🧠 Sample – Check for Balanced Parentheses  

```python
def is_balanced(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
    
    return len(stack) == 0

# Example
expression = "([{}])"
print("Balanced:" if is_balanced(expression) else "Not Balanced")
```
