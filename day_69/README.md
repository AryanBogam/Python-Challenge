# 🐍 Day 69/300 – Intermediate → Hard DSA Problems in Python  

Today, I worked on **Data Structures & Algorithms (DSA)** problems that focused on **heaps, graphs, DP, backtracking, and system design-inspired challenges**.  
These problems were **longer & more structured**, requiring efficient **data structures + careful algorithm design**.  

---

## ✅ Topics Practiced  

- 📊 Two Heaps (Median Finder, Kth Largest in Stream)  
- 🌉 Graph Traversal + Cloning  
- ➕ Dynamic Programming with Variations (Subarray Sum with Deletion)  
- 🐦 Mini System Design (Twitter Feed Simulation)  
- 🧩 Backtracking & Constraint Solving (Sudoku)  
- 🔡 Topological Sort for Alien Dictionary  
- 🗂️ Caching Strategies (LFU Cache)  
- 🔍 Sliding Window with HashMaps (Minimum Window Substring)  
- 🌲 Prefix Trees / Tries (Autocomplete Systems)  

---

## 🔍 What I Solved Today  

1. **Median of Data Stream (Medium-Hard)**  
   → Implemented `MedianFinder` using two heaps to keep track of streaming numbers and return the median in O(log n).  

2. **Clone a Graph (Medium)**  
   → Created a deep copy of a graph using BFS/DFS, handling cycles and references carefully.  

3. **Maximum Subarray Sum with One Deletion (Medium)**  
   → Extended Kadane’s algorithm to allow one deletion, tracking "with deletion" vs "without deletion".  

4. **Design Twitter (Mini-System Design)**  
   → Built a `Twitter` class with methods to post, follow/unfollow, and generate user feeds (top 10 tweets).  

5. **Kth Largest Element in a Stream (Medium)**  
   → Designed a `KthLargest` class using a min-heap to efficiently track the k-th largest element.  

6. **Sudoku Solver (Medium-Hard)**  
   → Solved 9×9 Sudoku board using backtracking with validity checks for rows, cols, and boxes.  

7. **Alien Dictionary (Medium-Hard)**  
   → Built a graph of character dependencies from sorted words and derived order using topological sort.  

8. **LFU Cache (Medium-Hard)**  
   → Designed LFU cache eviction strategy using HashMap + frequency counters.  

9. **Minimum Window Substring (Medium-Hard)**  
   → Applied sliding window + hashmap technique to find the smallest substring containing all characters of `t`.  

10. **Implement Trie (Prefix Tree) (Medium)**  
    → Implemented insert, search, and prefix-matching functionality for autocompletion-like systems.  

---

## 💭 Daily Reflection  

These challenges felt **close to real-world system design** — not just toy problems.  
Highlights for me today:  
- **Median Finder** → reinforced how heaps can balance data dynamically.  
- **Design Twitter** → made me think like a system architect, not just a coder.  
- **Sudoku Solver** → super satisfying once recursion + backtracking clicked.  
- **Alien Dictionary** → gave real insight into how search engines and compilers resolve dependencies.  

Every problem required me to **think about scalability and efficiency** — exactly what’s tested in interviews.  

⚡ Step by step, I’m not just solving problems → I’m **designing smarter systems**.  
As always:  
> “DSA is training the mind to see order in chaos.” 💡  

---

## 🧠 Sample – Median Finder in Python  

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.left = []   # max heap (invert values for min-heap behavior)
        self.right = []  # min heap

    def addNum(self, num: int) -> None:
        # Push to max heap (left)
        heapq.heappush(self.left, -num)
        # Balance: max of left should go to right
        heapq.heappush(self.right, -heapq.heappop(self.left))
        # Ensure left >= right in size
        if len(self.left) < len(self.right):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        return (-self.left[0] + self.right[0]) / 2.0


# Example
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(mf.findMedian())   # Output: 1.5
mf.addNum(3)
print(mf.findMedian())   # Output: 2
