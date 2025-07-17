def analyze_bios(bios):
    all_words = []
    total_length = 0
    
    for bio in bios:
        words = bio.split()
        all_words.extend(words)
        total_length += len(bio)
    
    # Count words
    word_count = {}
    for word in all_words:
        word_count[word] = word_count.get(word, 0) + 1
    
    # Find most common word
    most_common = max(word_count, key=word_count.get)
    
    # Average length
    avg_length = total_length / len(bios)
    
    # Top 3 keywords
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    top_3 = [word for word, count in sorted_words[:3]]
    
    return {
        "most_common_word": most_common,
        "average_length": avg_length,
        "top_3_keywords": top_3
    }

bios = ["I love coding", "coding is fun", "Python coding rocks"]
print(analyze_bios(bios))