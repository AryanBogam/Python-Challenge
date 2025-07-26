longest_word = ""

for i in range(5):
    word = input(f"Enter word {i + 1}: ")

    if len(word) > len(longest_word):
        longest_word = word

print(f"Longest word: {longest_word}")