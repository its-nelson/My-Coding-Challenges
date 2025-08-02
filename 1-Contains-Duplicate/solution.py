def containsDuplicate(nums):
    """Checks if an array contains any duplicate elements"""
    set_of_nums = set(nums)
    
    return len(nums) != len(set_of_nums)

# Example 1
print(f"Example 1\nOutput:\n{containsDuplicate([1,2,3,1])}\n")

# Example 2
print(f"Example 2\nOutput:\n{containsDuplicate([1,2,3,4])}\n")

# Example 3
print(f"Example 3\nOutput:\n{containsDuplicate([1,1,1,3,3,4,3,2,4,2])}\n")