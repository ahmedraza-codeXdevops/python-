
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

nums = [-6, 7, 1, -7, 6, 2]
target = 3

print(twoSum(nums, target))
