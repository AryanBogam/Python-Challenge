words = ["python", "java", "python", "c++"]

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

for word in word_count:
    print(word, "→", word_count[word])