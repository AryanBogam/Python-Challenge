# 🧠 Day 7 – Python While Loop Mastery 🔁

✅ **Topics Covered**
- `while` loops and control flow
- Loop conditions and exit logic
- Infinite loops with `break` conditions
- Logical thinking with counters and trackers
- Simulated real-world systems using loops
- Input-based decision making

---

## 🚀 What I Built Today

I solved 10 logic-based problems using `while` loops, including:

- ✅ AI training accuracy simulator
- ✅ Secret code guessing game
- ✅ Dream life balance tracker
- ✅ Crypto whale journey tracker
- ✅ Battery life simulator

Each problem helped me think in **terms of condition + repetition** — key to backend logic, automation, and AI loops.

---

## 🧪 Sample Code – Secret Code Game 🔐

```python
secret = 42
guess = -1

while guess != secret:
    guess = int(input("Guess the number: "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")

print("Correct! You cracked the code.")
