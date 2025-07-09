# 🧠 Day 9 – Python Function Mastery ⚙️

✅ **Topics Covered**
- Defining and calling functions
- Parameters and return values
- Conditional logic inside functions
- String and list manipulation through functions
- Function reusability and modular thinking
- Input/output control
- Problem solving with reusable logic

---

## 🚀 What I Built Today

I solved 10 structured problems using **custom functions**, including:

- ✅ Greeting logic with dynamic input
- ✅ Manual sum, max, and factorial functions
- ✅ Palindrome and vowel checkers
- ✅ Fibonacci series generator
- ✅ Grade evaluator and custom list reverser

Each problem trained me to **think in input-process-output structure**, preparing me for building scalable logic in AI systems, automation tools, and smart contracts.

---

## 🧪 Sample Code – Palindrome Checker 🔄

```python
def is_palindrome(text):

    cleaned_text = text.lower().replace(" ", "")
    
    ans = cleaned_text == cleaned_text[::-1]
    return ans

user_string = input("Enter a string: ")
result = is_palindrome(user_string)

if result:
    print(f"'{user_string}' is a palindrome!")
else:
    print(f"'{user_string}' is not a palindrome.")
