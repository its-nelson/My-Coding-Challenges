def containsDuplicate(nums):
    """Checks if an array contains any duplicate elements"""
    set_of_nums = set(nums)
    
    if len(nums) != len(set_of_nums):
        return True
    else:
        return False
