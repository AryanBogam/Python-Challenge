def wordBreak(s, wordDict):
    word_set = set(wordDict)
    memo = {}
    
    def backtrack(start):
        if start in memo:
            return memo[start]
        
        if start == len(s):
            return [""]
        
        result = []
        for end in range(start + 1, len(s) + 1):
            prefix = s[start:end]
            if prefix in word_set:
                suffixes = backtrack(end)
                for suffix in suffixes:
                    if suffix:
                        result.append(prefix + " " + suffix)
                    else:
                        result.append(prefix)
        
        memo[start] = result
        return result
    
    return backtrack(0)

s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
result = wordBreak(s, wordDict)
print(result)