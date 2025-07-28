countries = {"India": "IN", "United States": "US", "Canada": "CA"}

countries_lower = {}
for country, code in countries.items():
    countries_lower[country.lower()] = code

country = input("Enter country name: ")

try:
    code = countries_lower[country.lower()]
    print(f"Country code: {code}")
except KeyError:
    print("Country not found")