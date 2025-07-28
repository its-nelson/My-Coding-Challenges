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