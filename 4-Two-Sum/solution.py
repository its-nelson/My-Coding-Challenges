def twoSum(nums, target):
    """Returns the indeces of two numbers such that they add up to target"""
    nums_hashmap = {}
    for i, num in enumerate(nums):
        num_needed = target - num
        if num_needed in nums_hashmap:
            return [i, nums_hashmap[num_needed]]
        nums_hashmap[num] = i

# Example 1
print(f"Example 1\nOutput:\n{twoSum([2,7,11,15], 9)}\n")

# Example 2
print(f"Example 2\nOutput:\n{twoSum([3,2,4], 6)}\n")

# Example 3
print(f"Example 3\nOutput:\n{twoSum([3,3], 6)}\n")