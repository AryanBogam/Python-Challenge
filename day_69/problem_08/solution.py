class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.freq = {}
        self.min_freq = 0
    
    def get(self, key):
        if key not in self.cache:
            return -1
        
        value, count = self.cache[key]
        self.cache[key] = (value, count + 1)
        self.freq[key] = self.freq.get(key, 0) + 1
        return value
    
    def put(self, key, value):
        if self.capacity == 0:
            return
        
        if key in self.cache:
            old_value, count = self.cache[key]
            self.cache[key] = (value, count + 1)
            self.freq[key] = self.freq.get(key, 0) + 1
            return
        
        if len(self.cache) >= self.capacity:
            min_freq_key = min(self.freq.keys(), key=lambda k: (self.freq[k], k))
            del self.cache[min_freq_key]
            del self.freq[min_freq_key]
        
        self.cache[key] = (value, 1)
        self.freq[key] = 1

lfu = LFUCache(2)
lfu.put(1, 1)
lfu.put(2, 2)
print(lfu.get(1))
lfu.put(3, 3)
print(lfu.get(2))