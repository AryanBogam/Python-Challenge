# 🐍 Day 47/300 – Gmail Logic Systems in Python

Today, I built the **core logic behind Gmail-like features** — from counting unread emails and filtering labels to detecting spam, grouping threads, and simulating draft auto-saves.  

It felt like simulating **Gmail’s internal email operations** in Python, breaking down how the platform handles inbox management, searching, spam detection, and user experience.  

This day was **practical, realistic, and beginner-to-intermediate friendly** — these are the same kinds of logical checks used by real-world email platforms.  

---

## ✅ Topics Practiced

- 📩 Unread mail counting  
- 🏷️ Label filtering  
- 🚫 Spam detection  
- ⭐ Starred mail tracking  
- 📎 Attachment checking  
- 🔍 Keyword search  
- 📊 Inbox size calculation  
- 🧵 Thread grouping  
- ⚡ Important mail filtering  
- 💾 Draft auto-saving  

---

## 🔍 What I Solved Today

1. **Unread Mail Counter**  
   → Counted how many emails were unread.  

2. **Label Filter**  
   → Filtered emails based on their label (Work, Personal, etc.).  

3. **Spam Detector**  
   → Marked emails as spam if they contained banned keywords.  

4. **Starred Emails Counter**  
   → Counted how many emails were starred.  

5. **Attachment Checker**  
   → Returned emails that had attachments.  

6. **Search by Keyword**  
   → Searched emails by matching subject/body with a keyword.  

7. **Inbox Size Calculator**  
   → Calculated total inbox size in KB.  

8. **Thread Grouping**  
   → Grouped emails together under the same thread ID.  

9. **Important Mail Filter**  
   → Returned only the important emails.  

10. **Draft Auto-Save Simulator**  
    → Simulated Gmail’s auto-save feature for drafts.  

---

## 💭 Daily Reflection

Today’s challenge gave me a **clear picture of how email platforms process and organize communication**.  
Gmail isn’t just a mail client — it’s **a system of filters, counters, and validations** running constantly to ensure a seamless experience for users.  

By simulating these rules in Python, I’m starting to think like a **backend engineer**, focusing on **organization, performance, and user convenience**.  

Tomorrow? Taking on **bigger platform-like systems**.  
Because **“Every big product starts with small scripts.”**  

---

## 🧠 Sample – Spam Detector

```python
def spam_detector(subject):
    banned_keywords = ["lottery", "win", "prize"]
    for word in banned_keywords:
        if word.lower() in subject.lower():
            return "Spam"
    return "Not Spam"

# Example:
print(spam_detector("You won a lottery!"))
# Output: "Spam"
