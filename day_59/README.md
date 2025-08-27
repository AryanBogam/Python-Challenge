# 🐍 Day 59/300 – Beginner → Intermediate Mini Projects (Python Crash Course)  

Today, I explored **Python Mini Projects** from *Python Crash Course* — combining **functions, loops, lists, sets, tuples, and dictionaries** into small but real-world programs.  

This day was **mentally draining** — I’m juggling **boards + Python challenge**, and honestly, I’m **just trying to keep the streak alive**. Some problems were tricky, but I gave my **best effort** and completed them all.  

---

## ✅ Topics Practiced  

- 📚 List Management (Add/Remove Items)  
- ✅ To-Do List App Logic  
- 🔤 Unique Word Counters with Sets  
- 🗳️ Polling Systems  
- 🍽️ Menu-Driven Programs with Tuples  
- 🔢 Number Statistics & Math Operations  
- 📖 Guest Book Applications  
- 🗺️ Favorite Places Dictionary  
- 🎰 Lottery Number Generator  
- 🛒 Shopping Cart Apps  

---

## 🔍 What I Solved Today  

1. **Favorite Books Tracker**  
   → Added, removed, and displayed favorite books using lists.  

2. **Simple To-Do List Manager**  
   → Built a text-based task manager with add/remove/view features.  

3. **Unique Words Counter**  
   → Counted unique words in a paragraph using sets.  

4. **Simple Polling App**  
   → Collected and displayed programming language preferences.  

5. **Menu-Driven Restaurant App**  
   → Displayed a fixed menu (tuples), took orders, and printed bills.  

6. **Simple Number Statistics App**  
   → Calculated max, min, sum, and average of user-input numbers.  

7. **Guest Book App**  
   → Stored guest names until 'stop' was entered, then printed total guests.  

8. **Favorite Places Dictionary**  
   → Collected favorite places for multiple people and displayed results.  

9. **Lottery Number Picker**  
   → Generated unique random lottery numbers using sets.  

10. **Shopping Cart App**  
    → Allowed adding/removing items and checkout with total summary.  

---

## 💭 Daily Reflection  

Today was **tougher than expected** — I’m honestly **struggling to balance studies and coding**.  
But even on hard days, I know **consistency > perfection**. These mini projects helped me learn how **simple loops and data structures can create real applications**.  

I’ll keep pushing forward because **“Legends aren’t built in comfort zones.”**  

---

## 🧠 Sample – Simple To-Do List Manager  

```python
def todo_list():
    tasks = []
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Mark Task as Done\n4. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a task: ")
            tasks.append({"task": task, "done": False})
        elif choice == "2":
            for i, t in enumerate(tasks, 1):
                status = "✅" if t["done"] else "❌"
                print(f"{i}. {t['task']} {status}")
        elif choice == "3":
            num = int(input("Task number to mark as done: "))
            if 0 < num <= len(tasks):
                tasks[num-1]["done"] = True
        elif choice == "4":
            break
        else:
            print("Invalid option")

todo_list()
```

---
