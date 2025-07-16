def spam_filter(subject):
    """Flags email as spam based on suspicious keywords and patterns"""
    spam_keywords = ["win money", "click here", "free gift", "urgent"]
    subject_lower = subject.lower()
    
    # Check for spam keywords
    for keyword in spam_keywords:
        if keyword in subject_lower:
            return "SPAM"
    
    # Check for too many exclamation marks
    if subject.count('!') > 2:
        return "SPAM"
    
    return "NOT SPAM"

# Test
print(spam_filter("Click here to win money!!!"))
print(spam_filter("Meeting tomorrow at 3pm"))