class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_word = True
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_word
    
    def delete(self, word):
        def delete_helper(node, word, index):
            if index == len(word):
                if not node.is_end_word:
                    return False
                node.is_end_word = False
                return len(node.children) == 0
            
            char = word[index]
            if char not in node.children:
                return False
            
            should_delete_child = delete_helper(node.children[char], word, index + 1)
            
            if should_delete_child:
                del node.children[char]
                return not node.is_end_word and len(node.children) == 0
            
            return False
        
        delete_helper(self.root, word, 0)

trie = Trie()
trie.insert("apple")
trie.insert("app")
print(trie.search("app"))
trie.delete("app")
print(trie.search("app"))
print(trie.search("apple"))