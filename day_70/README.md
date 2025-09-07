# 🐍 Day 70/300 – Intermediate → Hard DSA Problems in Python  

Today, I worked on **Data Structures & Algorithms (DSA)** problems that focused on **backtracking, trees, dynamic programming, union-find, tries, and binary search with DP**.  
These challenges were **medium-to-hard**, requiring structured solutions and efficient use of recursion, hashing, and graph concepts.  

---

## ✅ Topics Practiced  

- 🔤 Backtracking in Strings & Grids (Word Search, Generate Parentheses, Subsets II)  
- 🌳 Binary Tree Traversal Variations (Zigzag Level Order)  
- 🔢 Hashing & Sets (Longest Consecutive Sequence)  
- 🔄 Dynamic Programming on Strings (Palindromic Substrings, Word Break II)  
- 📧 Graphs & Union-Find (Accounts Merge)  
- 🌲 Advanced Trie Operations (Delete Function)  
- 💼 DP + Binary Search (Job Scheduling for Max Profit)  

---

## 🔍 What I Solved Today  

1. **Word Search (Medium)**  
   → Used DFS + backtracking to check if a word exists in a 2D board by exploring all possible paths.  

2. **Binary Tree Zigzag Level Order Traversal (Medium)**  
   → Implemented BFS traversal with alternating direction at each level using a queue.  

3. **Longest Consecutive Sequence (Medium-Hard)**  
   → Solved with HashSet in O(n) by expanding from numbers that start a sequence.  

4. **Palindromic Substrings (Medium)**  
   → Expanded around centers for odd/even cases to count all palindromic substrings.  

5. **Accounts Merge (Medium-Hard)**  
   → Built a graph of emails → accounts and merged connected components using DFS/Union-Find.  

6. **Generate Parentheses (Medium)**  
   → Generated all valid parentheses combinations with recursive backtracking and constraints.  

7. **Subsets II (Medium)**  
   → Created all subsets of an array with duplicates using recursion and skipping duplicate states.  

8. **Implement Trie with Delete Function (Hard Extension)**  
   → Extended Trie with `delete(word)` using reference counters to handle removals safely.  

9. **Word Break II (Hard)**  
   → Combined recursion + memoization to split a string into valid sentences from a dictionary.  

10. **Maximum Profit in Job Scheduling (Hard)**  
    → Used DP with binary search to pick non-overlapping jobs for maximum profit.  

---

## 💭 Daily Reflection  

These problems pushed me to think in **multiple paradigms**: recursion, hashing, DP, and graph theory.  
Highlights for me today:  
- **Accounts Merge** → reminded me how union-find can simplify real-world merging problems.  
- **Generate Parentheses** → elegant recursion that forces disciplined constraints.  
- **Word Break II** → showed how DP + memoization can make brute force feasible.  
- **Job Scheduling** → felt like real-world resource optimization with DP + binary search.  

Every problem felt like **training for interviews** — building not just code, but **problem-solving systems**.  

⚡ Step by step, I’m sharpening both **logic and design sense**.  
As always:  
> “The harder the challenge, the stronger the brain grows.” 🧠  

---

## 🧠 Sample – Generate Parentheses in Python  

```python
class Solution:
    def generateParenthesis(self, n: int):
        result = []

        def backtrack(curr, open_count, close_count):
            if len(curr) == 2 * n:
                result.append(curr)
                return
            if open_count < n:
                backtrack(curr + "(", open_count + 1, close_count)
            if close_count < open_count:
                backtrack(curr + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return result


# Example
s = Solution()
print(s.generateParenthesis(3))
# Output: ["((()))","(()())","(())()","()(())","()()()"]
