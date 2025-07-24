paragraph = "Python is great. Python is easy to learn. Python is powerful and Python makes coding fun."

words = paragraph.lower().split()
word_count = {}

for word in words:
    clean_word = ""
    for char in word:
        if char.isalpha():
            clean_word = clean_word + char
    
    if clean_word in word_count:
        word_count[clean_word] = word_count[clean_word] + 1
    else:
        word_count[clean_word] = 1

print("Word Frequency:")
for word, count in word_count.items():
    print(f"{word}: {count}")

word_list = []
for word, count in word_count.items():
    word_list.append((word, count))

for i in range(len(word_list)):
    for j in range(len(word_list) - 1):
        if word_list[j][1] < word_list[j + 1][1]:
            word_list[j], word_list[j + 1] = word_list[j + 1], word_list[j]

print("\nTop 3 frequent words:")
for i in range(min(3, len(word_list))):
    print(f"{word_list[i][0]}: {word_list[i][1]}")