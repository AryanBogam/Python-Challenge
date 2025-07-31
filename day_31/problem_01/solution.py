def validate_invoice(invoice):
    parts = invoice.split("-")

    if len(parts) != 3:
        return "Invalid"

    prefix, year, serial = parts

    if prefix != "INV":
        return "Invalid"

    if len(year) != 4 or not year.isdigit():
        return "Invalid"
    
    if len(serial) != 4 or not serial.isdigit():
        return "Invalid"
    
    return f"Valid - Year: {year}, Serial: {serial}"

invoices = ["INV-2025-0543", "INV-2024-1234", "XYZ-2025-0543", "INV-25-0543"]

for invoice in invoices:
    result = validate_invoice(invoice)
    print(f"{invoice}: {result}")