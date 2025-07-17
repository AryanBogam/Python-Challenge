def compress_message(message):

    if not message:
        return ""
    
    compressed = ""
    current_char = message[0]
    count = 1
    
    for i in range(1, len(message)):
        if message[i] == current_char:
            count += 1
        else:
            compressed += current_char + str(count)
            current_char = message[i]
            count = 1
    
    # Add the last group
    compressed += current_char + str(count)
    return compressed

test_cases = ["aaabbccccd", "hello", "aaa", "abcdef"]
for test in test_cases:
    print(f"'{test}' → '{compress_message(test)}'")