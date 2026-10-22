
def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        needed = target - num

        if needed in seen:
            return [seen[needed], i]

        seen[num] = i

nums = [-6, 7, 1, -7, 6, 2]
target = 3

print(twoSum(nums, target))
