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
print(smallerNumbersThanCurrent([8,1,2,2,3]))

# Example 2
print(smallerNumbersThanCurrent([6,5,4,8]))

# Example 3
print(smallerNumbersThanCurrent([7,7,7,7]))
