def missingNumber(nums):
    """Finds the missing number in an array from the range of 0 to n"""
    expected_sum = sum(range(len(nums) + 1))
    actual_sum = sum(nums)
    return expected_sum - actual_sum