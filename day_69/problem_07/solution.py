def alienOrder(words):
    graph = {}
    in_degree = {}
    
    for word in words:
        for char in word:
            if char not in graph:
                graph[char] = []
                in_degree[char] = 0
    
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_len = min(len(word1), len(word2))
        
        for j in range(min_len):
            if word1[j] != word2[j]:
                graph[word1[j]].append(word2[j])
                in_degree[word2[j]] += 1
                break
    
    queue = []
    for char in in_degree:
        if in_degree[char] == 0:
            queue.append(char)
    
    result = []
    while queue:
        char = queue.pop(0)
        result.append(char)
        
        for neighbor in graph[char]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(result) == len(in_degree):
        return ''.join(result)
    return ""

words = ["wrt", "wrf", "er", "ett", "rftt"]
result = alienOrder(words)
print(result)