def check_hindi_availability(languages):
    if "Hindi" in languages:
        return "Available in Hindi"
    else:
        return "Not available in Hindi"

languages = ["English", "French", "Hindi"]
result = check_hindi_availability(languages)
print(result)

languages2 = ["English", "Spanish", "German"]
result2 = check_hindi_availability(languages2)
print(result2)