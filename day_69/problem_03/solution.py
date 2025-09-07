def maximumSum(arr):
    n = len(arr)
    if n == 1:
        return arr[0]
    
    no_delete = [0] * n
    one_delete = [0] * n
    
    no_delete[0] = arr[0]
    one_delete[0] = 0
    
    result = arr[0]
    
    for i in range(1, n):
        no_delete[i] = max(arr[i], no_delete[i-1] + arr[i])
        one_delete[i] = max(one_delete[i-1] + arr[i], no_delete[i-1])
        result = max(result, no_delete[i], one_delete[i])
    
    return result

arr = [1, -2, 0, 3]
result = maximumSum(arr)
print(result)