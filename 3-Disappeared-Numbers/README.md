# 3. Find All Numbers Disappeared in an Array (LeetCode #448)

**Link to Problem:** [https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)

## Problem Statement
Given an array `nums` of `n` integers where `nums[i]` is in the range `[1, n]`, return an array of all the integers in the range `[1, n]` that do not appear in `nums`.

---
## Sample Output

### Example 1
```
Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Explanation: n = 8 since there are 8 numbers. The numbers missing from the range [1,8] are 5 and 6 since they do not appear in nums.
```

### Example 2
```
Input: nums = [1,1]
Output: [2]
Explanation: n = 2 since there are 2 numbers. The number missing from the range [1,2] is 2 since it does not appear in nums.
```

---
## My Approach and Thought Process

The goal is to identify which numbers are missing from the input array, given that the array should contain numbers from `1` to `n`.

My solution uses a **Set** to efficiently check for the existence of numbers by removing duplicates. The logic is as follows:

1.  **Create a Set of Existing Numbers:** First, I convert the input array `nums` into a set (`set_of_nums`). This provides a fast way to check if a number is present, with an average lookup time of O(1).
2.  **Iterate Through the Full Range:** I then loop through the complete range of expected numbers, which is from `1` to `n` (inclusive). The value of `n` is simply the length of the `nums` array.
3.  **Check for Missing Numbers:** For each number in the complete range, I check if it exists in `set_of_nums`.
4.  **Collect Disappeared Numbers:** If a number is **not** found in the set, it means it was missing from the original array. I append this number to a `disappeared_nums` list.
5.  **Return the Result:** Finally, I return the `disappeared_nums` list, which now contains all the numbers that were missing.

---
## Complexity Analysis

* **Time Complexity: O(n)**
    * Creating the set from the `nums` array takes O(n) time.
    * The loop runs `n` times (from 1 to `n`). Inside the loop, the `in` check against a set is an O(1) operation on average.
    * Therefore, the total time complexity is dominated by the initial set creation and the loop, resulting in O(n).