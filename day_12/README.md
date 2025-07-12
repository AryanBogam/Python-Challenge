# 🧠 Day 12 – Intermediate to Advanced Python Challenges 🚀

✅ **Topics Practiced**:  
String manipulation, Data structures (lists, sets, dicts), Functions, Logic building, Input validation, Nested loops, Algorithmic thinking

---

## 🚀 What I Practiced

I solved 10 **intermediate to advanced-level problems** that pushed my logic and problem-solving skills to the next level. These weren’t just syntax drills — they required **conceptual clarity, structured reasoning, and pattern recognition**.

To grow faster, I took help to:
- Understand how to approach harder problems
- Break them down into manageable parts
- Think like a developer solving real challenges — not just completing a course
- Sharpen my logic, way of thinking, and critical problem-solving mindset
- Honestly, I relied a lot on help during this phase to move from basic to advanced thinking.

These problems sharpened my ability to **structure cleaner code, design reusable functions**, and **think algorithmically** — all essential for AI, automation, and real-world tech building.

---

### ✅ Problems Solved:
- 🔄 Sentence-level Palindrome Checker (ignoring spaces/case)
- 🔁 Right-rotation of Lists by K steps
- 🧱 Balanced Brackets Checker (`{[()]}`)
- 🧮 Flattening a Nested List (without recursion)
- 🔢 Find All Unique Pairs That Sum to a Target
- 🧬 Check If Two Strings Are Isomorphic
- 📊 Count Word Frequencies in Paragraphs
- 🧠 Longest Word Extractor
- 📦 Custom String Compressor (`aabcc → a2b1c2`)
- 🧩 Sudoku Board Validator (rules logic)

---

## 🧪 Sample – Compress a String (`aabcc → a2b1c2`)
```python
def compress_string(s):
    if not s:
        return ""
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1
    result += s[-1] + str(count)
    return result

print(compress_string("aabcccccaaa"))  # Output: a2b1c5a3
