class MedianFinder:
    def __init__(self):
        self.nums = []
    
    def addNum(self, num):
        self.nums.append(num)
        self.nums.sort()
    
    def findMedian(self):
        n = len(self.nums)
        if n % 2 == 1:
            return self.nums[n // 2]
        else:
            return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2

mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(mf.findMedian())
mf.addNum(3)
print(mf.findMedian())