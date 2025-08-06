# 🎬 Day 37/300 – Netflix Logic Systems in Python

Today, I simulated the **core logic of a Netflix-like backend** — from watch time tracking to subscription plan checks, age restrictions, and personalized recommendations.

Even as a beginner, this felt like building **real-world streaming service rules** — the kind that run behind the scenes every time you click play.

---

## ✅ Topics Practiced

- ⏱️ Total watch time calculation in hours & minutes  
- 📝 Subscription plan benefits lookup  
- 🔞 Parental control & age restriction checks  
- 🌟 Highest-rated movie finder  
- ⏳ Duration formatting into `HH:MM:SS`  
- 📈 Continue-watching progress percentage  
- 🌍 Language availability checks  
- 💰 Monthly cost calculations for plans  
- 📊 Watch history counting  
- 🎯 Genre-based recommendation filtering  

---

## 🔍 What I Solved Today

1. **Total Watch Time Calculator**  
   → Summed daily watch times (in minutes)  
   → Converted into hours & minutes.

2. **Subscription Plan Checker**  
   → Mapped plan type to its features.

3. **Parental Control Age Checker**  
   → Allowed or blocked based on minimum age.

4. **Top Rated Movie Finder**  
   → Found the movie with the highest rating from a dictionary.

5. **Episode Duration Formatter**  
   → Converted total seconds into `HH:MM:SS`.

6. **Continue Watching Progress Bar**  
   → Calculated percentage completion of a video.

7. **Language Availability Checker**  
   → Verified if "Hindi" is in the list of available languages.

8. **Monthly Cost Calculator**  
   → Multiplied monthly price by subscription duration.

9. **Watch History Counter**  
   → Counted how many times each movie was watched.

10. **Recommended Genre Filter**  
    → Returned all shows matching a specific genre.

---

## 💭 Daily Reflection

Today reminded me that **streaming services are powered by rules, not magic**.  
Every recommendation, restriction, and progress bar is just **logic applied to data**.

These problems might look simple now, but they’re the same building blocks used in real backend development for platforms like Netflix.  

Tomorrow? We turn these bricks into walls.  
Because **big systems start with small, consistent logic**.

---

## 🧠 Sample – Continue Watching Progress Bar

```python
def watch_progress(watched, total):
    if total == 0:
        return "No content length provided"
    return f"{(watched / total) * 100:.1f}%"

# Example:
print(watch_progress(45, 60))
# Output: 75.0%
