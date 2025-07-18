def parse_email(raw_email):
    lines = raw_email.strip().split("\n")
    email_data = {}

    for line in lines:
        if line.startswith("From:"):
            email_data["From"] = line[5:].strip()
        elif line.startswith("Subject:"):
            email_data["Subject"] = line[8:].strip()
        elif line.startswith("Date:"):
            email_data["Date"] = line[5:].strip()
    
    return email_data

email = """
From: Satya@microsoft.com
Subject: Azure Updates
Date: Mon, 15 July 2025 10:30:00 GMT
"""

print(parse_email(email))

