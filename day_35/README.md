# 🎥 Day 35/300 – CCTV Surveillance Logic in Python

Today, I simulated the backend brain of a **CCTV surveillance system** — motion detection, footage tracking, storage estimation, suspicious alerts, and more.

Felt like I was writing the logic for a **real-world security control center**, using only beginner-level Python.  
No AI libraries — just raw thinking, smart functions, and system-based logic.

---

## ✅ Topics Practiced

- 🚶 Motion detection using frame comparisons  
- 🧠 Logic-based alerts for suspicious activity  
- 🛠️ Camera health checks and toggling systems  
- 🕹️ Camera rotation simulation with error handling  
- 🧾 Storage space calculations for footage  
- 🌙 Night vision toggle systems  
- ⏱️ Time-based auto shutoff logic  
- 📊 Event logging and analysis  
- 🔍 Missing footage detection  
- 🧮 Room entry/exit tracking system

---

## 🔍 What I Solved Today

1. **Motion Detector Simulation**  
   → Compared two frames (e.g., `"empty"` vs `"person"`)  
   → Returned `True` if motion is detected.

2. **Camera Health Check**  
   → Counted `"on"` and `"off"` statuses in a list of cameras  
   → Output: `Working: X, Not working: Y`

3. **Suspicious Activity Alert System**  
   → Triggered alerts for `"gun"`, `"knife"`, or `"intruder"`  
   → Printed `"ALERT: Suspicious Activity!"`

4. **Camera Rotation Simulation**  
   → Rotated to angle between 0°–360°  
   → If out of range, handled error gracefully.

5. **Storage Space Calculator**  
   → 2 GB/hour per camera  
   → Calculated space = hours × cameras × 2 GB

6. **Night Vision Toggle System**  
   → Switched from `"OFF"` to `"ON"` and vice versa  
   → Printed current night vision state.

7. **Motion Event Logger**  
   → Printed time logs for each motion-detected timestamp  
   → Used list of strings like `"10:30"`, `"11:00"`.

8. **Time-Based Camera Auto-Off**  
   → Shutdown activated between 1 AM–5 AM  
   → Else, camera stays active.

9. **Missing Footage Checker**  
   → Checked for missing hourly recordings (expect 24)  
   → Calculated and printed missing hours.

10. **Simple Person Counter**  
    → Tracked `"enter"` and `"exit"` events  
    → Output: current number of people in room.

---

## 💭 Daily Reflection

Today showed me that **security systems are logic machines** — they're not just about storing footage, they're about thinking ahead.  
You build systems that **react**, **calculate**, and **protect**.

Even as a beginner, this felt like designing the **digital brain of a real CCTV setup**.  
Every function I wrote simulated real field behavior — toggles, alerts, counters, timers.

No AI, no OpenCV — but I’m laying the mental foundation for when those tools come next.

Tomorrow, we take it up a level.  
Because **you don’t just build security — you become it.**

---

## 🧠 Sample – Motion Detector

```python
def is_motion_detected(frame1, frame2):
    return frame1 != frame2

# Example:
print(is_motion_detected("empty", "person"))  
# Output: True
