# CS50P Week 1 - Deep Thought

## Problem Description
Create a program that prompts the user for the answer to the "Great Question of Life, the Universe, and Everything" and responds appropriately based on their input.

## Solution
The program accepts three valid forms of the answer "42":
- `42` (numeric)
- `forty-two` (lowercase with hyphen)
- `Forty Two` (title case with space)

Any other input returns "No".

## How to Run
```bash
python deep.py
```

## Example Output
```
What is the Answer to the Great Question of Life, the Universe, and Everything? 42
Yes

What is the Answer to the Great Question of Life, the Universe, and Everything? hello
No
```