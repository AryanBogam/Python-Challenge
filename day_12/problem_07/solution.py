from collections import Counter

def word_frequency(text):
    words = text.lower().split()
    return dict(Counter(words))

print(word_frequency("AI is the future and the future is AI"))
