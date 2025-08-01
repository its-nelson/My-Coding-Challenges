def twoSum(nums, target):
    """Returns the indeces of two numbers such that they add up to target"""
    nums_hashmap = {}
    for i, num in enumerate(nums):
        num_needed = target - num
        if num_needed in nums_hashmap:
            return [i, nums_hashmap[num_needed]]
        nums_hashmap[num] = i

# Example 1
print(twoSum([2,7,11,15], 9))

# Example 2
print(twoSum([3,2,4], 6))

# Example 3
print(twoSum([3,3], 6))