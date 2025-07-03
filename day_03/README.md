# 🚀 Day 3 – Python Foundations Level Up

## ✅ Topics Covered
- Tuples and tuple operations
- Variables with tuple data
- Data types in tuples (`int`, `float`, `str`, `bool`)
- Type casting between lists and tuples
- String operations with tuples
- Boolean logic and comparisons
- Operators (`+`, `-`, `*`, `/`, `>`, `<`, `==`, `len()`, `max()`, `min()`)
- Tuple indexing and slicing
- Combining tuples with previously learned concepts
- Problem-solving with tuple-based exercises

---

## 🧪 Sample Code

```python
# Example: Working with student data using tuples
student_info = ("Alice", 85, 92, 78)

# Access name
name = student_info[0]

# Access grades
grades = student_info[1:]

# Calculate average
average = sum(grades) / len(grades)

# Output result
print(f"Student: {name}, Average: {average:.1f}")
