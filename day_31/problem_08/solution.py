emails = ["alice@gmail.com", "bob@yahoo.com", "charlie@gmail.com", "diana@mbzuai.ac.ae", "eve@yahoo.com"]

domain_count = {}

for email in emails:
    parts = email.split("@")
    if len(parts) == 2:
        domain = "@" + parts[1]
        if domain not in domain_count:
            domain_count[domain] = 0
        domain_count[domain] += 1

print("EMAIL DOMAIN ANALYSIS")
print("-" * 30)
print("Email list:")
for email in emails:
    print(f"  {email}")

print("\nDomain Statistics:")
for domain, count in domain_count.items():
    print(f"{domain}: {count} users")

print(f"\nUnique domains found: {len(domain_count)}")