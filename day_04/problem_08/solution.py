# Given
your_domains = {"aiworld.com", "buildai.io", "futuretools.ai"}
competitor_domains = {"futuretools.ai", "visionchain.io", "hyperai.net"}
recently_registered = {"buildai.io", "hyperai.net", "skyai.co"}

# Domains that were recently registered
your_recent_domains = your_domains & recently_registered

# Domains shared between you and competitors
overlapping_domains = your_domains & competitor_domains

# Recently registered not owned by either
combined_known_domains = your_domains | competitor_domains
new_threats = recently_registered - combined_known_domains


print(" Your Recently Registered Domains:", your_recent_domains)
print(" Overlapping Domains with Competitors:", overlapping_domains)
print(" Potential New Threats:", new_threats)
