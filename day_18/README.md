# 🧠 Day 17 – Intermediate Python Problems: Microsoft Edition 🪟

✅ **Topics Sharpened**
- Outlook data parsing & file system logic  
- Excel-like formula evaluation  
- OneDrive path extraction  
- Azure billing simulation  
- Log file analyzers & security formatting  
- Microsoft-style text tools  

---

## 🚀 What I Practiced

Solved **10 intermediate-level, Microsoft-inspired problems** that simulate real use-cases in the Microsoft ecosystem – from Office automation to system-level data parsing.

This day helped me:
- Apply **problem-solving** in real product environments  
- Master **string parsing**, **date/time logic**, **regex**, and **data simulation**  
- Think like a **software engineer at Microsoft**, building core logic behind apps we use daily  

---

### ✅ Problems Solved

| #  | Title                                      | Status    |
|----|--------------------------------------------|-----------|
| 1  | 📁 Windows Folder Formatter                | ✅ Solved |
| 2  | 📅 Outlook Date Extractor                  | ✅ Solved |
| 3  | 📊 Excel Sheet Formula Evaluator           | ✅ Solved |
| 4  | 🧾 Azure Billing Calculator                | ✅ Solved |
| 5  | 📎 Word Smart Tag Parser                   | ✅ Solved |
| 6  | 🛡️ Windows Security Log Analyzer           | ✅ Solved |
| 7  | 🌐 Microsoft Edge URL Tag Extractor        | ✅ Solved |
| 8  | 🔐 MS Password Complexity Checker          | ✅ Solved |
| 9  | 📚 Word Doc Section Extractor              | ✅ Solved |
| 10 | 🧮 Excel Mini Calc Engine                  | ✅ Solved |

---

## 🧪 Sample – Excel Formula Evaluator 🔢

```python
def evaluate_formula(formula):
    try:
        return eval(formula.strip('='))
    except:
        return "Invalid formula"

print(evaluate_formula("=5+2*3"))  # ➞ 11
print(evaluate_formula("=10/2+7")) # ➞ 12.0
