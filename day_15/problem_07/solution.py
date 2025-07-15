def survey_collector():
    scores = []
    
    for i in range(5):
        while True:
            try:
                score = float(input(f"Enter score {i+1} (0-10): "))
                if 0 <= score <= 10:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0-10")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    average = sum(scores) / len(scores)
    high_scores = sum(1 for score in scores if score >= 9)
    
    print(f"All scores: {scores}")
    print(f"Average: {average:.2f}")
    print(f"Scores 9 or above: {high_scores}")

survey_collector()