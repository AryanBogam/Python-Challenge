def filter_odds(nums):
    count = []
    for i in nums:
        if i % 2 != 0:
            count.append(i)
    return count
print(filter_odds([1, 2, 3, 4, 5, 6]))