sentence = "Python is powerful"

words = sentence.split()
words.reverse()
reversed_sentence = " ".join(words)

print(f"Original: {sentence}")
print(f"Reversed: {reversed_sentence}")