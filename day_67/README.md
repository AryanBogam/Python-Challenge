# 🐍 Day 67/300 – Beginner → Intermediate DSA Problems in Python  

Today, I practiced **Data Structures & Algorithms (DSA)** problems in Python — focusing on **lists, strings, stacks, and matrices** to strengthen my logical thinking and implementation skills.  

---

## ✅ Topics Practiced  

- ➕ Insert & Modify Lists  
- 🔍 Index Searching  
- 🔗 String Isomorphism  
- ✨ Pangram Completeness  
- 📦 Stack Implementation  
- 🔠 Common Prefix Matching  
- 🧩 Sublist Checking  
- ⚡ Odd Occurrence Elements  
- 🧮 Matrix Multiplication  
- 🔁 Palindromic Substrings  

---

## 🔍 What I Solved Today  

1. **Insert Element at Specific Index**  
   → Inserted an element into a list at a given index without using `insert()`.  

2. **Find All Indices of an Element**  
   → Returned all indices where a target element appears.  

3. **Check if Two Strings are Isomorphic**  
   → Verified if two strings follow the same character mapping.  

4. **Find Missing Characters in Pangram**  
   → Identified which alphabets are missing from a given string.  

5. **Implement Stack using List**  
   → Created a stack class with `push()`, `pop()`, `peek()`, and `is_empty()` methods.  

6. **Find Longest Common Prefix (Strings)**  
   → Found the longest prefix shared by all words in a list.  

7. **Check if List is a Sublist of Another**  
   → Checked if one list is a contiguous sublist of another list.  

8. **Find Element Occurring Odd Number of Times**  
   → Found the element that occurs an odd number of times using XOR/frequency counting.  

9. **Matrix Multiplication (2D List)**  
   → Multiplied two 2D matrices without using NumPy.  

10. **Find Longest Palindromic Substring**  
    → Found the longest substring of a string that is a palindrome.  

---

## 💭 Daily Reflection  

Today’s problems mixed **list manipulation, string logic, stack fundamentals, and matrix operations**.  
I especially enjoyed implementing the **Stack class** and working on **Longest Palindromic Substring** — both forced me to think in terms of structure and iteration rather than shortcuts.  

Step by step, these DSA challenges are sharpening my **problem-solving intuition**.  
As always, **“DSA is not about memorizing, it’s about practicing until logic becomes instinct.”** 💡  

---

## 🧠 Sample – Implementing Stack in Python  

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0


# Example
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.peek())   # Output: 30
print(s.pop())    # Output: 30
print(s.is_empty())  # Output: False
