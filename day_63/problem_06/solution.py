def count_vowels_consonants(s):
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0
    
    for char in s.lower():
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return vowel_count, consonant_count

s = "hello"
vowels, consonants = count_vowels_consonants(s)
print(f"Vowels: {vowels}, Consonants: {consonants}")