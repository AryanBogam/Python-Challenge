# 🐍 Day 58/300 – Beginner → Intermediate Pattern Printing Problems  

Today, I explored **Python + Pattern Printing** — moving from simple rectangles and triangles to hollow shapes, zigzags, number pyramids, and even Pascal's triangle.  

This day was **harder than expected** — I **struggled with some logics**, had to **take help at times**, but finally solved all problems. It felt like learning **loop conditions, symmetry, and pattern-building logic** at a deeper level.  

---

## ✅ Topics Practiced  

- ⬛ Hollow Rectangles  
- 📐 Number Triangles  
- 🔄 Inverted Number Pyramids  
- ⬆️ Half Diamond Patterns  
- 🔢 Alternating Number-Star Patterns  
- 🏠 Hollow Triangles  
- ⛰️ Number Pyramids  
- 🧮 Multiplication Table Patterns  
- 🌀 Zigzag Patterns  
- 🔺 Pascal's Triangle Basics  

---

## 🔍 What I Solved Today  

1. **Hollow Rectangle**  
   → Printed a rectangle with borders of `*` and spaces inside.  

2. **Right-Angled Triangle with Numbers**  
   → Created a triangle with sequential numbers per row.  

3. **Inverted Pyramid with Numbers**  
   → Printed decreasing rows of sequential numbers.  

4. **Half Diamond Pattern**  
   → Printed a diamond shape using `*` growing then shrinking.  

5. **Alternating Number-Star Pattern**  
   → Printed rows alternating between numbers and `*`.  

6. **Hollow Triangle Pattern**  
   → Printed a triangle with `*` borders and empty center.  

7. **Number Pyramid**  
   → Printed a symmetric pyramid using numbers.  

8. **Multiplication Table Pattern**  
   → Printed multiplication tables row-wise as patterns.  

9. **Zigzag Pattern**  
   → Printed a zigzag layout using `*` with spacing.  

10. **Pascal's Triangle (Basic Version)**  
    → Printed a basic Pascal's triangle without formulas.  

---

## 💭 Daily Reflection  

Today’s challenge was **tough but satisfying**. Some patterns required **multiple attempts and external help** to fully understand the logic behind loops, spacing, and symmetry.  

By solving these problems, I realized how **loop logic scales into graphics, animations, and UI designs** when combined with creative conditions.  

Tomorrow? I’ll take this **logic-building momentum** forward into **real-world problem solving** with Python.  
Because **“Struggles build mastery, one pattern at a time.”**  

---

## 🧠 Sample – Hollow Rectangle  

```python
def hollow_rectangle(rows, cols):
    for i in range(rows):
        for j in range(cols):
            if i == 0 or i == rows-1 or j == 0 or j == cols-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

hollow_rectangle(4, 5)
# Output:
# *****
# *   *
# *   *
# *****
```
