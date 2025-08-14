def check_ad_blocker(website, blocked_domains):
    if website in blocked_domains:
        return "Ads Blocked"
    else:
        return "Ads Allowed"

website = "example.com"
blocked_domains = ["ads.com", "example.com"]
result = check_ad_blocker(website, blocked_domains)
print(f'Website: {website}')
print(f'Result: {result}')

test_websites = [
    "example.com",
    "ads.com",
    "google.com",
    "youtube.com"
]

for site in test_websites:
    result = check_ad_blocker(site, blocked_domains)
    print(f'{site}: {result}')

def show_blocked_domains(blocked_domains):
    print("Blocked domains:")
    for domain in blocked_domains:
        print(f"  - {domain}")

print(f"\nAd blocker settings:")
show_blocked_domains(blocked_domains)

def add_to_blocklist(blocked_domains, new_domain):
    if new_domain not in blocked_domains:
        blocked_domains.append(new_domain)
        return f"Added {new_domain} to blocklist"
    else:
        return f"{new_domain} already blocked"

print(f"\nAdding new domain:")
message = add_to_blocklist(blocked_domains, "spam.com")
print(message)
print(f"Updated blocklist: {blocked_domains}")