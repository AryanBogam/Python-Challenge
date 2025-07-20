# 🍏 Day 20 – Apple-Inspired Real-World Python Challenges 🍎

✅ **Topics Applied**
- Email & password validation logic
- Greedy algorithms for optimization
- Time-based conditional scheduling
- NLP-style parsing & spam detection
- Priority-based sorting and simulation
- User behavior tracking
- Device proximity & signal ranking
- Voice input interpretation

---

## 🚀 What I Solved Today

Tackled **10 realistic Apple-inspired Python challenges**, including:

- ✅ Apple ID format & password checker  
- ✅ iPhone storage space optimizer using greedy strategy  
- ✅ iCloud backup decision scheduler  
- ✅ App Store review content filter  
- ✅ Apple Watch fall & heart alert simulation  
- ✅ AirDrop proximity detector with signal sorting  
- ✅ Siri-style natural language reminder parser  
- ✅ Genius Bar queue manager with urgency logic  
- ✅ Privacy toggle tracker with smart help suggestions  
- ✅ iMessage spam detector (links, caps, repetition)

Each problem reflected **the kind of logic Apple engineers build into their ecosystem – blending UX, system intelligence, and behavioral checks**.

---

## 💡 Learning Reflection

Apple’s ecosystem is clean on the outside — but powerful underneath.

These challenges made me:

- Simulate real-world system behaviors like proximity detection, health alerts, spam checks  
- Think like an engineer designing **for real users**, not just passing tests  
- Understand **how context, device logic, and user habits** affect the backend  
- Practice writing **clean, modular, decision-driven Python** code  

Seriously, by solving this question i got stuck many times, In some of the question i have used chatgpt to understand the concept and logic,
but all the problem are solved by me.

**“Think different.” — Steve Jobs**

---

## 🧪 Sample Code – iMessage Spam Detector

```python
def is_spam(message, history):
    links = message.lower().count("http")
    caps = sum(1 for word in message.split() if word.isupper())
    repeated = history.count(message)

    if links > 2 or caps > 5 or repeated > 1:
        return "Spam"
    return "Safe"

history = [
    "BUY NOW http://scam.com",
    "BUY NOW http://scam.com",
    "BUY NOW http://scam.com"
]

print(is_spam("BUY NOW http://scam.com", history))
