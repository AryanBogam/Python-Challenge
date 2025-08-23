# 🐍 Day 54/300 – Fresh Intermediate Python Problems with Real Usecases  

Today, I explored **real-world intermediate Python problems** — from stock price analysis and JSON data filtering to text analytics and simple automation tools.  

It felt like simulating **small systems behind financial dashboards, data analytics pipelines, and automation scripts**, showing how Python powers **data processing, automation, and decision-making**.  

This day was **fun, intermediate-level, and practical** — these problems reflect the **kind of challenges developers solve in real projects**.  

---

## ✅ Topics Practiced  

- 📧 Email Domain Extraction  
- 💹 Stock Price Analysis  
- 🔤 Character Frequency Mapping  
- 🗂️ JSON Data Filtering  
- 🌡️ Temperature Conversion  
- 🔢 Prime Number Generation  
- 🎓 Student Performance Analysis  
- 📝 Duplicate Word Detection  
- 💱 Currency Conversion Basics  
- 🗳️ Simple Voting System  

---

## 🔍 What I Solved Today  

1. **Email Domain Extractor**  
   → Extracted domain names from email addresses.  

2. **Stock Price Difference**  
   → Calculated the maximum single-day profit.  

3. **Character Frequency Heatmap**  
   → Counted each character in a string.  

4. **JSON Data Filter**  
   → Filtered users older than 18 from a JSON list.  

5. **Temperature Unit Converter**  
   → Converted Celsius to Fahrenheit.  

6. **Prime Number Generator**  
   → Generated prime numbers up to a limit.  

7. **Student Grade Analyzer**  
   → Calculated average and top performer.  

8. **Duplicate Word Finder**  
   → Found duplicate words in a text file.  

9. **Currency Converter (Mock)**  
   → Converted USD to INR using fixed rates.  

10. **Simple Voting System**  
    → Counted votes and found the winner.  

---

## 💭 Daily Reflection  

Today’s challenge helped me understand how **Python solves everyday automation and analytics problems**.  
From **finance to education**, these problems show how simple scripts can **analyze, automate, and simplify complex tasks**.  

By solving these problems, I started thinking like a **developer building practical tools** for **data analysis, automation, and reporting**.  

Tomorrow? Moving toward **advanced automation + real-world APIs** where Python powers bigger systems.  
Because **“Every powerful tool starts with a simple script.”**  

---

## 🧠 Sample – Email Domain Extractor  

```python
emails = ["alice@gmail.com", "bob@yahoo.com"]

# Extract domains
domains = [email.split("@")[1] for email in emails]

print(domains)
# Output: ['gmail.com', 'yahoo.com']
