def list_divider():
    list1_input = input("Enter first list (comma-separated): ")
    list2_input = input("Enter second list (comma-separated): ")
    
    list1 = [float(x.strip()) for x in list1_input.split(',')]
    list2 = [float(x.strip()) for x in list2_input.split(',')]
    
    if len(list1) != len(list2):
        print("Error: Lists must have equal lengths")
        return
    
    results = []
    for i in range(len(list1)):
        try:
            if list2[i] == 0:
                results.append(f"Index {i}: Division by zero error")
            else:
                result = list1[i] / list2[i]
                results.append(f"Index {i}: {result}")
        except Exception as e:
            results.append(f"Index {i}: Error - {e}")
    
    for result in results:
        print(result)
list_divider()