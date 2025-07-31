def containsDuplicate(nums):
    """Checks if an array contains any duplicate elements"""
    set_of_nums = set(nums)
    
    return len(nums) != len(set_of_nums)

# Example 1
print(containsDuplicate([1,2,3,1]))

# Example 2
print(containsDuplicate([1,2,3,4]))

# Example 3
print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))