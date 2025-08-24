def count_vowels(text):
    vowels = "aeiou"
    count = 0
    for char in text:
        if char.lower() in vowels:
            count = count + 1
    return count

result = count_vowels("hello world")
print(result)