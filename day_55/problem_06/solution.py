def word_frequency(text):
    words = text.split()
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] = frequency[word] + 1
        else:
            frequency[word] = 1
    return frequency

result = word_frequency("the sky is blue the sea is blue")
print(result)