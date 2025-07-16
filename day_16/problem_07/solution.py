def auto_label_emails(emails, categories):
    labeled_emails = []
    
    for email in emails:
        subject = email.get('subject', '').lower()
        sender = email.get('sender', '').lower()
        content = f"{subject} {sender}"
        
        labels = []
        for category, keywords in categories.items():
            if any(keyword.lower() in content for keyword in keywords):
                labels.append(category)
        
        email_copy = email.copy()
        email_copy['labels'] = labels if labels else ['general']
        labeled_emails.append(email_copy)
    
    return labeled_emails

emails = [{"subject": "Invoice #123", "sender": "billing@company.com"}]
categories = {"invoice": ["invoice", "billing"], "promotion": ["sale", "offer"]}
result = auto_label_emails(emails, categories)
print(result)