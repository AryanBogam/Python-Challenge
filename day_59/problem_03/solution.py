paragraph = input("Enter a paragraph: ")
words = paragraph.split()

total_words = len(words)
unique_words = set(words)
unique_count = len(unique_words)

print("Total words:", total_words)
print("Unique words:", unique_count)
print("Unique words list:")
for word in unique_words:
    print("-", word)