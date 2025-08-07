# 👻 Day 38/300 – Snapchat Logic Systems in Python

Today, I built the **core logic behind Snapchat’s key features** — from tracking snap streaks and story expiry to filtering bitmoji users and calculating snap scores.

It felt like breaking down Snapchat into **backend logic blocks**, simulating real-world app behavior through simple Python functions.

---

## ✅ Topics Practiced

- 🔥 Snap streak activity tracker  
- 📈 Snap score calculator  
- ⏳ Story expiry status (24h rule)  
- 🧍‍♂️ Bitmoji-enabled user filter  
- 🏆 Top best friends based on snaps  
- 🔓 Snapcode unlock time check  
- 🧾 Friend request validation  
- 👁️ Story view counter  
- 📩 Unopened snap filter  
- 💸 Streak saver check logic  

---

## 🔍 What I Solved Today

1. **Snap Streak Checker**  
   → Checked streak based on consecutive active days  
   → Returned messages like `"🔥 Streak Active!"`, `"❌ Streak Lost"`

2. **Snap Score Calculator**  
   → Summed snaps sent and received for total score

3. **Story Expiry Checker**  
   → Verified if a story was expired (after 24 hours)

4. **Bitmoji Filter**  
   → Filtered and returned users with Bitmoji connected

5. **Best Friend Ranker**  
   → Ranked top 3 friends based on snap frequency

6. **Snapcode Unlock Timer**  
   → Checked if Snapcode feature was unlocked based on remaining time

7. **Friend Request Filter**  
   → Determined whether a friend request can be sent or not

8. **Story View Counter**  
   → Counted the number of users who viewed a story

9. **Filter Unopened Snaps**  
   → Filtered and returned names of users with unopened snaps

10. **Streak Saver Check**  
    → Checked if the user had an active streak saver

---

## 💭 Daily Reflection

Today was a reminder that **apps we use every day are just logic, lists, and conditionals behind the scenes**.  

Snapchat’s addictive UX isn't magic — it's data transformed with clever logic.

Each function today was a **mini backend simulation**. Small, yes — but these are the building blocks of systems that handle millions of users.

Tomorrow? We do it again — bigger, cleaner, sharper.  
Because **empires are built in silence — one solved function at a time.**

---

## 🧠 Sample – Bitmoji Filter

```python
def get_bitmoji_users(users):
    return [user["username"] for user in users if user["bitmoji"]]

# Example:
users = [
    {"username": "arya", "bitmoji": True},
    {"username": "zoe", "bitmoji": False},
    {"username": "milan", "bitmoji": True}
]

print(get_bitmoji_users(users))
# Output: ['arya', 'milan']
