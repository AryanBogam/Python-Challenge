# 🧠 Day 31/300 – Advanced Python Logic Projects

Today’s focus: turning logic into systems.  
I challenged myself with **10 real-world mini projects** to simulate data validation, business flows, scheduling, billing, and string parsing — the kind of logic every product, dashboard, or automation needs behind the scenes.

It wasn’t about loops or conditionals anymore — it was about **building thought-powered logic** with clean input-output design.

---

## ✅ Topics Practiced

- 🔍 Pattern validation & data extraction  
- 🏭 Scheduling with rotation logic  
- 📦 Categorizing data into nested structures  
- 📆 Conflict detection in timeslots  
- 🧾 Result formatting and grading  
- 🍽️ Order grouping with summarization  
- 📶 Usage limit detectors  
- 📧 Email domain parsing  
- 💰 Discount rule engines  
- 🧮 Stateful command calculators  

---

## 🔍 What I Solved Today

1. **Invoice Number Validator**  
   → Validated format `INV-YYYY-XXXX`, extracted year and serial.  
   → Simulated real-world invoice verification and data parsing.

2. **Shift Scheduler**  
   → Assigned rotating shifts to workers without repeat.  
   → Simulated scheduling systems used in manufacturing and logistics.

3. **Parcel Weight Categorizer**  
   → Grouped parcel weights into Light, Medium, Heavy.  
   → Practiced conditionals with real-life shipping logic.

4. **Meeting Room Conflict Checker**  
   → Detected overlaps in meeting slot tuples.  
   → Simulated booking conflict resolution like Google Calendar backend.

5. **Student Result Card Formatter**  
   → Calculated total and assigned grades (A/B/C/Fail).  
   → Printed clean console reports with `.ljust()` formatting.

6. **Restaurant Order Tracker**  
   → Grouped orders by table and identified most ordered item.  
   → Simulated POS (Point of Sale) logic for restaurants.

7. **Mobile Data Usage Analyzer**  
   → Calculated per-user usage, flagged overuse, and showed top consumers.  
   → Built logic like telecom data usage tracking.

8. **Email Domain Extractor**  
   → Parsed emails to find domains and their frequency.  
   → Simulated HR/email-system cleanup and categorization tools.

9. **Discount Engine Simulator**  
   → Applied multiple discount rules (%, flat, capped).  
   → Built a pricing rule engine like e-commerce platforms.

10. **Calculator with Memory**  
    → Interpreted commands: `add`, `sub`, `mult`, `reset`, `show`.  
    → Simulated REPL-style user command processors.

---

## 💭 Daily Reflection

**What I realized today:**  
🚀 Real software isn’t just code — it’s the logic behind decisions, flows, and outcomes.  
From invoice parsing to billing logic to conflict detection — you need to think like a systems architect, not just a coder.

### Lessons:
- Clean logic is more important than fancy syntax  
- Simulate real apps in your head → then write the code  
- Track state, validate input, and protect against edge cases  
- Treat every small program like a micro-product

---

## 🔧 Sample – Invoice Validator

```python
def validate_invoice(code):
    if not code.startswith("INV-"):
        return "Invalid"

    parts = code.split("-")
    if len(parts) != 3 or not parts[1].isdigit() or not parts[2].isdigit():
        return "Invalid"

    year, serial = parts[1], parts[2]
    if len(year) != 4 or len(serial) != 4:
        return "Invalid"

    return f"Valid Invoice\nYear: {year}, Serial: {serial}"

print(validate_invoice("INV-2025-0543"))
