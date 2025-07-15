def age_classifier():
    ages_input = input("Enter ages (comma-separated): ")
    ages_list = ages_input.split(',')
    
    child_count = 0
    adult_count = 0
    senior_count = 0
    
    for age_str in ages_list:
        try:
            age = int(age_str.strip())
            if age < 0:
                continue
            
            if age < 18:
                child_count += 1
            elif age <= 60:
                adult_count += 1
            else:
                senior_count += 1
        except:
            continue
    
    print(f"Child (< 18): {child_count}")
    print(f"Adult (18-60): {adult_count}")
    print(f"Senior (60+): {senior_count}")

age_classifier()