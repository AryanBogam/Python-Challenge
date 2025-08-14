def check_browser_mode(is_incognito):
    if is_incognito:
        return "Incognito Mode On"
    else:
        return "Normal Mode"

incognito_status = True
mode = check_browser_mode(incognito_status)
print(mode)

test_cases = [True, False]

for status in test_cases:
    result = check_browser_mode(status)
    print(f"Incognito: {status} -> {result}")

def print_browser_mode(is_incognito):
    if is_incognito:
        print("Incognito Mode On")
    else:
        print("Normal Mode")

print("\nDirect print version:")
print_browser_mode(True)
print_browser_mode(False)