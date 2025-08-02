def findDisappearedNumber(nums):
    """Finds all numbers that are missing from an array containing numbers
    in the range [1, n]."""
    set_of_nums = set(nums)
    disappeared_nums = []

    for num in range(1, len(nums) + 1):
        if num not in set_of_nums:
            disappeared_nums.append(num)
    return disappeared_nums

# Example 1
print(f"Example 1\nOutput:\n{findDisappearedNumber([4,3,2,7,8,2,3,1])}\n")

# Example 2
print(f"Example 2\nOutput:\n{findDisappearedNumber([1,1])}\n")