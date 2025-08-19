# 🐍 Day 50/300 – Real Usecases of Lists in Python

Today, I explored **real-world usecases of Python lists** — from managing tasks and tracking stock prices to analyzing ratings and checking inventory.  

It felt like simulating **daily systems behind apps like Spotify, Amazon, and IMDb**, showing how much power lists have when solving practical problems.  

This day was **fun, intermediate-level, and realistic** — these problems are the same logical checks used by real-world platforms.  

---

## ✅ Topics Practiced

- 📝 Task management with lists  
- 👥 Unique visitors & duplicate removal  
- 📈 Stock price analysis (min/max)  
- 🎶 Playlist reordering  
- 🛒 Shopping cart billing  
- 🔡 Word frequency counting  
- 🎟️ Event attendance tracking  
- 📚 Library book availability  
- 🏪 Inventory restock alerts  
- ⭐ Movie ratings averaging  

---

## 🔍 What I Solved Today

1. **To-Do List Manager**  
   → Added and removed tasks dynamically.  

2. **Unique Visitors Counter**  
   → Removed duplicates and counted unique users.  

3. **Stock Price Tracker**  
   → Found minimum and maximum prices.  

4. **Playlist Organizer**  
   → Reordered songs by moving positions.  

5. **Shopping Cart**  
   → Calculated total checkout bill.  

6. **Word Frequency Counter**  
   → Counted occurrences of words in a list.  

7. **Event Attendance**  
   → Found common attendees between two events.  

8. **Library Book Tracker**  
   → Checked availability of a searched book.  

9. **Inventory Restock Alert**  
   → Triggered alerts for low stock items.  

10. **Movie Ratings Analyzer**  
    → Calculated average rating from user reviews.  

---

## 💭 Daily Reflection

Today’s challenge gave me a **clearer understanding of lists as the backbone of real-world apps**.  
From **task managers** to **e-commerce carts**, lists are everywhere — they drive how apps store, update, and analyze data.  

By solving these problems, I’m learning to think like a **software engineer who builds scalable systems**, focusing on **efficiency and user experience**.  

Tomorrow? Moving into even **more advanced data structures**.  
Because **“Code is the invisible engine behind every great product.”**  

---

## 🧠 Sample – To-Do List Manager

```python
tasks = ["Buy groceries", "Read book", "Workout"]

# Add a task
tasks.append("Finish Python project")

# Remove a task
tasks.remove("Read book")

print(tasks)
# Output: ['Buy groceries', 'Workout', 'Finish Python project']
