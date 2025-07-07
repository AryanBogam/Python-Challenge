accuracy = 50
iterations = 0

while accuracy < 90:
    accuracy += 5
    iterations += 1
    
print(f"Model reached 90% accuracy in {iterations} iterations.")