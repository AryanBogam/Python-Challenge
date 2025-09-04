def find_leaders(nums):
    leaders = []
    n = len(nums)
    
    for i in range(n):
        is_leader = True
        for j in range(i + 1, n):
            if nums[j] >= nums[i]:
                is_leader = False
                break
        
        if is_leader:
            leaders.append(nums[i])
    
    return leaders

nums = [16, 17, 4, 3, 5, 2]
result = find_leaders(nums)
print(result)