import re

def filter_valid_plates(plates):
    pattern = r"^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$"
    valid = [plate for plate in plates if re.match(pattern, plate)]
    return valid

plates = ["MH12AB1234", "XYZ123", "DL09C1234", "INVALID123"]
print(filter_valid_plates(plates))