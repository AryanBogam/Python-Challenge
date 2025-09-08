# 🐍 Day 71/300 – Building a Mini-Facebook in Python  

Today, I shifted focus from pure **DSA problems** to **real-world project building**.  
I started developing a **mini-version of Facebook**, breaking down its core features into **10 coding challenges**.  
Each challenge represented a **building block** of the social platform — from user accounts to posts, friends, and notifications.  

---

## ✅ Features Implemented  

- 👤 **User System** → Registration & Login with validation  
- 📝 **Profiles** → Bio, age, city, and education storage  
- 🤝 **Friend Requests** → Send, accept, reject, and manage connections  
- 📰 **News Feed** → Post updates visible to all users  
- 👍💬 **Engagement** → Likes & comments on posts  
- ✉️ **Private Messaging** → User-to-user messaging system  
- 🔍 **Search** → Find users by partial name match  
- 👥 **Groups/Communities** → Create, join, and post inside groups  
- 🔔 **Notifications** → Alerts for likes, comments, and friend requests  

---

## 🔍 What I Solved Today  

1. **User Registration System**  
   → Built a signup system storing username, email, and password in dictionaries with duplicate checks.  

2. **User Login & Authentication**  
   → Added secure login by validating stored credentials and marking active sessions.  

3. **Profile Creation & Update**  
   → Allowed logged-in users to add/edit bio, city, education, and age details.  

4. **Friend Requests (Add/Remove)**  
   → Designed a system to send, accept, or reject requests and manage friend lists.  

5. **News Feed (Posting)**  
   → Implemented a posting system where users can share updates visible to all.  

6. **Like & Comment System**  
   → Enhanced posts with likes and comments, preventing duplicate likes by the same user.  

7. **Private Messaging (Inbox)**  
   → Created a messaging system where users can send and receive messages privately.  

8. **Search Users**  
   → Implemented substring search to find users by username efficiently.  

9. **Groups / Communities**  
   → Added group functionality where users can create/join groups and share posts inside them.  

10. **Notifications System**  
    → Designed notifications for likes, comments, and friend requests to keep users updated.  

---

## 💭 Daily Reflection  

This was a **major leap**:  
- Instead of isolated algorithms, I worked on **system design thinking**.  
- Learned how to **connect multiple features** into a cohesive project.  
- Understood the importance of **data structures (dicts, lists, sets)** for building real-world apps.  

Highlights for me today:  
- **Friend Requests & Graphs** → reminded me that social networks are built on graph structures.  
- **Notifications** → made me realize how small details keep users engaged.  
- **Groups** → expanded the idea of community-driven design inside platforms.  

This day felt like **building a product, not just solving problems**.  
Each problem was a step closer to creating something that people could actually use.  

> “First you practice on problems. Then you practice on products. That’s how empires are built.” ⚡  

---

## 🧠 Sample – User Registration in Python  

```python
users = {}

def register(username, email, password):
    if username in users:
        return "❌ Username already exists."
    for u in users.values():
        if u["email"] == email:
            return "❌ Email already registered."
    users[username] = {"email": email, "password": password, "profile": {}}
    return f"✅ User {username} registered successfully!"

# Example
print(register("aryan", "aryan@example.com", "secure123"))
print(register("aryan", "aryan2@example.com", "newpass"))
