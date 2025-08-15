# 🐍 Day 46/300 – Airbnb Logic Systems in Python

Today, I built the **core logic behind Airbnb-like features** — from calculating nightly prices and adding cleaning fees to checking availability, applying discounts, and determining Superhost status.

It felt like simulating **Airbnb’s internal booking operations** in Python, breaking down how the platform handles pricing, availability, reviews, and host performance.

This day was **practical, realistic, and beginner-friendly** — these are the same kinds of logical checks used by real-world booking platforms.

---

## ✅ Topics Practiced

- 💵 Nightly price calculation  
- 🧹 Cleaning fee addition  
- 📅 Date availability check  
- 👫 Guest capacity validation  
- ⭐ Average review rating calculation  
- ⏳ Last-minute booking discounts  
- 📍 Location-based filtering  
- 🛏️ Minimum stay enforcement  
- 📊 Host earnings calculation  
- 🏆 Superhost status check  

---

## 🔍 What I Solved Today

1. **Nightly Price Calculator**  
   → Multiplied nightly rate by number of nights.

2. **Cleaning Fee Adder**  
   → Added cleaning fee to the booking total.

3. **Availability Checker**  
   → Checked if a date was free for booking.

4. **Guest Capacity Validator**  
   → Validated that guest count didn’t exceed the limit.

5. **Review Rating Calculator**  
   → Calculated the average rating from guest reviews.

6. **Last-Minute Discount**  
   → Applied a 10% discount if booking was within 3 days.

7. **Location Filter**  
   → Returned only listings in the desired city.

8. **Minimum Stay Checker**  
   → Verified if requested nights met the host’s minimum stay.

9. **Total Earnings Calculator**  
   → Summed multiple booking totals for a host.

10. **Superhost Status Checker**  
    → Checked if the host qualified for Superhost status.

---

## 💭 Daily Reflection

Today’s challenge gave me a **clear picture of how booking platforms process reservations**.  
Airbnb isn’t just a pretty website — it’s **a set of calculations, filters, and validations** running constantly to make sure both guests and hosts have a smooth experience.

By simulating these rules in Python, I’m starting to think like a **platform engineer**, focusing on **accuracy, usability, and trust**.

Tomorrow? Stepping into **more complex multi-system integrations**.  
Because **“Every big platform starts as a small script.”**

---

## 🧠 Sample – Availability Checker

```python
def check_availability(booked_dates, requested_date):
    return "Available" if requested_date not in booked_dates else "Not Available"

# Example:
print(check_availability(["2025-08-14", "2025-08-15"], "2025-08-16"))
# Output: "Available"
```
