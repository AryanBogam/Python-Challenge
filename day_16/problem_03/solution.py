import re

def normalize_text(sentence):
    stopwords = ["the", "is", "at", "on"]
    
    # Convert to lowercase
    text = sentence.lower()
    
    # Remove punctuation and split into words
    words = re.findall(r'\b[a-zA-Z]+\b', text)
    
    # Remove stopwords
    clean_words = [word for word in words if word not in stopwords]
    
    return clean_words

result = normalize_text("The cat is sitting on the mat!")
print(result)