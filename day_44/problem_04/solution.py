def check_region_availability(region):
    available_regions = ["eastus", "westus", "centralus"]    
    if region in available_regions:
        return "Region available"
    else:
        return "Region not available"

region = "eastus"
result = check_region_availability(region)
print(f'Region "{region}": {result}')

test_regions = [
    "eastus",
    "westus",
    "centralus",
    "northus",
    "southus"
]

for region in test_regions:
    result = check_region_availability(region)
    print(f'{region}: {result}')

def list_available_regions():
    return ["eastus", "westus", "centralus"]

print(f"\nAvailable regions: {list_available_regions()}")