# 📱 Day 39/300 – WhatsApp Logic Systems in Python

Today, I built the **core logic behind WhatsApp’s main features** — from checking last seen times and tracking unread messages to organizing pinned chats and finding the most active contact.

It felt like breaking down WhatsApp into **backend logic modules**, simulating how the app works under the hood with simple Python scripts.

---

## ✅ Topics Practiced

- 🕒 Last seen status check  
- 🔔 Unread message counter  
- 👥 Group member sorting  
- ⏳ Status expiry check (24h rule)  
- 📸 Media type counter  
- 🔍 Chat keyword search  
- 🏆 Most active contact finder  
- ⌨️ Typing indicator simulation  
- 📌 Pinned chats organizer  
- 📅 Daily message tracker  

---

## 🔍 What I Solved Today

1. **Last Seen Status Checker**  
   → Compared last seen time with current time  
   → Returned messages like `"Aryan is online"` or `"Aryan was last seen 8 minutes ago"`

2. **Unread Message Counter**  
   → Summed unread counts from multiple chats

3. **Group Member Lister**  
   → Sorted and printed member names alphabetically

4. **WhatsApp Status Expiry**  
   → Checked if a status was active or expired after 24 hours

5. **Media Type Counter**  
   → Counted photos, videos, and documents shared in a chat

6. **Message Search**  
   → Found and returned messages containing a specific keyword

7. **Most Active Contact Finder**  
   → Identified contact with the most sent messages

8. **Typing Indicator Simulation**  
   → Displayed `"Contact is typing..."` if a boolean flag was True

9. **Pinned Chats Organizer**  
   → Listed pinned chats first, then unpinned chats

10. **Daily Message Tracker**  
    → Stored and displayed message counts for each day of the week

---

## 💭 Daily Reflection

Today was proof that **every fancy app feature starts with simple logic**.  
WhatsApp’s smooth chat experience is powered by tiny functions that handle data, check conditions, and update statuses in real-time.

By simulating them in Python, I’m not just coding — I’m **learning to think like a backend engineer**.  
And every day like this moves me one step closer to building systems that scale to millions of users.

Tomorrow? We keep building.  
Because **legacy isn’t given — it’s coded.**

---

## 🧠 Sample – Unread Message Counter

```python
def total_unread(chats):
    return sum(chat["unread"] for chat in chats)

# Example:
chats = [
    {"name": "Mom", "unread": 2},
    {"name": "Work", "unread": 5},
    {"name": "Friends", "unread": 8}
]

print("Total unread messages:", total_unread(chats))
# Output: Total unread messages: 15
