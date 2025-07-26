import time

for cycle in range(3):
    print(f"Cycle {cycle + 1}:")
    
    # Green light - 5 seconds
    for i in range(5, 0, -1):
        print(f"Green: {i}s")
        time.sleep(1)
    
    # Yellow light - 2 seconds  
    for i in range(2, 0, -1):
        print(f"Yellow: {i}s")
        time.sleep(1)
    
    # Red light - 5 seconds
    for i in range(5, 0, -1):
        print(f"Red: {i}s")
        time.sleep(1)
    
    print("---")