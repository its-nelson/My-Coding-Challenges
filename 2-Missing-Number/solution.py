def missingNumber(nums):
    """Finds the missing number in an array from the range of 0 to n"""
    # Expected sum: sum(range(len(nums) + 1))
    # Actual sum: sum(nums)
    # Missing number: Expected sum - Actual sum
    return sum(range(len(nums) + 1)) - sum(nums)

# Example 1
print(f"Example 1\nOutput:\n{missingNumber([3,0,1])}\n")

# Example 2
print(f"Example 2\nOutput:\n{missingNumber([0,1])}\n")

# Example 3
print(f"Example 3\nOutput:\n{missingNumber([9,6,4,2,3,5,7,0,1])}\n")

