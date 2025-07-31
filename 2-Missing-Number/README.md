# 2. Missing Number (LeetCode #268)

**Link to Problem:** [https://leetcode.com/problems/missing-number/](https://leetcode.com/problems/missing-number/)

## Problem Statement
Given an array `nums` containing `n` distinct numbers in the range `[0, n]`, return the only number in the range that is missing from the array.

---
## My Approach and Thought Process

The problem guarantees that the input array contains `n` distinct numbers from a range that should ideally contain `n + 1` numbers (from 0 to `n`). This means exactly one number is missing.

My solution is based on a mathematical property of sequences. The most efficient way to find the missing number is to calculate the difference between the expected sum of the complete sequence and the actual sum of the numbers present in the input array.

1.  **Calculate the Expected Sum:** The complete sequence should be `0, 1, 2, ..., n`. The sum of this arithmetic series can be found by creating a range from `0` to `len(nums) + 1` and summing its elements.
2.  **Calculate the Actual Sum:** Simply sum all the elements in the input array `nums`.
3.  **Find the Difference:** The missing number is the result of `Expected sum - Actual sum`. This works because the difference is precisely the value of the number that was left out.

This approach avoids the need for sorting or using extra space for a set, making it highly efficient.

---
## Sample Output

### Example 1
```
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
```

### Example 2
```
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
```

### Example 3
```
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
```

---
## Complexity Analysis

* **Time Complexity: O(n)**
    * `sum(nums)` takes O(n) time to iterate through the list.
    * `sum(range(len(nums) + 1))` also takes O(n) time.
    * The overall complexity is dominated by these two operations.
 
* **Space Complexity: O(1)**
    * This solution uses a constant amount of extra space to store the sums, regardless of the size of the input array.
