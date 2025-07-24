emails = [
    "alice@gmail.com",
    "bob@yahoo.com",
    "alice@gmail.com",
    "charlie@gmail.com",
    "bob@yahoo.com",
    "diana@outlook.com"
]

print("Original emails:", len(emails))
for email in emails:
    print(email)

unique_emails = set(emails)
clean_list = list(unique_emails)

print(f"\nClean list ({len(clean_list)} emails):")
for email in clean_list:
    print(email)