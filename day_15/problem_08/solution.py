import random

def math_quiz():
    score = 0
    
    for i in range(3):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(['+', '*'])
        
        if operation == '+':
            correct_answer = num1 + num2
            question = f"What is {num1} + {num2}?"
        else:
            correct_answer = num1 * num2
            question = f"What is {num1} * {num2}?"
        
        while True:
            try:
                answer = float(input(question + " "))
                break
            except ValueError:
                print("Please enter a valid number")
        
        if answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The answer is {correct_answer}")
    
    print(f"Final score: {score}/3")

math_quiz()