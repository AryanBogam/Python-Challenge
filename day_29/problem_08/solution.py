nums = [1, 2, 2, 3, 4, 1, 2, 3, 4, 5]

current = [nums[0]]
longest = [nums[0]]

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        current.append(nums[i])
    else:
        if len(current) > len(longest):
            longest = current
        current = [nums[i]]

if len(current) > len(longest):
    longest = current

print(longest)