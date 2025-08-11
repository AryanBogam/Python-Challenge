# 🐍 Day 42/300 – VS Code Logic Systems in Python

Today, I built the **core logic behind VS Code’s main features** — from counting open tabs to simulating auto-save and breakpoints.

It felt like breaking down VS Code into **backend logic modules**, simulating how the editor works under the hood with simple Python scripts.

---

## ✅ Topics Practiced

- 📂 Open file tab counting  
- 🗂 File type statistics  
- 🕒 Recent file tracking  
- 🔍 File search by name  
- 📝 Word search in file content  
- 🧩 Extension checking  
- 💾 Auto-save simulation  
- 🎯 Debug breakpoint tracking  
- 📏 Line counting  
- 🎨 Theme switching  

---

## 🔍 What I Solved Today

1. **File Tab Tracker**  
   → Counted how many files are currently open

2. **File Type Counter**  
   → Counted how many files belong to each file extension

3. **Recent Files List**  
   → Stored only the last N files opened, removing the oldest when the limit was reached

4. **File Search**  
   → Returned all file names containing a specific keyword

5. **Word Search in File Content**  
   → Counted how many times a word appears in a file’s text

6. **Extension List Checker**  
   → Checked if a specific extension is installed

7. **Auto-Save Simulation**  
   → Triggered a save if more than a set time had passed since last save

8. **Debug Breakpoint Tracker**  
   → Checked if a given line number has a breakpoint

9. **Code Line Counter**  
   → Counted total lines and non-empty lines in a file

10. **Theme Switcher**  
    → Switched between Light and Dark themes

---

## 💭 Daily Reflection

Today made me realize **VS Code’s “magic” is just simple logic applied well**.  
Tabs, searches, breakpoints — all built from small, precise operations.

By simulating VS Code in Python, I’m thinking like a **tool builder** who creates the editors that developers depend on daily.

Tomorrow? More logic.  
Because **“Programs must be written for people to read, and only incidentally for machines to execute.” – Harold Abelson**

---

## 🧠 Sample – File Tab Tracker

```python
def file_tab_tracker(open_files):
    return len(open_files)

# Example:
files = ["main.py", "index.html", "styles.css"]
print("Open tabs:", file_tab_tracker(files))
# Output: Open tabs: 3
