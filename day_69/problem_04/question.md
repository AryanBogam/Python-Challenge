Q4. Design Twitter (Mini-System Design)

Problem: Create a class Twitter with:
postTweet(userId, tweetId)
getNewsFeed(userId) → return 10 most recent tweets from user & followees.
follow(followerId, followeeId)
unfollow(followerId, followeeId)

Why: Combines heap + hashmap + list. Real-world "feed ranking" system.