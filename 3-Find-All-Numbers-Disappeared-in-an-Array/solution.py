def findDisappearedNumber(nums):
    """Finds all numbers that are missing from an array containing numbers
    in the range [1, n]."""
    set_of_nums = set(nums)
    disappeared_nums = []

    for num in range(1, len(nums) + 1):
        if num not in set_of_nums:
            disappeared_nums.append(num)
    return disappeared_nums