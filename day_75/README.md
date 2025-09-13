# 🐍 Day 75/300 – Mini-YouTube Intermediate Features in Python  

Today, I continued building the **mini-YouTube project** by adding **intermediate features** that enhance engagement, analytics, and personalization.  
These challenges focused on **user interaction, content metrics, and real-world app functionalities** in a modular way.  

---

## ✅ Features Implemented  

- 🏷️ **Video Categories / Tags** → Assign tags to videos for topic-based filtering  
- ❤️ **Top Liked Videos** → Display videos sorted by number of likes  
- 📉 **Dislike Percentage** → Show percentage of dislikes on a video  
- 👍 **Comment Likes** → Allow users to like/unlike individual comments  
- 👤 **User Profile Summary** → Show total uploads, views, comments, and likes given  
- 📝 **Video Description Field** → Add/edit descriptions for each video  
- ❌ **Remove Video / Delete** → Allow authors to delete their videos safely  
- ⏱️ **Recently Watched** → Display last N videos watched by a user  
- 🔎 **Search Channels by Name** → Find channels or authors by name  
- 📊 **Basic Analytics – Most Active User** → Identify the user with the highest engagement  

---

## 🔍 What I Solved Today  

1. **Video Categories / Tags**  
   → Added a `tags` list to videos and allowed searching videos by tag.  

2. **Top Liked Videos**  
   → Sorted videos by number of likes and displayed the top ones.  

3. **Dislike Percentage**  
   → Calculated dislikes as a percentage of total reactions for each video.  

4. **Comment Likes**  
   → Enabled liking/unliking individual comments, stored in a `likes` list.  

5. **User Profile Summary**  
   → Aggregated a user’s total videos, views, comments, and likes for a quick overview.  

6. **Video Description Field**  
   → Added a description key and allowed editing the content of a video.  

7. **Remove Video / Delete**  
   → Allowed only the author to delete a video and updated related references safely.  

8. **Recently Watched**  
   → Displayed the last N videos watched by a user in reverse chronological order.  

9. **Search Channels by Name**  
   → Filtered videos or channels by author name to allow easy discovery.  

10. **Basic Analytics – Most Active User**  
    → Computed the user with the highest total activity (uploads + comments + likes given).  

---

## 💭 Daily Reflection  

Today’s focus was on making the mini-YouTube **more interactive and analytical**:  
- Learned how to handle **nested dictionaries and lists** for comments, likes, and tags.  
- Practiced **sorting, filtering, and aggregation** for meaningful insights.  
- Enhanced personalization features like recently watched videos, top liked videos, and user activity summaries.  

Highlights for me today:  
- **Top Liked Videos & Dislike Percentage** → Introduced basic content metrics.  
- **Comment Likes** → Learned to manage nested user interactions.  
- **User Profile Summary & Most Active User** → Gave a glimpse of real-world analytics dashboards.  

This day felt **rewarding**, combining multiple small features into a realistic, modular project.  
> “Small consistent steps today lead to big products tomorrow.” ⚡  

---

## 🧠 Sample – Video Categories & Top Liked in Python  

```python
videos = []

def upload_video(title, author, tags=[]):
    video_id = len(videos) + 1
    videos.append({
        "id": video_id,
        "title": title,
        "author": author,
        "views": 0,
        "likes": [],
        "dislikes": [],
        "comments": [],
        "tags": tags,
        "description": ""
    })
    return f"✅ Video '{title}' uploaded with ID {video_id}!"

def top_liked_videos(top_n=3):
    sorted_videos = sorted(videos, key=lambda v: len(v["likes"]), reverse=True)
    return sorted_videos[:top_n]

# Example
print(upload_video("Python Tutorial", "Aryan", tags=["Education", "Python"]))
print(upload_video("Vlog Day 1", "Raj", tags=["Vlog"]))
videos[0]["likes"].extend(["Aryan", "Raj"])
print(top_liked_videos())
print(videos)
