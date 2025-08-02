pnr_db = {
    "1234567890": "Confirmed",
    "2345678901": "RAC", 
    "3456789012": "Waiting List"
}

def check_pnr_status(pnr_number):
    if pnr_number in pnr_db:
        return pnr_db[pnr_number]
    else:
        return "Invalid PNR"
    
test_pnrs = ["1234567890", "2345678901", "9999999999"]

print("PNR STATUS TRACKER")
print("-" * 25)

for pnr in test_pnrs:
    status = check_pnr_status(pnr)
    print(f"PNR {pnr}: {status}")

print("\n" + "="*25)
user_pnr = input("Enter your PNR number: ")
result = check_pnr_status(user_pnr)
print(f"Status: {result}")