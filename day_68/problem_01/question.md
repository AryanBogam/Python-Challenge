Q1. LRU Cache Implementation (Medium-Hard)

Problem: Design an LRU (Least Recently Used) Cache with:
get(key) → returns value if key exists, else -1.
put(key, value) → insert/update, evict least recently used if full.

Concepts: HashMap + Doubly Linked List.
Why: This is an interview classic. Real-world browsers, DBs, OS caching use this.
Hint: Think of storing data + usage order efficiently.