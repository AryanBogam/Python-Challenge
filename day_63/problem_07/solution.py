def find_longest_word(sentence):
    words = sentence.split()
    longest = ""
    
    for word in words:
        if len(word) > len(longest):
            longest = word
    
    return longest

sentence = "I love programming in Python"
result = find_longest_word(sentence)
print(result)