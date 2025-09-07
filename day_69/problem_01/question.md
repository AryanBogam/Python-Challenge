Q1. Median of Data Stream (Medium-Hard)

Problem: Implement a class MedianFinder with methods:

addNum(num) → adds number to stream.

findMedian() → returns median of all numbers so far.

Hint: Use two heaps (max-heap for left, min-heap for right).
Example: Add [1, 2, 3] → Median = 2. Add [1, 2, 3, 4] → Median = 2.5.
Why: Real-world streaming stats (finance, logging).