# 🧠 Day 16 – Real-World Python Challenges Inspired by Google 🌐

✅ **Topics Covered**  
- Data cleaning & string processing  
- Basic NLP preprocessing  
- Real-world input validation  
- Smart assistants & command parsing  
- Spam detection logic  
- Duplicate handling and file filtering  
- Ranking and sorting with conditions  
- ETA and metric-based calculations  

---

## 🚀 What I Solved Today

I worked on **10 Python problems** inspired by **real Google-level systems** like Search, Gmail, Assistant, Maps, YouTube, and Photos. Each problem sharpened my ability to:

- 🧠 Think in terms of real-world logic and data validation  
- 🔍 Simulate backend logic used in AI and big tech systems  
- 🛠️ Break down problems into functions, validate input, and format output clearly  

---

## ✅ Real-World Problems Tackled

| Problem                              | Key Skill                             |
|--------------------------------------|----------------------------------------|
| 🔤 Search Autocomplete Logic         | Startswith string filtering            |
| 🚫 Spam Filter Rule Checker          | Keyword detection + logic              |
| 🧹 AI Word Normalizer                | Text preprocessing with stopwords      |
| 📋 Google Form Validator             | Field validation and type-checking     |
| 📺 YouTube Watch History Cleaner     | Deduplication with reverse logic       |
| 🧠 Smart Assistant Parser            | Input parsing and extraction           |
| ✉️ Gmail Auto-Label System           | Categorization using keyword mapping   |
| 🕐 Google Maps ETA Simulator         | Distance-speed-time formula            |
| 🖼️ Image File Validator              | Extension filtering                    |
| 📊 Relevance Ranker                  | Custom ranking based on metric         |

---

## 🧪 Sample Code – Smart Assistant Parser

```python
def parse_command(command):
    command = command.lower()
    parsed = {"action": None, "device": None, "location": None}
    if "turn on" in command or "turn off" in command:
        parsed["action"] = "turn on" if "turn on" in command else "turn off"
    if "light" in command or "lights" in command:
        parsed["device"] = "lights"
    if "living room" in command:
        parsed["location"] = "living room"
    elif "bedroom" in command:
        parsed["location"] = "bedroom"
    return parsed

# Output: {'action': 'turn on', 'device': 'lights', 'location': 'living room'}
