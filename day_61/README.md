# 🐍 Day 61/300 – Beginner → Easy DSA Problems in Python  

Today, I practiced **Basic DSA (Data Structures & Algorithms)** problems in Python — focusing on **loops, lists, sets, dictionaries, and basic algorithms** to build a stronger foundation before moving to complex topics.  

---

## ✅ Topics Practiced  

- 🔄 List Reversal  
- 🔢 Max & Min Elements in a List  
- 🔤 Palindrome String Check  
- ➕ Summation of List Elements  
- 📊 Frequency Counters with Dictionaries  
- 🔗 Merging Sorted Lists  
- 🎯 Linear Search Basics  
- 🗑️ Removing Duplicates  
- 🥈 Second Largest Element Logic  
- 📈 Sorted List Checker  

---

## 🔍 What I Solved Today  

1. **Reverse a List**  
   → Reversed a list without using built-in functions like `reverse()` or slicing.  

2. **Find Maximum & Minimum**  
   → Implemented logic to find largest & smallest elements manually.  

3. **Palindrome String Check**  
   → Verified whether a string reads the same forward & backward.  

4. **Sum of All Elements**  
   → Calculated total sum of list elements without using `sum()`.  

5. **Count Frequency of Each Element**  
   → Used dictionaries to count occurrences of items in a list.  

6. **Merge Two Sorted Lists**  
   → Combined two sorted lists into one sorted list manually.  

7. **Linear Search**  
   → Searched for an element in a list and returned its index.  

8. **Remove Duplicates**  
   → Returned a new list with unique elements only.  

9. **Find Second Largest Element**  
   → Implemented logic to find second largest element in a list.  

10. **Check if List is Sorted**  
    → Checked whether a list is sorted in ascending order.  

---

## 💭 Daily Reflection  

Today was **less stressful** but **very important** — these small DSA problems helped me **understand logic-building and problem-solving patterns** step-by-step.  

Even though these were beginner-level questions, they **build the base for advanced algorithms**.  

I’m sticking to my goal because **“Consistency > Motivation — daily effort beats random inspiration.”**  

---

## 🧠 Sample – Reverse a List  

```python
def reverse_list(nums):
    reversed_list = []
    for i in range(len(nums)-1, -1, -1):
        reversed_list.append(nums[i])
    return reversed_list

# Example
numbers = [1, 2, 3, 4, 5]
print("Original:", numbers)
print("Reversed:", reverse_list(numbers))
