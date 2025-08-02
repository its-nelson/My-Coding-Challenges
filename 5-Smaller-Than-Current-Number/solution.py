def smallerNumbersThanCurrent(nums):
    """For each nums[i], finds out how many numbers in the array are 
    smaller than it"""
    sorted_nums = sorted(nums)
    hashmap = {}

    for i, num in enumerate(sorted_nums):
        if num not in hashmap:
            hashmap[num] = i

    smaller_nums = []
    for num in nums:
        smaller_nums.append(hashmap[num])

    return smaller_nums

# Example 1
print(f"Example 1\nOutput:\n{smallerNumbersThanCurrent([8,1,2,2,3])}\n")

# Example 2
print(f"Example 2\nOutput:\n{smallerNumbersThanCurrent([6,5,4,8])}\n")

# Example 3
print(f"Example 3\nOutput:\n{smallerNumbersThanCurrent([7,7,7,7])}\n")
