# 📺 Day 36/300 – YouTube Logic Systems in Python

Today, I built the **core logic of a YouTube-like backend** — from tracking views and likes to validating uploads and detecting trending videos.

Even though this was **beginner-level Python**, the problems felt like mini real-world systems.  
No APIs, no databases — just pure **problem-solving and clean function logic**.

---

## ✅ Topics Practiced

- 📊 View counting & aggregation  
- 👍 Like/dislike percentage calculations  
- 🚫 Comment moderation with banned word detection  
- ⏱️ Video duration formatting (MM:SS)  
- 🏆 Subscriber milestone checks  
- 🔥 Trending video detection  
- 📂 Playlist duration calculation  
- ✂️ Title shortening logic  
- 📉 Average watch time calculation  
- 📤 Video upload validation based on file size

---

## 🔍 What I Solved Today

1. **Video View Counter**  
   → Summed up views from a list of videos  
   → Output: total view count.

2. **Like Percentage Calculator**  
   → Calculated like percentage from likes and dislikes  
   → Output formatted with `%`.

3. **Comment Word Filter**  
   → Checked for banned words: `"spam"`, `"scam"`, `"fake"`  
   → Output: `"Blocked"` or `"Approved"`.

4. **Video Duration Formatter**  
   → Converted seconds into `MM:SS` format.

5. **Subscriber Milestone Checker**  
   → Determined if a channel earns `"Gold Play Button"`, `"Silver Play Button"`, or encouragement.

6. **Trending Video Detector**  
   → Marked a video as `"Trending"` if views in a day > 50,000.

7. **Playlist Duration Calculator**  
   → Calculated total playlist length in hours and minutes.

8. **Video Title Shortener**  
   → Trimmed titles longer than 50 characters and added `"..."`.

9. **Average Watch Time Calculator**  
   → Computed the average watch time from a list of minutes.

10. **Video Upload Validator**  
    → Checked if file size exceeded 2 GB (2048 MB) and returned appropriate upload status.

---

## 💭 Daily Reflection

Today showed me that **YouTube’s backend is all about data logic** — counting, checking, validating, and formatting.  
It’s not about flashy frontends, it’s about the **rules** that keep the system running smoothly.

These beginner problems laid the mental groundwork for **real backend development**.  
Step by step, I’m moving from **simple scripts** to **system thinking**.

Tomorrow, the challenge gets deeper.  
Because **every great platform is built one logical brick at a time**.

---

## 🧠 Sample – Like Percentage Calculator

```python
def like_percentage(likes, dislikes):
    total = likes + dislikes
    if total == 0:
        return "No ratings yet"
    return f"{(likes / total) * 100:.1f}%"

# Example:
print(like_percentage(120, 30))
# Output: 80.0%
