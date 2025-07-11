# 🧠 Day 11 – Python Fundamentals Revision 🔁

✅ **Topics Revised**:  
Strings, Lists, Sets, Tuples, Dictionaries, For/While Loops, Functions, Logic Building

---

## 🚀 What I Practiced

Solved 10 focused problems to master fundamentals and train my logic muscle:

- 🧹 Formatted strings by removing punctuation & replacing spaces
- 🔡 Extracted unique vowels using sets
- 🔁 Reversed a list manually with `.pop()` and `.append()`
- 📊 Counted word frequency using dictionaries
- 🪜 Sorted list of tuples by score using lambda
- 📤 Filtered odd numbers from a list
- 🔗 Merged two dictionaries with overwrite logic
- 🧩 Found common letters using set intersection
- ⬆️ Simulated `max()` using loops
- 🔄 Built a custom palindrome checker function

Each challenge was designed to reinforce real-world programming thinking — not just syntax.

---

## 🧪 Sample – Word Frequency Counter (Dicts + Loops)
```python
def word_count(sentence):
    words = sentence.split()
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count

print(word_count("AI is the future and AI is now"))
# Output: {'AI': 2, 'is': 2, 'the': 1, 'future': 1, 'and': 1, 'now': 1}
