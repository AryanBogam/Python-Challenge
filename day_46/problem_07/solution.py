def filter_by_location(listings, city):
    filtered_listings = []
    for listing in listings:
        if city in listing:
            filtered_listings.append(listing)
    return filtered_listings

listings = ["Paris - Cozy Room", "London - Luxury Flat"]
city = "Paris"
result = filter_by_location(listings, city)
print(result)

all_listings = ["New York - Studio", "Paris - Apartment", "London - House", "Paris - Villa"]
print(filter_by_location(all_listings, "Paris"))
print(filter_by_location(all_listings, "London"))
print(filter_by_location(all_listings, "Tokyo"))