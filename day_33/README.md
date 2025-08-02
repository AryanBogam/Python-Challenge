# 🚆 Day 33/300 – Railway System Simulation

Today was all about building logic for real-world railway systems like IRCTC using Python.  
From platform allocation to fare calculation and PNR lookup — each challenge forced me to think like an **engineer building for millions**.

Honestly, this was one of the **hardest days so far**.  
I struggled to solve some logic-heavy parts and used **Claude AI** to understand certain questions deeper.  
It wasn’t just coding — it was designing actual systems.

---

## ✅ Topics Practiced

- 🔎 Dictionary lookup and nested data structures  
- 🧾 Data validation and exception handling  
- 🧮 Conditional logic for fares, delays, and platforms  
- 🕐 Time parsing (AM/PM → 24hr format)  
- 🎟 Booking system validations  
- 📊 List & route filtering using index logic  
- 🗂 REPL-style commands for state updates  
- 🔧 Simulating real-world transport workflows  
- ✨ Building clean, single-responsibility functions  

---

## 🔍 What I Solved Today

1. **PNR Status Tracker**  
   → Checked PNR number against a dictionary and returned its current status.  
   → Mimicked IRCTC PNR checking logic.

2. **Train Seat Availability Checker**  
   → Used nested dictionaries to return remaining seats based on train number and class.  
   → Practiced real backend data structure traversal.

3. **Train Route Finder**  
   → Checked if a route is direct between two stations in a given list.  
   → Simulated route planning logic used in real train systems.

4. **Fare Calculator (Dynamic by Class & Distance)**  
   → Built a fare system using class-based rates and distance input.  
   → Made it scalable and realistic for SL, 3A, 2A, 1A.

5. **Train Time Parser (AM/PM to 24hr)**  
   → Converted time strings like “3:15PM” to 24-hour format.  
   → Learned how scheduling logic handles user-friendly time formats.

6. **Ticket Booking Validator**  
   → Validated user input fields for name, age, and seat preference.  
   → Mimicked server-side form validation.

7. **Train Delay Analyzer**  
   → Filtered out only those trains with delays above a certain threshold.  
   → Practiced dictionary iteration with conditions.

8. **Platform Assignment System**  
   → Assigned platforms to trains, ensured uniqueness, and handled conflict cases.  
   → Simulated how stations manage real-time data allocation.

9. **Coach Number Extractor**  
   → Parsed seat codes like “B3-45” into coach and seat number using string manipulation.  
   → Helpful in automating UI for displaying seat layout.

10. **Railway Announcement Generator**  
    → Generated dynamic announcements with or without delay info.  
    → Practiced string formatting for user-facing messaging systems.

---

## 💭 Daily Reflection

Today I really felt what it means to **simulate real software**.

These weren’t textbook exercises — they were blueprints of actual railway logic.  
I had to debug, rethink functions, and model logic the way systems like **IRCTC, DB Bahn, Amtrak** might.

It wasn’t easy.  
I struggled with the platform system, nested dictionaries, and parsing logic.  
Used Claude AI as an assistant to **help break down certain problems**, especially when my mind hit a wall.

But that’s how real builders work — we don’t give up. We **ask, learn, solve**.

---

## 🧠 Sample – PNR Status Tracker

```python
train_to_platform = {
  "12903": 1,
  "12050": 2
}
pnr_db = {
    "1234567890": "Confirmed",
    "2345678901": "RAC",
    "3456789012": "Waiting List"
}

def check_pnr_status(pnr):
    return pnr_db.get(pnr, "Invalid PNR")

print(check_pnr_status("1234567890"))
# Output: Confirmed