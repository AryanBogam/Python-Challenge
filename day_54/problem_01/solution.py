emails = ["alice@gmail.com", "bob@yahoo.com"]

domains = []
for email in emails:
    domain = email.split("@")[1]
    domains.append(domain)

print(domains)