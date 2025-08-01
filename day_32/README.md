# 🧠 Day 32/300 – Twitter Logic Challenges

Today’s focus: **simulating real-world logic using Python** — built around Twitter (X) inspired systems.  
From hashtag extraction to pinned tweet handling, I worked on **10 focused mini-projects** designed to simulate core backend logic like filtering, formatting, validation, and command parsing.

This was less about learning new syntax, and more about **thinking like an engineer building tools for millions**.

---

## ✅ Topics Practiced

- 🔠 Hashtag & mention parsing  
- 🔍 Word and URL filtering  
- 📊 Frequency counting & dictionary manipulation  
- 🚫 Character limit validation with exceptions  
- 🧾 String formatting for user-facing systems  
- 📌 Simulating pinned states and REPL-style commands  
- 🔢 24-hour time conversion  
- 🤖 Input-output logic driven by business rules  
- ❗ Exception handling using try-except  
- 🧠 Writing small functions that feel like real microservices  

---

## 🔍 What I Solved Today

1. **Hashtag Extractor**  
   → Parsed hashtags from a tweet using `.split()` and looped string checks.  
   → Mimicked how Twitter identifies and highlights hashtags.

2. **Tweet Word Counter (Excluding URLs)**  
   → Counted only the non-URL words in a tweet.  
   → Learned to exclude patterns like `http...` from analysis.

3. **User Mention Tracker**  
   → Counted `@mentions` across tweets using a dictionary.  
   → Simulated basic analytics like Twitter Insights.

4. **Tweet Sentiment Categorizer**  
   → Classified tweets into positive, negative, or neutral using keyword matching.  
   → Foundation for building sentiment engines.

5. **Trending Hashtag Finder**  
   → Found top 3 hashtags using frequency count and sorting.  
   → Simulated Twitter’s trending hashtag feature.

6. **Tweet Length Validator**  
   → Checked tweet length against 280-char limit and raised a custom `TweetTooLongError`.  
   → Practiced real-world input validation.

7. **Twitter Bio Formatter**  
   → Collected user details and formatted into a short, tweet-style bio.  
   → Simulated UX logic from Twitter profile editors.

8. **Pinned Tweet Manager**  
   → Allowed only one tweet to be pinned at a time.  
   → Mimicked pinned-tweet systems and tested state-replacement logic.

9. **Follower Comparison Bot**  
   → Compared follower counts from a dictionary and handled missing users with `try-except`.  
   → Simulated backend social metric logic.

10. **Tweet Scheduler Parser**  
    → Parsed schedule strings like `"Tweet at 9AM, 3PM"` into `["09:00", "15:00"]`.  
    → Practiced string parsing and time format conversion.

---

## 💭 Daily Reflection

**What I realized today:**  
🚀 Even the smallest tweet contains logic: from parsing, tracking, and formatting — to limits, validation, and automation.  
This challenge reminded me that the most-used apps are just **layers of simple but sharp logic** stacked cleanly.

### Lessons:
- Think user-first → build logic that feels intuitive  
- Your function names should sound like product features  
- Protect inputs, process smartly, and return clean output  
- Don’t just write code — simulate systems  

---

## 🔧 Sample – Tweet Sentiment Categorizer

```python
def categorize_tweet(tweet):
    positives = ["love", "great", "awesome"]
    negatives = ["hate", "bad", "terrible"]
    tweet = tweet.lower()

    score = 0
    for word in tweet.split():
        if word in positives:
            score += 1
        elif word in negatives:
            score -= 1

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

print(categorize_tweet("I love Python but hate bugs"))
# Output: Neutral
