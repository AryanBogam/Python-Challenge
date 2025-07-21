# 🚦 Day 21 – Smart City Traffic Challenges 

✅ **Topics Applied**
- Conditional logic & pattern detection  
- Real-time system simulation  
- Data structures: lists, dicts, sets  
- Regex for validation  
- Priority-based scheduling  
- Analytics, scoring & decision systems  
- Speed & congestion tracking  
- Emergency logic design  

---

## 🚀 What I Solved Today

Completed **10 Smart City Python challenges** aimed at simulating intelligent traffic systems of the future:

- ✅ Smart Traffic Light Scheduler (rush hour logic)  
- ✅ Emergency Vehicle Detector (priority green)  
- ✅ Red Light Violation Tracker (flagging >3)  
- ✅ Congestion Analyzer (speed-based status)  
- ✅ Smart Parking Finder (real-time slot check)  
- ✅ Peak Hour Detector (vehicle volume logs)  
- ✅ Accident Alert Generator (sudden speed drop)  
- ✅ License Plate Validator (using regex)  
- ✅ Traffic Violation Fine Calculator (₹ logic)  
- ✅ Smart Route Recommender (distance + traffic scoring)

These problems made me think like someone designing real-world solutions for cities — balancing logic, safety, efficiency, and dynamic responses.

---

## 💡 Learning Reflection

This day was about building **intelligent, reactive systems** like those in smart cities:

- Learned to simulate real-world **urban traffic rules** and emergency protocols  
- Applied logic to detect **violations, accidents, and congestion**  
- Practiced writing **scalable, modular Python code**  
- Improved in working with **real-time data structures and traffic models**  
- Realized how even simple city problems need well-planned logic and system thinking

There were moments I got stuck and had to rethink my logic, especially for accident detection and scoring routes. But every challenge made me better at **breaking real-world problems into code**.

**“Smart cities need smart coders.” — Me, after this session**

---

## 🧪 Sample Code – Peak Hour Detection

```python
def detect_peak_hours(traffic_log):
    max_vehicles = max(entry["vehicles"] for entry in traffic_log)
    peak_hours = [entry["hour"] for entry in traffic_log if entry["vehicles"] == max_vehicles]
    return peak_hours

traffic_log = [
    {"hour": "08:00", "vehicles": 120},
    {"hour": "09:00", "vehicles": 250},
    {"hour": "10:00", "vehicles": 250}
]

print(detect_peak_hours(traffic_log))
