def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = "I love Python coding"
result = count_words(sentence)
print(result)