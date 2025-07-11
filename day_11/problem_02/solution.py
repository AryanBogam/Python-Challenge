def get_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = set()
    for char in text.lower():
        if char in vowels:
            result.add(char)
    return result


print(get_vowels("Artificial Intelligence"))
