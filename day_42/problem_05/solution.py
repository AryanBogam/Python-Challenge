def count_word_in_text(text, word):
    """
    Counts how many times a word appears in the given text
    """
    count = 0
    words = text.split()
    
    for text_word in words:
        clean_word = text_word.strip(".,!?;:")
        if clean_word == word:
            count += 1
    return count

text = "Hello world. Hello again."
word = "Hello"
result = count_word_in_text(text, word)
print(f'Word "{word}" appears {result} times in: "{text}"')

test_text1 = "Python is great. I love Python programming. Python is fun!"
result1 = count_word_in_text(test_text1, "Python")
print(f'"Python" appears {result1} times')

test_text2 = "The quick brown fox jumps over the lazy dog. The fox is quick."
result2 = count_word_in_text(test_text2, "the")
print(f'"the" appears {result2} times (case sensitive)')

result3 = count_word_in_text(test_text2, "The")
print(f'"The" appears {result3} times (case sensitive)')

result4 = count_word_in_text(test_text2, "cat")
print(f'"cat" appears {result4} times')