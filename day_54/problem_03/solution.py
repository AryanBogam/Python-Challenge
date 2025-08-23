text = "hello world"

freq = {}
for char in text:
    if char != " ":
        if char in freq:
            freq[char] = freq[char] + 1
        else:
            freq[char] = 1

print(freq)