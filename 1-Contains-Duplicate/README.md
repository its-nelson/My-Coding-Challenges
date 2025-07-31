# 1. Contains Duplicate (LeetCode #217)

**Link to Problem:** [https://leetcode.com/problems/contains-duplicate/](https://leetcode.com/problems/contains-duplicate/)

## Problem Statement
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

---
## My Approach and Thought Process

My strategy relies on the core property of a **Set**: it cannot contain duplicate elements. This provides a very efficient way to solve the problem.

The logic is as follows:
1.  Convert the entire input list `nums` into a set in a single, direct operation: `set(nums)`. This automatically handles the removal of any duplicate values.
2.  Compare the length of the newly created set with the length of the original `nums` list.
3.  If the lengths are **not equal**, it confirms that elements were discarded during the set conversion, which only happens if duplicates were present. In this case, return `true`.
4.  If the lengths are **equal**, it means every element from the original list was unique and made it into the set. Therefore, return `false`.

---
## Sample Output

* **Example 1**
    nums = [1,2,3,1]
    Output = `True`
    The element `1` occurs at the indices `0` and `3`

* **Example 2**
    nums = [1,2,3,4]
    Output = `False`
    No element is repeated.

* **Example 3**
    nums = [1,1,1,3,3,4,3,2,4,2]
    Output = `True`
    Each element in nums is repeated at least `twice`.

---
## Complexity Analysis

* **Time Complexity: O(n)**
    * Building a set from a list of *n* elements takes O(n) time, as each element must be processed.

* **Space Complexity: O(n)**
    * In the worst-case scenario where all elements are unique, the `set_of_nums` will grow to store all *n* elements from the input array.
