# 🐍 Day 68/300 – Intermediate → Hard DSA Problems in Python  

Today, I practiced **Data Structures & Algorithms (DSA)** problems in Python — focusing on **graphs, trees, heaps, sliding windows, and backtracking**.  
These problems were longer and more structured, pushing me to think in terms of **efficient data structures + clean code design**.  

---

## ✅ Topics Practiced  

- 🗂️ Caching with HashMap + Linked List  
- 🌉 Graph BFS (Word Ladder, Course Schedule)  
- 🍊 Grid BFS Simulation (Rotting Oranges)  
- 👑 Backtracking (N-Queens)  
- 💧 Two-Pointer Technique (Trapping Rain Water)  
- 🌲 Tree Serialization & Deserialization  
- ⏳ Topological Sorting & Cycle Detection  
- 📈 Sliding Window Optimization  
- ⛓️ Min-Heap for Merging Sorted Lists  
- 🧭 DFS + Memoization in Matrix  

---

## 🔍 What I Solved Today  

1. **LRU Cache Implementation**  
   → Designed a cache that evicts the least recently used item using HashMap + Doubly Linked List.  

2. **Word Ladder**  
   → Found the minimum number of transformations from a start word to an end word using BFS on a dictionary of words.  

3. **Rotting Oranges**  
   → Simulated infection spread across a grid using multi-source BFS to calculate the time until all oranges rot.  

4. **N-Queens Problem**  
   → Placed N queens on a chessboard without conflicts using backtracking and recursion.  

5. **Trapping Rain Water**  
   → Calculated the total trapped rainwater between elevations using two-pointer optimization.  

6. **Serialize and Deserialize Binary Tree**  
   → Implemented methods to convert a binary tree into a string and reconstruct it back into a tree.  

7. **Course Schedule**  
   → Determined if all courses can be completed given prerequisites using graph + topological sort.  

8. **Sliding Window Maximum**  
   → Found the maximum element in each sliding window using a deque for O(n) efficiency.  

9. **Merge K Sorted Lists**  
   → Merged multiple sorted linked lists into one sorted list using a min-heap.  

10. **Longest Increasing Path in a Matrix**  
    → Used DFS + memoization to compute the longest increasing path in a 2D grid.  

---

## 💭 Daily Reflection  

These problems were **heavier than usual** — they required careful structuring, not just quick coding.  
I especially enjoyed:  
- **LRU Cache** → felt like building a real system component.  
- **N-Queens** → reminded me how powerful backtracking can be.  
- **Sliding Window Maximum** → forced me to think beyond brute force and use deques efficiently.  

Each challenge sharpened my **problem-solving intuition** and made me more confident about handling **interview-level questions**.  

Step by step, I’m moving from solving toy problems → designing **scalable solutions**.  
As always, **“DSA is not about the code you write, but the way you think about the problem.”** 💡  

---

## 🧠 Sample – LRU Cache in Python  

```python
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _add(self, node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]


# Example
lru = LRUCache(2)
lru.put(1, 10)
lru.put(2, 20)
print(lru.get(1))   # Output: 10
lru.put(3, 30)      # Evicts key 2
print(lru.get(2))   # Output: -1
