def validate_form(name, email, age):
    results = {}
    
    # Validate name (only letters and spaces)
    results['name'] = name.replace(' ', '').isalpha()
    
    # Validate email (contains @)
    results['email'] = '@' in email
    
    # Validate age (18-100)
    try:
        age_int = int(age)
        results['age'] = 18 <= age_int <= 100
    except:
        results['age'] = False
    
    return results

result = validate_form("John Doe", "john@email.com", "25")
print(result)