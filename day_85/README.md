Today, I solved the **Meal Time problem** from **Harvard's CS50P Week 1**!  
This problem focused on **time parsing** and **conditional logic** to determine appropriate meal times.  

---

## ✅ Problem Overview  

- ⏰ **Time Parser** → Convert "HH:MM AM/PM" format to decimal hours.  
- 🍽️ **Meal Time Logic** → Determine breakfast, lunch, or dinner based on time.  
- 🔄 **Conditional Statements** → Use if/elif to check time ranges.  
- 🧮 **Mathematical Conversion** → Convert minutes to decimal format (minutes/60).  

---

## 🎯 Problem Solved

### Meal Time Detector
Built a program that:
- Prompts user for current time in "HH:MM AM/PM" format
- Converts time to decimal hours (e.g., 7:30 AM = 7.5)
- Determines meal time based on these ranges:
  - **Breakfast**: 7:00 AM - 7:59 AM
  - **Lunch**: 12:00 PM - 12:59 PM  
  - **Dinner**: 6:00 PM - 6:59 PM

**Example**:
```
What time is it? 7:30 am
breakfast time

What time is it? 12:42 pm
lunch time

What time is it? 6:15 pm
dinner time

What time is it? 11:11 am
(no output - not a meal time)
```

---

## 💭 Daily Reflection  

This problem taught me about **time manipulation** and **string parsing with multiple delimiters**.  
The key insight was converting minutes to decimal format and handling AM/PM logic properly.  

> "Time is just another data type to master — parse it right, and your programs will always know when it's time to eat!" ⏰🍽️