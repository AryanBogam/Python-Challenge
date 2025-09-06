def word_ladder(beginWord, endWord, wordList):
    if endWord not in wordList:
        return 0
    
    queue = [(beginWord, 1)]
    visited = set()
    
    while queue:
        word, steps = queue.pop(0)
        
        if word == endWord:
            return steps
        
        if word in visited:
            continue
        
        visited.add(word)
        
        for next_word in wordList:
            if next_word not in visited:
                diff = 0
                for i in range(len(word)):
                    if word[i] != next_word[i]:
                        diff += 1
                
                if diff == 1:
                    queue.append((next_word, steps + 1))
    
    return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
result = word_ladder(beginWord, endWord, wordList)
print(result)