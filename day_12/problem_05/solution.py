def pair_sum(nums, target):
    seen = set()
    pairs = set()
    for num in nums:
        diff = target - num
        if diff in seen:
            pairs.add(tuple(sorted((num, diff))))
        seen.add(num)
    return list(pairs)

print(pair_sum([2, 4, 3, 5, 7, 8], 10))