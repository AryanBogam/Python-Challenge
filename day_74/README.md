# 🐍 Day 74/300 – Mini-YouTube Core Features in Python  

Today, I started building the **mini-YouTube project** by focusing on **beginner-friendly tasks** that simulate YouTube’s core functionality.  
These challenges focused on **video management, engagement tracking, and personalization features** in a simple, modular way.  

---

## ✅ Features Implemented  

- 🎥 **Video Upload System** → Add new videos with title, author, and auto-generated ID  
- 👀 **View Counter** → Increment view count each time a video is watched  
- 👍 **Like & Dislike System** → Users can like/dislike videos and switch reactions  
- 💬 **Comment System** → Add comments to videos and store them per video  
- 🔍 **Search Videos by Keyword** → Search for videos by title keyword  
- 🔔 **Subscribe to a Channel** → Users can subscribe/unsubscribe to creators  
- 🕒 **Watch History** → Maintain per-user watch history  
- 📈 **Trending Videos** → Sort videos by views in descending order  
- 🎯 **Video Recommendations** → Recommend videos not yet watched by the user  
- 📂 **Simple Playlist Feature** → Users can create playlists and add videos to them  

---

## 🔍 What I Solved Today  

1. **Video Upload System**  
   → Built a function to add new videos, auto-assign unique IDs, and return confirmation.  

2. **View Counter**  
   → Each time a video is watched, incremented its `views` count and displayed total views.  

3. **Like & Dislike System**  
   → Stored likes/dislikes as lists of usernames, allowing users to toggle reactions.  

4. **Comment System**  
   → Added the ability to comment on a video and stored comments as nested dictionaries.  

5. **Search Videos by Keyword**  
   → Implemented case-insensitive title search to filter matching videos.  

6. **Subscribe to a Channel**  
   → Allowed users to subscribe or unsubscribe, storing subscriptions per user.  

7. **Watch History**  
   → Appended watched videos to each user’s watch history list.  

8. **Trending Videos**  
   → Sorted videos by view count and displayed top ones as “trending.”  

9. **Video Recommendations (Basic)**  
   → Recommended videos the user hasn’t watched yet by checking watch history.  

10. **Simple Playlist Feature**  
    → Created user-specific playlists and allowed adding videos by ID.  

---

## 💭 Daily Reflection  

Today’s focus was on building the **core pillars of YouTube**:  
- Learned how to manage **lists of dictionaries** effectively.  
- Practiced **sorting, filtering, and conditional logic** for realistic features.  
- Built personalized features like watch history, recommendations, and playlists.  

Highlights for me today:  
- **Trending Videos** → Sorting taught me about ranking algorithms.  
- **Playlists & Subscriptions** → Helped me understand how apps store per-user data.  
- **Video Recommendations** → My first attempt at simulating a basic recommendation engine.  

This was a **fun project day** — small but meaningful tasks that combine into a real product.  
> “When you break a big product into small problems, you stop feeling overwhelmed and start building.” ⚡  

---

## 🧠 Sample – Video Upload & View Counter in Python  

```python
videos = []

def upload_video(title, author):
    video_id = len(videos) + 1
    videos.append({"id": video_id, "title": title, "author": author, "views": 0, "likes": [], "dislikes": [], "comments": []})
    return f"✅ Video '{title}' uploaded with ID {video_id}!"

def watch_video(video_id):
    for video in videos:
        if video["id"] == video_id:
            video["views"] += 1
            return f"🎥 Watched '{video['title']}' | Total views: {video['views']}"
    return "❌ Video not found."

# Example
print(upload_video("My First Vlog", "Aryan"))
print(watch_video(1))
print(watch_video(1))
print(videos)
