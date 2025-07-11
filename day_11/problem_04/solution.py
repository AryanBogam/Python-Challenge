def word_count(sentence):
    words = sentence.split()
    count = {}
    for word in words:
        count[word] = count.get(word,0) + 1
    return (count)

print(word_count("AI is the future and AI is now"))