class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.nums = sorted(nums)
    
    def add(self, val):
        self.nums.append(val)
        self.nums.sort()
        
        if len(self.nums) >= self.k:
            return self.nums[-self.k]
        return None

kth_largest = KthLargest(3, [4, 5, 8, 2])
print(kth_largest.add(3))
print(kth_largest.add(5))
print(kth_largest.add(10))
print(kth_largest.add(9))