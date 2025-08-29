# 🐍 Day 60/300 – Beginner → Intermediate Social Media–Style Mini Projects  

Today, I explored **Social Media–Style Mini Projects** in Python — building small features inspired by platforms like Facebook using **functions, loops, lists, sets, tuples, and dictionaries**.  

This day was **mentally exhausting** — I’m still juggling **boards + Python challenge**, and honestly, I’m **just keeping the streak alive**. Some projects took time, but I gave my **best possible effort** and completed them all.  

---

## ✅ Topics Practiced  

- 👤 User Authentication & Login Systems  
- 👫 Friend List Management  
- 📰 News Feed Simulations  
- 📝 Status Update Features  
- 💬 Basic Messenger Chats  
- 👍 Like & Comment Systems  
- 👥 Group Creation Logic  
- 📅 Event Invitation Systems  
- 🤝 Friend Recommendation Basics  
- 🔔 Notification Handling  

---

## 🔍 What I Solved Today  

1. **Simple User Registration & Login System**  
   → Created a dictionary-based system for sign-up and login authentication.  

2. **Friend List Manager**  
   → Added, removed, and displayed friends in a list-based app.  

3. **Simple News Feed (Static Posts)**  
   → Printed predefined posts with like counters.  

4. **Status Update App**  
   → Stored and displayed user status updates.  

5. **Basic Messenger Chat**  
   → Simulated one-to-one chat storing messages with sender info.  

6. **Like & Comment System**  
   → Allowed likes & comments on posts using nested data structures.  

7. **Group Creation App**  
   → Created groups with names and member lists.  

8. **Event Invitation System**  
   → Stored events with dates and invited friends.  

9. **Friend Recommendation (Basic Version)**  
   → Suggested mutual friends using set intersections.  

10. **Mini Notification System**  
    → Stored and displayed unread notifications for user actions.  

---

## 💭 Daily Reflection  

Today was **tough** — balancing studies and Python coding is not easy.  
But I realized that even on the hardest days, **showing up matters more than perfection**.  

These projects taught me how **real-world features are built using simple loops, conditions, and data structures** in Python.  

I’m going to keep pushing forward because **“Consistency today builds empires tomorrow.”**  

---

## 🧠 Sample – Simple Login System  

```python
def login_system():
    users = {}
    while True:
        print("\n1. Register\n2. Login\n3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            users[username] = password
            print("Registration successful!")
        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")
            if username in users and users[username] == password:
                print("Login successful!")
            else:
                print("Invalid credentials")
        elif choice == "3":
            break
        else:
            print("Invalid option")

login_system()
```

---
