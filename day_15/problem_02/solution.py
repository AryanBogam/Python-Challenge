def loan_eligibility():
    age = int(input("Enter age: "))
    income = float(input("Enter monthly income: "))
    credit_score = int(input("Enter credit score (300-900): "))
    
    if age < 21 or age > 60:
        print("Age must be between 21-60")
        return
    
    if income <= 15000:
        print("Income must be greater than 15,000")
        return
    
    if credit_score < 650:
        print("Credit score must be at least 650")
        return
    
    print("Eligible for loan!")

loan_eligibility()