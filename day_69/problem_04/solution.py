class Twitter:
    def __init__(self):
        self.tweets = {}
        self.follows = {}
        self.time = 0
    
    def postTweet(self, userId, tweetId):
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1
    
    def getNewsFeed(self, userId):
        all_tweets = []
        
        if userId in self.tweets:
            all_tweets.extend(self.tweets[userId])
        
        if userId in self.follows:
            for followee in self.follows[userId]:
                if followee in self.tweets:
                    all_tweets.extend(self.tweets[followee])
        
        all_tweets.sort(key=lambda x: x[0], reverse=True)
        return [tweet[1] for tweet in all_tweets[:10]]
    
    def follow(self, followerId, followeeId):
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)
    
    def unfollow(self, followerId, followeeId):
        if followerId in self.follows:
            self.follows[followerId].discard(followeeId)

twitter = Twitter()
twitter.postTweet(1, 5)
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print(twitter.getNewsFeed(1))