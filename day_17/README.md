# 🧠 Day 17 – Intermediate Python Problems 🔍

✅ **Topics Mastered**
- Feed ranking systems & scoring logic  
- Text compression & pattern recognition  
- Time-based user activity tracking  
- Authentication: email format & password strength  
- Graph traversal & loop detection  
- Hashtag & keyword extraction  
- Real-world data simulation & parsing  
- Bio analysis & insights  

---

## 🚀 What I Practiced

Solved **10 intermediate-level, Facebook-inspired problems** that simulate core features in modern social media apps. Built logic for ranking, security, recommendation, analytics, and real-time trend detection.

This day helped me:
- Think in terms of **product-based features**
- Write **modular**, **efficient**, and **scalable** code
- Blend **algorithms**, **regex**, and **data structures** into real solutions

---

### ✅ Problems Solved

1. **Feed Ranking Algorithm** – Scoring and sorting posts like a real newsfeed  
2. **Message Compression** – Compact string encoding system  
3. **Unique Active Users** – 24-hour activity tracker  
4. **User Authentication** – Email and password validator  
5. **Facebook Groups – Common Interests** – User similarity matcher  
6. **Post Keyword Highlighter** – Smart string formatting  
7. **Check-in Tracker** – Most visited location today  
8. **Profile Bio Analyzer** – Word frequency and bio stats  
9. **Friendship Cycle Detector** – Graph-based loop detection  
10. **Trending Hashtag Tracker** – Real-time top 5 hashtag extractor  

---

### 💡 To grow faster, I took help to:
- Plan out graph traversal and dictionary-based solutions  
- Design regex and logic for format validations  
- Think like a **systems engineer** building backend logic for social platforms  

---

## 🧪 Sample – Feed Ranking Algorithm 📊

```python
def rank_posts(posts):

    for post in posts:
        post['score'] = 3 * post['likes'] + 5 * post['comments'] + 10 * post['shares']
    
    sorted_posts = sorted(posts, key=lambda x: x['score'], reverse=True)
    return sorted_posts[:3]

posts = [
    {"id": 1, "likes": 10, "comments": 5, "shares": 2},
    {"id": 2, "likes": 20, "comments": 10, "shares": 5},
    {"id": 3, "likes": 5, "comments": 15, "shares": 1},
    {"id": 4, "likes": 30, "comments": 3, "shares": 8}
]

top_posts = rank_posts(posts)
for post in top_posts:
    print(f"Post {post['id']}: Score = {post['score']}")