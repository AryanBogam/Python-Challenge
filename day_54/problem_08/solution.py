text = "the sky is blue and the sea is blue"

words = text.split()
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] = word_count[word] + 1
    else:
        word_count[word] = 1

duplicates = []
for word in word_count:
    if word_count[word] > 1:
        duplicates.append(word)

print(duplicates)