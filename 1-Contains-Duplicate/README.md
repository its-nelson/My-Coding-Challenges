# 1. Contains Duplicate (LeetCode #217)

**Link to Problem:** [https://leetcode.com/problems/contains-duplicate/](https://leetcode.com/problems/contains-duplicate/)

## Problem Statement
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

---
## My Approach and Thought Process

My strategy relies on the core property of a **Set**: it cannot contain duplicate elements.

The logic is as follows:
1.  Initialize an empty set, `set_of_nums`.
2.  Iterate through each number in the input list `nums` and add it to the set. The set automatically handles duplicates; if a number is already present, the set remains unchanged.
3.  After the loop, compare the length of the original `nums` list with the final length of `set_of_nums`.
4.  If the lengths are different, it confirms that at least one duplicate element was present in the original list. In this case, return `true`.
5.  If the lengths are the same, every element was unique. Therefore, return `false`.

---
## Complexity Analysis

* **Time Complexity: O(n)**
    * We iterate through the `nums` array of *n* elements once to build the set. Each `.add()` operation to a set takes O(1) time on average.

* **Space Complexity: O(n)**
    * In the worst-case scenario where all elements are unique, the `set_of_nums` will grow to store all *n* elements from the input array.